# read file
with open('sample-file.txt', 'r') as file:
    raw_text = file.read()

# split into tokens
raw_tokens = raw_text.split()

# convert to lowercase
lower_tokens = [token.lower() for token in raw_tokens]

# remove punctuation from beginning and end
for i in range(len(lower_tokens)):
    lower_tokens[i] = lower_tokens[i].strip('.,!?";():')

# remove words with fewer than 2 letters
filtered_tokens = []
for word in lower_tokens:
    if len(word) >= 2:
        filtered_tokens.append(word)

tokens = filtered_tokens

# count frequencies without imports
token_counts = {}

for word in tokens:
    if word in token_counts:
        token_counts[word] += 1
    else:
        token_counts[word] = 1

# sort by frequency (highest first)
sorted_token_counts = sorted(token_counts.items(), key=lambda x: x[1], reverse=True)

# print top 10
for word, count in sorted_token_counts[:10]:
    print(word, count)
