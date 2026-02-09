with open('sample-file.txt', 'r') as file:
    text = file.read()
# Split into tokens
tokens = text.split()
tokens_unfiltered = text.split()

# Convert to lowercase
tokens = [token.lower() for token in tokens]
tokens_unfiltered = [token.lower() for token in tokens_unfiltered]

# Remove punctuation from beginning and end
for i in range(len(tokens)):
    tokens[i] = tokens[i].strip('.,!?";():')
for i in range(len(tokens_unfiltered)):
    tokens_unfiltered[i] = tokens_unfiltered[i].strip('.,!?";():')
# check for 2 letters or more
clean_tokens = []
for word in tokens_unfiltered:
    if len(word) >= 2:
        clean_tokens.append(word)

tokens = clean_tokens
    

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
