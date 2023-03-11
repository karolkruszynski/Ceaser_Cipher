alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text,shift):
    word = ""
    for i in text:
            letter_nr = alphabet.index(i)
            shift_letter_number = letter_nr+shift
            if shift_letter_number > 25:
                shift_letter_number -= 26
                shifted_letter = alphabet[shift_letter_number]
                word += shifted_letter
            else:
                shifted_letter = alphabet[shift_letter_number]
                word += shifted_letter
    print(word)
def decrypt(text,shift):
    word = ""
    for i in text:
            letter_nr = alphabet.index(i)
            shift_letter_number = letter_nr-shift
            shifted_letter = alphabet[shift_letter_number]
            word += shifted_letter
    print(word)
if direction == "encode":
    encrypt(text,shift)
elif direction == "decode":
    decrypt(text,shift)