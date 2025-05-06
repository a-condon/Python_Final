# test_python_final.py
# This file contains tests for each function in python_final.py

from python_final import read_sequence, count_kmers, count_followers, write_output

# Test count_kmers

def test_count_kmers_typical():
    # This tests count_kmers on a normal DNA sequence
    sequence = "ATGGATTTTAA"
    k = 3
    result = count_kmers(sequence, k)
    assert result["ATG"] == 1
    assert result["TTT"] == 2
    assert result["TTA"] == 1

def test_count_kmers_empty():
    # This tests count_kmers with an empty string
    sequence = ""
    k = 3
    result = count_kmers(sequence, k)
    assert result == {}

def test_count_kmers_k_too_large():
    # This tests count_kmers where k is bigger than the sequence
    sequence = "ATG"
    k = 10
    result = count_kmers(sequence, k)
    assert result == {}

# Test count_followers

def test_count_followers_typical():
    # This tests follower counts on a normal DNA sequence
    sequence = "ATGGATTTTAA"
    k = 3
    result = count_followers(sequence, k)
    assert result["TTT"]["T"] == 1
    assert result["TTT"]["A"] == 1

def test_count_followers_empty():
    # This tests follower counts with an empty string
    sequence = ""
    k = 3
    result = count_followers(sequence, k)
    assert result == {}

# Test read_sequence

def test_read_sequence_from_file():
    # This test writes a small sequence to a file and checks if read_sequence reads it properly
    test_filename = "test_sequence.fa"

    # Write a small sequence with newlines
    with open(test_filename, "w") as f:
        f.write("ATG\n")
        f.write("TGA\n")

    # Read the file using the function
    result = read_sequence(test_filename)

    # It should return the sequence with newlines removed
    assert result == "ATGTGA"

# Test write_output

def test_write_output_to_file():
    # This test writes test data to a file using write_output
    # and checks that the output text file contains expected strings

    kmer_counts = {"AAA": 2, "AAT": 1}
    follower_counts = {"AAA": {"T": 2}, "AAT": {"G": 1}}
    output_filename = "test_output.txt"

    # Write the data to the file
    write_output(kmer_counts, follower_counts, output_filename)

    # Open the output file and check for specific expected lines
    with open(output_filename, "r") as f:
        contents = f.read()
        assert "AAA: 2" in contents
        assert "AAT -> G: 1" in contents
