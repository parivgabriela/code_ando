def caesar_cipher(text:str, key:int):
    """This use the key and sum it to each letter of the text the result is returned
        -The alphabet take note of Spanish and English
         a-zA-Z include ñ(241) Ñ(209)
         between 65-90/97-122 
    Args:
        text (str): text to encrypt
        key (int): number of position to move the letters
    """
    list_words = text.split()
    list_word_encripted = []
    for word in list_words:
        temp_word = []
        for letter in word:
            ascii_letter = letter_to_ascii(letter, key)
            temp_word.append(ascii_letter)
        list_word_encripted.append(''.join(temp_word))

    text_encripted = ' '.join(list_word_encripted)
    return text_encripted

def letter_to_ascii(letter, key):
    letter_enie_min = 241
    letter_enie_caps = 209
    letter_to_ascii = ord(letter)
    new_letter = letter_to_ascii + key
    if (new_letter >= 65 and new_letter <= 90) or (new_letter >=97 and new_letter <= 120):
        ascii_letter = new_letter
    elif letter_to_ascii == letter_enie_min:
        ascii_letter = 110 + key
    elif letter_to_ascii == letter_enie_caps:
        ascii_letter = 78 + key
    else:
        ascii_letter = letter_to_ascii
    return chr(ascii_letter)
text = "Hasta mañana"

print(caesar_cipher(text,3))