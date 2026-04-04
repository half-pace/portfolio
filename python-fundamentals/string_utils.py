def count_vowels(s: str) -> int:
    """Counts the number of vowels in a given string."""
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

def reverse_words(s: str) -> str:
    """Reverses the order of words not letters"""
    words = s.split()
    return ' '.join(reversed(words))

def capitalize_words(s: str) -> str:
    """Capitalizes the first letter of each word in the string."""
    return ' '.join(word.capitalize() for word in s.split())

def is_anagram(s1: str, s2: str) -> bool:
    """Checks if two strings are anagrams of each other."""
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())

def longest_common_prefix(strs: list) -> str:
    """Finds the longest common prefix string amongst an array of strings."""
    if not strs:
        return ""
    
    prefix = strs[0]
    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix

def main():
    print(count_vowels("Hello World"))  # Output: 3
    print(reverse_words("Hello World"))  # Output: "World Hello"
    print(capitalize_words("hello world"))  # Output: "Hello World"
    print(is_anagram("listen", "silent"))  # Output: True
    print(longest_common_prefix(["flower", "flow", "flight"]))  # Output: "fl"
    
if __name__ == "__main__":    main()