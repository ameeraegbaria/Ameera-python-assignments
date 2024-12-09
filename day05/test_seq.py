
from SeqStats import calculate_statistics

def test1():
    fileName = 'seq1.txt'
    with open(fileName, 'w') as f:
        f.write("ACAGTACCTTTT")
    tot_count = calculate_statistics([fileName])

    assert tot_count == {'A':3, 'C':3, 'G':1, 'T':5, 'Unknown':0}
    

def test2():
    fileName = 'seq2.txt'
    with open(fileName, 'w') as f:
        f.write("X!!AT!!!")
    tot_count = calculate_statistics([fileName])
    assert tot_count == {'A':1, 'C':0, 'G':0, 'T':1, 'Unknown':6}

def test3():
    fileName = 'seq3.txt'
    with open(fileName, 'w') as f:
        f.write("AAAAAAA")
    tot_count = calculate_statistics([fileName])
    assert tot_count == {'A':7, 'C':0, 'G':0, 'T':0, 'Unknown':0}

def test4():
    fileName = 'seq4.txt'
    with open(fileName, 'w') as f:
        f.write("FFFFF")
    tot_count = calculate_statistics([fileName])
    assert tot_count == {'A':0, 'C':0, 'G':0, 'T':0, 'Unknown':5}






    
if __name__ == '__main__':
    try:
        test1()
        test2()
        test3()
        test4()
        
        print()
        print("All tests ran successfully.")
    except:
        print("At least one of the tests failed")
