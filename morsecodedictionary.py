morse_code_dict = {
    'A': '.-', 'B': '-...',
    'C': '-.-.', 'D': '-..',
    'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....',
    'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-',
    'U': '..-', 'V': '...-',
    'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---',
    '3': '...--', '4': '....-',
    '5': '.....', '6': '-....',
    '7': '--...', '8': '---..',
    '9': '----.', '0': '-----',
    ' ': '/'
}
def encrypt(text):
    """Encrypts a given English phrase into Morse code."""
    encrypted_text = ''
    for char in text.upper():
        if char in morse_code_dict:
            encrypted_text += morse_code_dict[char] + ' '
        else:
            encrypted_text += ' '

    return encrypted_text.strip()

def decrypt(morse_code):
    """Decrypts Morse code into an English phrase."""
    morse_code_words = morse_code.split(' ')
    decrypted_text = ''
    for word in morse_code_words:
        for key, value in morse_code_dict.items():
            if value == word:
                decrypted_text += key
                break
        else:
            decrypted_text += ' '

    return decrypted_text
