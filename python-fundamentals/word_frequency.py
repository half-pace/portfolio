import re
from collections import Counter

freq = {}
def word_freq(text):
    #freq = {}
    for word in text:
        freq[word] = freq.get(word, 0) + 1
    return freq

def top_n_words(freq, n):
    return sorted(freq.keys(), key=freq.get, reverse=True)[:n]


#input
para_input = input("Enter a paragraph: ").lower()
text = re.sub(r'[^\w\s]', '', para_input).split()
top_n = int(input("Enter the number of top words to display: "))

#word_frequency
frequency = word_freq(text)
print("Word Frequency: ", frequency)

#top_n_words
top = top_n_words(frequency, top_n)
print("Top", top_n, "Words: ", top)

#hapax_legomena
hapax = [word for word, count in frequency.items() if count == 1]
print(f"Hapax Legomena: {hapax}")

#avg_freq
avg = sum(frequency.values()) / len(frequency)
print(f"Average Frequency: {avg:.2f}")

#freq_distribution
group = {}
for keys, val in frequency.items():
    group[val] = group.get(val, []) + [keys]

print(f"Freq_distributed: {dict(sorted(group.items()))}")

#counter comparison
counter_freq = Counter(text)
print(f"Counter Frequency: {counter_freq}")





