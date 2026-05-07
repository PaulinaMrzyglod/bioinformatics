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

def calculate_statistics(sequence):
    length = len(sequence)

    count_a = sequence.count('A')
    count_g = sequence.count('G')
    count_c = sequence.count('C')
    count_t = sequence.count('T')

    stats = {
        "A": count_a / length * 100,
        "G": count_g / length * 100,
        "C": count_c / length * 100,
        "T": count_t / length * 100,
        "GC": (count_g + count_c) / length * 100,
    }

    return stats

def print_statistics(stats):
    print("\nSequence statistics:")
    print(f"A: {stats['A']:.2f}%")
    print(f"G: {stats['G']:.2f}%")
    print(f"C: {stats['C']:.2f}%")
    print(f"T: {stats['T']:.2f}%")
    print(f"GC-content: {stats['GC']:.2f}%")

def get_name():
    return input("Enter your name: ").strip().lower()

def insert_name_into_sequence(sequence, name):
    if name == "":
        return sequence

    insert_position = random.randint(0, len(sequence))

    modified_sequence = (sequence[:insert_position] + name + sequence[insert_position:])
    return modified_sequence

def main():
    sequence_length = get_sequence_length()
    sequence_id = get_sequence_id()
    description = get_description()
    name = get_name()

    #generate biological sequence
    dna_sequence = generate_dna_sequence(sequence_length)

    #insert name
    visual_sequence = insert_name_into_sequence(dna_sequence, name)
    save_to_fasta(sequence_id, description, visual_sequence)

    statistics = calculate_statistics(dna_sequence)
    print_statistics(statistics)

#    print("DNA sequence: ", dna_sequence)

if __name__ == "__main__":
    main()