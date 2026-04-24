def caesar_shift_char(ch, shift):
    if ch.isalpha():
        base = ord('A') if ch.isupper() else ord('a')
        return chr((ord(ch) - base + shift) % 26 + base)
    return ch


def caesar_encode(text, shift):
    return "".join(caesar_shift_char(c, shift) for c in text)


def caesar_decode(text, shift):
    return caesar_encode(text, -shift)


# ---------------------------
# 🔹 VIGENERE CIPHER
# ---------------------------

def clean_key(key):
    if not key.isalpha():
        return None
    return key.lower()


def vigenere_shift(text, key, decode=False):
    result = []
    key = clean_key(key)

    if key is None:
        return None

    key_len = len(key)
    j = 0

    for ch in text:
        if ch.isalpha():
            shift = ord(key[j % key_len]) - ord('a')
            if decode:
                shift = -shift

            base = ord('A') if ch.isupper() else ord('a')
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            j += 1
        else:
            result.append(ch)

    return "".join(result)


def vigenere_encode(text, key):
    return vigenere_shift(text, key, decode=False)


def vigenere_decode(text, key):
    return vigenere_shift(text, key, decode=True)

def rot13(text):
    return caesar_encode(text, 13)



#cli

def main():
    while True:
        print("Choose a cipher:")
        print("1. Caesar Cipher")
        print("2. Vigenère Cipher")
        print("3. ROT13 Cipher")
        print("4. Exit")
        cipher_choice = input("Enter the number of the cipher you want to use: ")
        
        if cipher_choice == "4":
            print("Exiting!")
            break
        
        text = input("Enter text to encode or decode: ")
        
        if cipher_choice == "1":
            mode = input("Encode or Decode (e/d): ").lower()
            
            try:
                shift = int(input("Enter shift value: "))
            except ValueError:
                print("Invalid Shift Value")
                continue
            
            if mode == "e":
                print(f"Resut: {caesar_encode(text, shift)}")
            else:
                print(f"Result: {caesar_decode(text, shift)}")
        
        elif cipher_choice == "2":
            mode = input("Encode or Decode(e/d): ").lower()
            key = input("Enter keyword: ")
            
            result = vigenere_encode(text, key) if mode == "e" else vigenere_decode(text, key)
            
            if result is None:
                print("Invalid key! Only letters allowed")
            else:
                print(f"Result: {result}")
        
        elif cipher_choice == "3":
            print("Result: ", rot13(text))
            
        else: print("Invalid choice!")
        
if __name__ == "__main__":
    main()

