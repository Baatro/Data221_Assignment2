import re
from collections import Counter

# Read the file
with open('sample-file.txt', 'r') as file:
    text = file.read()

# Split into tokens (words)
tokens = text.split()

# Convert to lowercase
tokens = [token.lower() for token in tokens]

# Remove punctuation from beginning and end
tokens = [re.sub(r'^[^\w]+|[^\w]+$', '', token) for token in tokens]

# Keep only tokens with at least 2 alphabetic characters
tokens = [token for token in tokens if sum(1 for c in token if c.isalpha()) >= 2]

# Count word frequencies
word_counts = Counter(tokens)

# Get 10 most frequent words
top_10 = word_counts.most_common(10)

# Print results
for word, count in top_10:
    print(f"{word} -> {count}")