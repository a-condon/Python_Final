"""
python_final.py

This script analyzes a DNA sequence from a text file and counts all k-mers (substrings of length k)
as well as the frequency of each character that follows each k-mer.

Input:
- A fixed sequence file at: /mnt/homes4celsrs/shared/439539/reads.fa
- One command-line argument: an integer k (the length of each k-mer)

Output:
- A file named "kmer_output.txt" in the current working directory containing:
  1. The frequency of each k-mer in the sequence
  2. The frequency of each character that follows each k-mer

How to run:
  python python_final.py 4
"""

import sys  # Import sys so we can use sys.argv to read input from the command line

def read_sequence(path):
    """
    Reads the DNA sequence from a file and returns it as a single concatenated string.

    Parameters:
        path (str): The path to the input FASTA file.

    Returns:
        str: A string containing the entire sequence.
    """
    sequence = ""

    # Open the input file so we can read its contents
    file = open(path, "r")

    # Go through each line in the file
    for line in file:
        # Remove any spaces or newline characters at the end and add the line to our sequence string
        sequence = sequence + line.strip()

    # Close file after done reading
    file.close()

    return sequence

def count_kmers(sequence, k):
    """
    Counts all k-mers of length k in the sequence.

    Parameters:
        sequence (str): The full DNA sequence.
        k (int): The k-mer length.

    Returns:
        dict: A dictionary with k-mers as keys and their frequency as values.
    """
    kmer_counts = {}

    # Use a while loop to go through every possible k-mer in the sequence
    i = 0
    while i < len(sequence) - k:
        # Get the substring of length k starting at position i
        kmer = sequence[i:i+k]

        # If the k-mer is already in the dictionary, increase its count
        if kmer in kmer_counts:
            kmer_counts[kmer] = kmer_counts[kmer] + 1
        else:
            # If this is the first time we've seen this k-mer, set count to 1
            kmer_counts[kmer] = 1

        # Move to the next position in the sequence
        i = i + 1

    return kmer_counts

def count_followers(sequence, k):
    """
    Counts which character follows each k-mer and how often.

    Parameters:
        sequence (str): The full DNA sequence.
        k (int): The k-mer length.

    Returns:
        dict: A nested dictionary of the form {kmer: {next_char: count}}.
    """
    follower_counts = {}

    # Reset i to 0 to go through the sequence again
    i = 0
    while i < len(sequence) - k:
        # Get the k-mer
        kmer = sequence[i:i+k]

        # Get the character that follows the k-mer (position i+k)
        next_char = sequence[i+k]

        # If we haven't seen this k-mer yet in the follower dictionary, add it
        if kmer not in follower_counts:
            follower_counts[kmer] = {}

        # If the next character already exists under this k-mer, increment it
        if next_char in follower_counts[kmer]:
            follower_counts[kmer][next_char] = follower_counts[kmer][next_char] + 1
        else:
            # Otherwise, start the count for that character at 1
            follower_counts[kmer][next_char] = 1

        # Move to the next position in the sequence
        i = i + 1

    return follower_counts

def write_output(kmer_counts, follower_counts, output_path):
    """
    Writes the k-mer and follower frequency results to an output file.

    Parameters:
        kmer_counts (dict): Dictionary of k-mer frequencies.
        follower_counts (dict): Nested dictionary of k-mer follower frequencies.
        output_path (str): Path to the output text file.
    """
    # Open the output file in write mode
    out = open(output_path, "w")

    # Write a header for the k-mer counts
    out.write("K-mer Frequencies:\n")

    # Go through each k-mer and write its count to the file
    for kmer in kmer_counts:
        # Write the k-mer followed by its count
        out.write(kmer + ": " + str(kmer_counts[kmer]) + "\n")

    # Add a blank line before the next section
    out.write("\nFollower Frequencies:\n")

    # Go through each k-mer that has follower characters
    for kmer in follower_counts:
        # Go through each follower character for this k-mer
        for char in follower_counts[kmer]:
            # Write the relationship and count to the file
            out.write(kmer + " -> " + char + ": " + str(follower_counts[kmer][char]) + "\n")

    # All done, close the file
    out.close()

def main():
    """
    Main execution function: reads input, performs k-mer analysis,
    and writes results to a file.
    """
    input_path = "/mnt/homes4celsrs/shared/439539/reads.fa"
    output_path = "kmer_output.txt"
    k = int(sys.argv[1])

    sequence = read_sequence(input_path)
    kmer_counts = count_kmers(sequence, k)
    follower_counts = count_followers(sequence, k)
    write_output(kmer_counts, follower_counts, output_path)

if __name__ == "__main__":
    main()
