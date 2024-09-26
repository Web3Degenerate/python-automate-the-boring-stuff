alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

def encrypt(original_text, shift_amount):
    #To accumulate shifted letters
    cipher_text = ""
    for letter in original_text:
        #Determine shifted position
        shifted_position = alphabet.index(letter) + shift_amount #7 (shift 2) = 9

        # Use modulo to cover the case where the shifted letter goes past 26
        # shifted_position = shifted_position % len(alphabet)
        shifted_position %= len(alphabet) #always 0-25

        #get new letter
        cipher_text += alphabet[shifted_position]

    print(f"Encoded Result: {cipher_text}")

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(original_text=text, shift_amount=shift)

# fruits = ['Apple', 'Pear', 'Banana']
# fruits.index("Banana") #returns 2
