def find_lines_containing(filename, keyword):
    matches = []
    lower_keyword = keyword.lower()

    with open(filename, "r") as file_handle:
         for index, line in enumerate(file_handle, start=1):
            if lower_keyword in line.lower():
                matches.append((index, line.rstrip("\n")))
    return matches

def main(): #main function to run the code

    test_filename = "sample-file.txt"
    test_keyword = "lorem"


    results = find_lines_containing(test_filename, test_keyword)


    # Print how many matching lines were found.
    print(f"Matches found: {len(results)}")

    # Print the first 3 matching lines (line number and text).
    print("First 3 matches:")
    for line_number, line_text in results[:3]:
        print(f"Line {line_number}: {line_text}")

main() #call the main function to run the code
