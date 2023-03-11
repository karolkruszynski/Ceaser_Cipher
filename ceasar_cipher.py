alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceasar(text,shift,direction):
    word = ""
    if direction == "decode":
        shift *= -1
    for i in text:
        if i in alphabet:
            letter_nr = alphabet.index(i)
            shift_letter_number = letter_nr + shift
            if shift_letter_number > 25:
                shift_letter_number -= 26
                shifted_letter = alphabet[shift_letter_number]
                word += shifted_letter
            else:
                shifted_letter = alphabet[shift_letter_number]
                word += shifted_letter
        else:
            word += i
    print(f"The {direction}d text is {word}")
from art import logo
print(logo)
should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    ceasar(text,shift,direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
