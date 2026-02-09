# first chunk of code copied from question 1

# read file
with open('sample-file.txt', 'r') as file:
    text = file.read()
# Split into tokens
tokens = text.split()

# Convert to lowercase
tokens = [token.lower() for token in tokens]

# Remove punctuation from beginning and end
for i in range(len(tokens)):
    tokens[i] = tokens[i].strip('.,!?";():')

bigrams = []
# Create bigrams
for i in range(len(tokens) - 1):
    bigram = (tokens[i], tokens[i + 1])
    bigrams.append(bigram)

# Count bigrams
bigram_counts = {}
for bigram in bigrams:
    bigram_counts[bigram] = bigram_counts.get(bigram, 0) + 1

# Sort and find top 5
sorted_bigrams = []
bigram_counts_copy = bigram_counts.copy()
for i in range(5):
    if len(bigram_counts_copy) == 0:
        break
    max_bigram = None
    max_count = 0
    for bigram in bigram_counts_copy:
        if bigram_counts_copy[bigram] > max_count:
            max_count = bigram_counts_copy[bigram]
            max_bigram = bigram
    if max_bigram is not None:
        sorted_bigrams.append((max_bigram, max_count))
        del bigram_counts_copy[max_bigram]

# Print top 5
print("Top 5 most common bigrams:")
counter = 1
for bigram_tuple in sorted_bigrams:
    bigram = bigram_tuple[0]
    count = bigram_tuple[1]
    print(f"{counter}. {bigram}: {count}")
    counter = counter + 1






