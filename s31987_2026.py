#s31987
#07.05.2026
#Program do przetwarzania sekwencji biologicznych w formacie FASTA

import random

#function to find motif
def find_motif(sequence: str, motif: str) -> list:
    positions = []

    if motif == "":
        return positions

    motif = motif.upper()

    for i in range(0, len(sequence) - len(motif) + 1):
        if sequence[i:i + len(motif)] == motif:
            positions.append(i + 1)

    return positions

#function to display motif
def print_motif_positions(positions: list, motif: str) -> None:
    if motif == "":
        print("Motif is empty")
    elif positions:
        print(f"Motif {motif} was found at positions {positions}")
    else:
        print(f"Motif {motif} was not found")

#complementary sequence
def complementary_sequence(sequence: str) -> str:

    complementary_map = {
        "A": "T",
        "T": "A",
        "G": "C",
        "C": "G",
    }

    comp_sequence = ""

    for nucleotide in sequence:
        comp_sequence += complementary_map[nucleotide]

    return comp_sequence

#reverse complementary sequence
def reverse_complementary_sequence(sequence: str) -> str:
    comp_sequence = complementary_sequence(sequence)
    reverse_comp_sequence = comp_sequence[::-1]
    return reverse_comp_sequence

def transcribe_dna(sequence: str) -> str:
    return sequence.replace("T", "U")

#add records to existing FASTA file
def append_to_fasta(sequence_id: str, fasta_record: str) -> None:
    filename = f"{sequence_id}.fasta"

    with open(filename, "a") as fasta_file:
        fasta_file.write("\n")
        fasta_file.write(fasta_record)

#counting gc_content in sliding_window
# Returns a list of tuples:
# (start_position, gc_content)
def sliding_window(sequence: str, window_size: int) -> list:
    results = []
    for i in range(0, len(sequence) - window_size + 1):
        window = sequence[i:i + window_size]
        gc_count = window.count("G") + window.count("C")
        gc_content = (gc_count / window_size) * 100

        results.append((i+1, gc_content))
    return results

#saving sliding_window result to cvs file
def save_gc_to_csv(sequence_id: str, gc_result: list) -> None:
    filename = f"{sequence_id}_gc_content.csv"

    with open(filename, "w") as csv_file:
        csv_file.write("start_position,gc_content\n")

        for position, gc_content in gc_result:
            csv_file.write(f"{position},{gc_content:.2f}\n")

    print(f"GC content saved to {filename}")

def validate_positive_int(prompt: str, min_val: int = 1, max_val: int = 100000) -> int:
    while True:
        user_input = input(prompt)

        try:
            value = int(user_input)
        except ValueError:
            print("Invalid input")
            print("Input should be a number")
            continue

        if value < min_val or value > max_val:
            print("Invalid input")
            print(f"Input should be a number between {min_val} and {max_val}")
            continue

        return value


def format_fasta(sequence_id: str,description: str, sequence: str, line_length: int=80) -> str:
    if description:
        fasta_record = f">{sequence_id} {description}\n"
    else:
        fasta_record = f">{sequence_id}\n"

    for i in range(0, len(sequence), line_length):
        fasta_record += sequence[i:i+line_length] + "\n"

    return fasta_record

def save_to_fasta(sequence_id: str, fasta_record: str) -> None:
    filename = f"{sequence_id}.fasta"

    with open(filename, "w") as fasta_file:
        fasta_file.write(fasta_record)

    print(f"Wrote to {filename}")

def get_sequence_id() -> str:
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

def get_description() -> str:
    return input("Enter the description(optional): ")

"""
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
"""


def generate_sequence(length: int) -> str:
    nucleotides = ['A', 'G', 'C', 'T']
    sequence = ''

    for _ in range(length):
        sequence += random.choice(nucleotides)

    return sequence

def calculate_statistics(sequence: str) -> dict:
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

def print_statistics(stats: dict) -> None:
    print("\nSequence statistics:")
    print(f"A: {stats['A']:.2f}%")
    print(f"G: {stats['G']:.2f}%")
    print(f"C: {stats['C']:.2f}%")
    print(f"T: {stats['T']:.2f}%")
    print(f"GC-content: {stats['GC']:.2f}%")

def get_name():
    return input("Enter your name: ").strip().lower()

def insert_name(sequence: str, name: str) -> str:
    if name == "":
        return sequence

    insert_position = random.randint(0, len(sequence))

    modified_sequence = (sequence[:insert_position] + name + sequence[insert_position:])
    return modified_sequence

def main():
    sequence_length = validate_positive_int("Enter a sequence length(between 1 and 100 000): ")
    sequence_id = get_sequence_id()
    description = get_description()
    name = get_name()

    #generate biological sequence
    dna_sequence = generate_sequence(sequence_length)

    #insert name
    visual_sequence = insert_name(dna_sequence, name)

    fasta_record = format_fasta(sequence_id, description, visual_sequence)
    save_to_fasta(sequence_id, fasta_record)

    #Calculate statistics only for biological sequence
    statistics = calculate_statistics(dna_sequence)
    print_statistics(statistics)

    #finding motif
    motif = input("Enter the motif sequence: ").strip().upper()
    motif_positions = find_motif(dna_sequence, motif)
    print_motif_positions(motif_positions, motif)

    #complemenatry sequence
    comp_sequence = complementary_sequence(dna_sequence)
    comp_record = format_fasta(sequence_id + "_complement", "complementary strand", comp_sequence)
    append_to_fasta(sequence_id, comp_record)

    #reverse complementary sequence
    reverse_comp_sequence = reverse_complementary_sequence(dna_sequence)
    reverse_comp_record = format_fasta(sequence_id + "_reverse", "reverse complementary strand", reverse_comp_sequence)
    append_to_fasta(sequence_id, reverse_comp_record)

    #transcibe dna
    mrna = transcribe_dna(dna_sequence)
    mrna_record = format_fasta(sequence_id + "_mrna", "transcribed mRNA strand", mrna)
    append_to_fasta(sequence_id, mrna_record)

    #window sliding
    windowe_size = validate_positive_int("Enter sliding window size: ", min_val=1, max_val=sequence_length)
    gc_result = sliding_window(dna_sequence, windowe_size)
    save_gc_to_csv(sequence_id, gc_result)

if __name__ == "__main__":
    main()