vowels = set("aeiou")

word = input("Please enter a word to search for vowels: ")

found = vowels.intersection(set(word))

print(f"We found the vowels {sorted(found)} in your word")

