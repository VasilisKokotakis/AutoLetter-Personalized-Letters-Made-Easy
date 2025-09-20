PLACEHOLDER = "[name]"

# Paths
names_file_path  = "Input/Names/invited_names.txt"
letter_file_path = "Input/Letters/starting_letter.txt"
output_dir       = "Output/ReadyToSend"

# Read all names from the file and strip whitespace
with open(names_file_path, mode="r") as names_file:
    names_list = [name.strip() for name in names_file.readlines()]

# Read the letter template once
with open(letter_file_path) as letter_file:
    letter_content = letter_file.read()

# Create personalized letters for each name
for name in names_list:
    new_letter = letter_content.replace(PLACEHOLDER, name)

    output_path = f"{output_dir}/letter_for_{name}.txt"
    with open(output_path, mode="w") as completed_letter:
        completed_letter.write(new_letter)
