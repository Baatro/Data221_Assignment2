# read file
with open('sample-file.txt', 'r') as file:
    cleaned_lines = []
    original_lines = []

    punctuation = ".,!?;:'\"()-[]{}-"

    # Clean each line
    for line in file:
        original_lines.append(line.rstrip("\n")) #got this line from w3schools
        line = line.lower()

        result = ""
        for character in line:
            if character not in punctuation and not character.isspace():
                result += character

        cleaned_lines.append(result)



groups = {}  # key = cleaned version, value = list of line indices
for line in cleaned_lines:
    if line == '':
        continue
    else:
        counter = 0
        line_number = 0
        for check in cleaned_lines:
            if line == check:
                counter += 1
        if counter >= 2:
            groups.update({line:})




print(groups)
