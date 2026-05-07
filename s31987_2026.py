#s31987
#07.05.2026
#Program do przetwarzania sekwencji biologicznych w formacie FASTA

import random

def format_fasta_sequence(sequence, line_length=80):
    formatted_sequence = ""

    for i in range(0, len(sequence), line_length):
        formatted_sequence += sequence[i:i+line_length] + "\n"

    return formatted_sequence

def save_to_fasta(sequence_id, description, sequence):
    filename = f"{sequence_id}.fasta"

    with open(filename, "w") as fasta_file:
        if description:
            fasta_file.write(f">{sequence_id} {description}\n")
        else:
            fasta_file.write(f">{sequence_id}\n")

        fasta_file.write(format_fasta_sequence(sequence))

    print(f"Wrote to {filename}")

def get_sequence_id():
    while True:
        sequence_id = input("Enter the sequence id: ")

        if sequence_id == "":
            print("Invalid input")
            print("Id cannot be empty")
            continue

        if any(char.isspace() for char in sequence_id):
            print("Invalid input")
            print("Id cannot contain whitespace")
            continue

        return sequence_id

def get_description():
    return input("Enter the description(optional): ")

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
    sequence_id = get_sequence_id()
    description = get_description()

    dna_sequence = generate_dna_sequence(sequence_length)
    save_to_fasta(sequence_id, description, dna_sequence)

#    print("DNA sequence: ", dna_sequence)

if __name__ == "__main__":
    main()