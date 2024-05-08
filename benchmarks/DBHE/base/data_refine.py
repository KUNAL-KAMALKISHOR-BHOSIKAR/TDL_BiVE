def remove_duplicate_nodes(input_file, output_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()

    cleaned_lines = []
    for line in lines:
        node1, node2, _ = line.strip().split()
        if node1 != node2:
            cleaned_lines.append(f"{node1} {node2} 1\n")

    with open(output_file, 'w') as file:
        file.writelines(cleaned_lines)

if __name__ == "__main__":
    input_file = "data.txt"
    output_file = "dataset_with_1.txt"
    remove_duplicate_nodes(input_file, output_file)
    print(f"Cleaned dataset saved to {output_file}")