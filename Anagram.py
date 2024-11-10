

from collections import defaultdict

# List of words (you can change this input as needed)
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

anagram_map = defaultdict(list)
result = []

# Iterate over each word
for word in strs:
    sorted_word = tuple(sorted(word))  # Sort the characters of the word to create a unique key
    anagram_map[sorted_word].append(word)

# Collect the grouped anagrams
for values in anagram_map.values():
    result.append(values)

# Print the result
print(result)
