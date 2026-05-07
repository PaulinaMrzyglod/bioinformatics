#s31987
#07.05.2026
#Program do przetwarzania sekwencji biologicznych w formacie FASTA

import random

def get_sequence_length():

    while True:
        user_input = input("Enter a sequence length (between 1 and 100 000): ")

        if not user_input.isdigit():
            print("Invalid input")
            print("Input should be a number")
            continue

        length = int(user_input)

        if length < 1 or length > 100000:
            print("Invalid input")
            print("Input should be a number between 1 and 10000")
            continue

        return length

def generate_dna_sequence(length):
    nucleotides = ['A', 'G', 'C', 'T']
    sequence = ''

    for _ in range(length):
        sequence += random.choice(nucleotides)

    return sequence

def main():
    sequence_length = get_sequence_length()

    dna_sequence = generate_dna_sequence(sequence_length)

    print("DNA sequence: ", dna_sequence)

if __name__ == "__main__":
    main()