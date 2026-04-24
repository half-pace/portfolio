text = input("Enter a paragraph: ")

def word_Count(text: str) -> int:
    """ Counts the number of words in the given text."""
    words = text.split()
    return len(words)

def unique_Word_Count(text: str) -> int:
    """ Counts the number of unique words in the given text."""
    words = text.lower().split()
    unique_words = []
    for word in words:
        if word in unique_words:
            continue
        else:
            unique_words.append(word)
    return len(unique_words)

def char_Count_Spaces(text: str) -> int:
    """Counts the number of characters in the given text, including spaces."""
    return len(text)
    

def char_Count_No_Spaces(text: str) -> int:
    """Counts the number of characters in the given text, excluding spaces."""
    words = text.split()
    count = 0
    for word in words:
        for char in word:
            count += 1
    return count
    
def most_Frequent_Word(text: str) -> str:
    """Finds the most frequent word in the text."""
    words = text.lower().split()
    seen = {}
    max_freq = 0
    most_freq_word = ""
    for word in words:
        if word in seen:
            seen[word] += 1
        else:
            seen[word] = 1
            
    for word, freq in seen.items():
        if freq > max_freq:
            max_freq = freq
            most_freq_word = word
    
    return most_freq_word

def least_Frequent_Word(text: str) -> str:
    """Finds the least frequent word in the text."""
    words = text.lower().split()
    seen = {}
    min_freq = 0
    least_freq_word = ""
    for word in words:
        if word in seen:
            seen[word] += 1
        else:
            seen[word] = 1
                  
    for word, freq in seen.items():
        if freq < min_freq or min_freq == 0:
            min_freq = freq
            least_freq_word = word
    
    return least_freq_word

def avg_Word_Len(text: str) -> float:
    """Calculates the average word length in the text."""
    words = text.split()
    total_length = sum(len(word) for word in words)
    return total_length / len(words) if words else 0

def longest_Word(text: str) -> str:
    """Finds the longest word in the text."""
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def shortest_Word(text: str) -> str:
    """Finds the shortest word in the text."""
    words = text.split()
    shortest = words[0] if words else ""
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest

def words_Appearing_More_Than_Once(text: str) -> dict:
    """Finds words that appear more than once in the text."""
    words = text.lower().split()
    seen = {}
    for word in words:
        if word in seen:
            seen[word] += 1
        else:
            seen[word] = 1
            
    return {word: freq for word, freq in seen.items() if freq > 1}

def no_Of_Sentences(text: str) -> int:
    """Counts the number of sentences in the text."""
    no_of_sentences = 0 
    inside_punc = False
    for word in text:
        if word in ['.', '!', '?']:
            if not inside_punc:
                no_of_sentences += 1
                inside_punc = True
            else:
                inside_punc = True
                continue
        else:
            inside_punc = False
            
    return no_of_sentences

def word_Letter_Replace(text: str) -> str:
    """Replaces every word longer than 5 characters with its first 3 characters followed by '...'. """
    word = text.split()
    modfied_words = []  
    for word in word:
        if len(word) > 5:
            modfied_words.append(word[:3] + '...')
        else:
            modfied_words.append(word)
            
    return ' '.join(modfied_words)

word_count = word_Count(text)
unique_word_count = unique_Word_Count(text)
character_count_with_spaces = char_Count_Spaces(text)
character_count_without_spaces = char_Count_No_Spaces(text)
most_frequent_word = most_Frequent_Word(text)
least_frequent_word = least_Frequent_Word(text)
avg_word_length = avg_Word_Len(text)
longest_word = longest_Word(text)
shortest_word = shortest_Word(text)
no_of_sentences = no_Of_Sentences(text)
words_appearing_more_than_once = words_Appearing_More_Than_Once(text)
word_letter_replace = word_Letter_Replace(text)

print(f"Word Count: {word_count}")
print(f"Unique Word Count: {unique_word_count}")
print(f"Character Count (with spaces): {character_count_with_spaces}")
print(f"Character Count (without spaces): {character_count_without_spaces}")
print(f"Most Frequent Word: {most_frequent_word}")
print(f"Least Frequent Word: {least_frequent_word}")
print(f"Average Word Length: {avg_word_length}")
print(f"Longest Word: {longest_word}")
print(f"Shortest Word: {shortest_word}")
print(f"Number of Sentences: {no_of_sentences}")
print(f"Words Appearing More Than Once: {words_appearing_more_than_once}")
print(f"Text after replacing words longer than 5 characters: {word_letter_replace}")