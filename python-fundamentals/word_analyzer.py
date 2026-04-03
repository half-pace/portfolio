user = input("Enter a sentence: ")

total_char = 0
total_word = 0
longest_word = ""
shortes_word = ""
words_start_with_vowel = 0
rev_sentence = ""

for i, word in enumerate(user.split()):
    total_char += len(word)
    total_word += 1

    if i == 0:
        longest_word = word
        shortes_word = word
    else:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len(shortes_word):
            shortes_word = word

    if word[0].lower() in "aeiou":
        words_start_with_vowel += 1
        
    rev_sentence = rev_sentence + word[::-1] + " "
        
print(f"Total characters: {total_char}")
print(f"Total words: {total_word}")
print(f"Longest word: {longest_word}")
print(f"Shortest word: {shortes_word}")
print(f"Words starting with a vowel: {words_start_with_vowel}")
for word in user.split():
    print(f"{word}: {len(word)}", end=" ")
print(f"\nReversed sentence: {rev_sentence}")
    