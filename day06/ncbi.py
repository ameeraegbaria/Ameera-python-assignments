import argparse
import csv
import os
from datetime import datetime
import requests
from xml.etree import ElementTree

# Base URL for NCBI E-utilities
BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

# Function to search and download data from NCBI
def search_and_download(database, term, number, output_format):
    try:
        print(f"🔍 Searching NCBI database '{database}' for term '{term}'...")
        search_url = f"{BASE_URL}esearch.fcgi"
        search_params = {
            "db": database,
            "term": term,
            "retmax": number,
            "retmode": "xml"
        }

        # Perform the search request
        search_response = requests.get(search_url, params=search_params)
        search_response.raise_for_status()

        # Parse the search results
        root = ElementTree.fromstring(search_response.text)
        ids = [id_elem.text for id_elem in root.findall(".//Id")]
        total_found = root.find(".//Count").text if root.find(".//Count") is not None else "0"

        print(f"Found {total_found} items. Downloading up to {len(ids)}...")

        filenames = []

        for i, record_id in enumerate(ids):
            try:
                fetch_url = f"{BASE_URL}efetch.fcgi"
                fetch_params = {
                    "db": database,
                    "id": record_id,
                    "rettype": output_format,
                    "retmode": "text"
                }

                # Perform the fetch request
                fetch_response = requests.get(fetch_url, params=fetch_params)
                fetch_response.raise_for_status()

                filename = f"{term}_{i+1}.{output_format}"
                with open(filename, "w") as file:
                    file.write(fetch_response.text)
                filenames.append(filename)
                print(f"✔️ Saved {filename}")
            except Exception as e:
                print(f"❌ Error downloading ID {record_id}: {e}")

        return filenames, total_found
    except Exception as e:
        print(f"❌ Error occurred while downloading data from NCBI: {e}")
        return [], 0

# Function to log search details to a CSV file
def log_search_details(csv_filename, date, database, term, max_number, total_found, status="success"):
    file_exists = os.path.isfile(csv_filename)
    with open(csv_filename, mode="a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        if not file_exists:
            writer.writerow(["date", "database", "term", "max", "total", "status"])
        writer.writerow([date, database, term, max_number, total_found, status])

# Main function to parse arguments and execute the script
def main():
    parser = argparse.ArgumentParser(description="Download data from NCBI.")
    parser.add_argument("--database", type=str, default="nucleotide", help="NCBI database to query (default: nucleotide)")
    parser.add_argument("--term", type=str, required=True, help="Search term")
    parser.add_argument("--number", type=int, default=10, help="Maximum number of items to download (default: 10)")
    parser.add_argument("--format", type=str, default="fasta", choices=["fasta", "gb"], help="Output file format (default: fasta)")

    args = parser.parse_args()

    database = args.database
    term = args.term.strip()
    number = args.number
    output_format = args.format

    if not term.isalnum():
        print(f"⚠️ Warning: The search term '{term}' contains non-alphanumeric characters.")

    # Get the current date and time
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Search and download data
    filenames, total_found = search_and_download(database, term, number, output_format)

    if filenames:
        print("Downloaded files:")
        for filename in filenames:
            print(f"  {filename}")
    else:
        print("No files downloaded.")

    # Log the search
    log_search_details("search_log.csv", date, database, term, number, total_found, status="failed" if total_found == "0" else "success")
    print("Search details logged to search_log.csv")

if __name__ == "__main__":
    main()
