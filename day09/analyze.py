import argparse
import re

def parse_fasta(file_path):
    """Extracts the sequence from a FASTA file."""
    try:
        with open(file_path, "r") as file:
            sequence_lines = []
            for line in file:
                line = line.strip()
                if not line.startswith(">"):
                    sequence_lines.append(line)
            return "".join(sequence_lines)
    except FileNotFoundError:
        raise ValueError(f"File not found: {file_path}")
    except Exception as e:
        raise ValueError(f"Error reading the file: {e}")

def find_repeated_segment(sequence):
    """Identifies the longest repeated segment in the sequence."""
    sequence_length = len(sequence)
    longest_repeat = ""

    # Use a dynamic programming table to store matches
    dp_table = [[0] * (sequence_length + 1) for _ in range(sequence_length + 1)]

    for i in range(1, sequence_length + 1):
        for j in range(i + 1, sequence_length + 1):
            if sequence[i - 1] == sequence[j - 1] and dp_table[i - 1][j - 1] + 1 < (j - i):
                dp_table[i][j] = dp_table[i - 1][j - 1] + 1
                repeated_segment = sequence[i - dp_table[i][j]:i]
                if len(repeated_segment) > len(longest_repeat):
                    longest_repeat = repeated_segment

    return longest_repeat

def calculate_gc_percentage(sequence):
    """Calculates the GC content percentage of a DNA sequence."""
    gc_count = sequence.upper().count("G") + sequence.upper().count("C")
    return (gc_count / len(sequence) * 100) if len(sequence) > 0 else 0

def main():
    parser = argparse.ArgumentParser(description="Analyze sequences for repeated segments and GC content.")
    parser.add_argument("file", help="Path to the input FASTA file.")
    parser.add_argument("--repeat", action="store_true", help="Find the longest repeated segment in the sequence.")
    parser.add_argument("--gc", action="store_true", help="Calculate the GC content percentage.")

    args = parser.parse_args()

    try:
        # Parse sequence from the input file
        sequence = parse_fasta(args.file)

        if not args.repeat and not args.gc:
            print("No analysis option specified. Use --repeat or --gc to perform an analysis.")
            return

        if args.repeat:
            longest_segment = find_repeated_segment(sequence)
            print(f"Longest repeated segment: {longest_segment if longest_segment else 'None found'}")

        if args.gc:
            gc_content = calculate_gc_percentage(sequence)
            print(f"GC content: {gc_content:.2f}%")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
