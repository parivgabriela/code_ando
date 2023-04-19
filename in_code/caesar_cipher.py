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
            new_letter = letter_moved(letter, key)
            temp_word.append(new_letter)
        list_word_encripted.append(''.join(temp_word))

    text_encripted = ' '.join(list_word_encripted)
    return text_encripted


def caesar_decryptor(text:str, key:int):
    """This use the key and decrypt the message with the key given
        -The alphabet take note of Spanish and English
         a-zA-Z include ñ(241) Ñ(209)
         between 65-90/97-122 
    Args:
        text (str): text to decrypt
        key (int): number of position to move the letters
    """
    list_words = text.split()
    list_word_encripted = []
    for word in list_words:
        temp_word = []
        for letter in word:
            # minus the number of key means it revert the positions
            key_decrypt = -key 
            new_letter = letter_moved(letter, key_decrypt)
            temp_word.append(new_letter)
        list_word_encripted.append(''.join(temp_word))

    text_encripted = ' '.join(list_word_encripted)
    return text_encripted

def letter_moved(letter, key):
    """ Return a new letter after moved key positions

    Args:
        letter (char): letter to be moved
        key (): n position to moved the letter

    Returns:
        ascii_letter: new letter moved n(key) positions
    """
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
text_encrypted = caesar_cipher(text,3)

print(text_encrypted)

print(f"decrypte message {caesar_decryptor(text_encrypted, 3)}")