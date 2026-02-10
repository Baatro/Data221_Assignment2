# read file
with open('sample-file.txt', 'r') as file:
    original_lines = []
    cleaned_lines = []

    punctuation = ".,!?;:'\"()-[]{}-"

    # Clean 
    for line in file:
        original_line = line.rstrip("\n")
        original_lines.append(original_line)
        
        line = line.lower()

        result = ""
        for character in line:
            if character not in punctuation and not character.isspace():
                result += character

        cleaned_lines.append(result)



# Group lines by their cleaned version
groups = {}  # key = cleaned version, value = list of (line_number, original_line)
for i, cleaned_line in enumerate(cleaned_lines):
    if cleaned_line == '':
        continue
    
    if cleaned_line not in groups:
        groups[cleaned_line] = []
    
    groups[cleaned_line].append((i + 1, original_lines[i]))


# Filter
duplicate_sets = []
for cleaned_line, line_list in groups.items():
    if len(line_list) >= 2:
        duplicate_sets.append(line_list)


# Print results
print(f"Number of near-duplicate sets: {len(duplicate_sets)}")
print()

# Print the first two sets
for i, line_set in enumerate(duplicate_sets[:2]):
    print(f"Set {i + 1}:")
    for line_num, original_line in line_set:
        print(f"  Line {line_num}: {original_line}")
    print()
