morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..',
    'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----',
    '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ',': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-'
}
# {
#     'а': ".-", 'б': "-...", 'в': ".--", 'г': "--.", 'д': "-..", 'е': ".", 'ё': ".", 'ж': "...-", 'з': "--..",
#     'и': "..", 'й': ".---", 'к': "-.-", 'л': ".-..", 'м': "--", 'н': "-.", 'о': '---', 'п': ".--.", 'р': ".-.",
#     'с': "...", 'т': "-", 'у': "..-", 'ф': "..-.", 'х': "....", 'ц': "-.-.", 'ч': "---.", 'ш': "----", 'щ': "--.-",
#     'ъ': "--.--", 'ы': "-.--", 'ь': "-..-", 'э': "..-..", 'ю': "..-.", 'я': ".-.-"
# }


def encrypt_morse_code(text):
    encrypted_text = ''
    for char in text.upper():
        if char != ' ' and char in morse_code_dict:
            encrypted_text += morse_code_dict[char] + ' '
        else:
            encrypted_text += ' '
    return encrypted_text


def decrypt_morse_code(text):
    decrypted_text = ''
    reversed_morse_dict = {v: k for k, v in morse_code_dict.items()}
    for code in text.split():
        if code in reversed_morse_dict:
            decrypted_text += reversed_morse_dict[code]
        elif code == '':
            decrypted_text += ' '
    return decrypted_text


original_text = "HELLO WORLD"
encrypted_text = encrypt_morse_code(original_text)
decrypted_text = decrypt_morse_code(encrypted_text)

print(f'Оригинальный текст: {original_text}')
print(f'Зашифрованный текст: {encrypted_text}')
print(f'Расшифрованный текст: {decrypted_text}')
