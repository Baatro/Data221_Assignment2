# first chunk of code copied from question 1

# read file
with open('sample-file.txt', 'r') as file:
    text = file.read()
# Split into tokens
tokens_unfiltered = text.split()

# Convert to lowercase
tokens_unfiltered = [token.lower() for token in tokens_unfiltered]

# Remove punctuation from beginning and end
for i in range(len(tokens_unfiltered)):
    tokens_unfiltered[i] = tokens_unfiltered[i].strip('.,!?";():')
# check for 2 letters or more
clean_tokens = []
for word in tokens_unfiltered:
    if len(word) >= 2:
        clean_tokens.append(word)

tokens = clean_tokens
