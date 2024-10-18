###
# Encrypts text using Caesar Code, shifting each letter
# in the alphabet right one position
#
plain_text = 'The early bird catches the worm'
encrypted_text = ''


for char in plain_text:
    if char.isalpha():
        new_char_code =ord(char) + 1
        if char.islower() and new_char_code > ord('z'):
            new_char_code = ord('a')
        elif char.isupper() and new_char_code > ord('Z'):
            new_char_code = ord('A')
        encrypted_text += chr(new_char_code)
    else: 
        encrypted_text+= char


    # read the character's code (use ord())
    ...
    # add one to the character's code
    ...
    # replace new character code with its
    # corresponding character (use chr())
    ...
    # add encrypted character to encrypted text
    ...

print(f'plain_text :',{plain_text})
print(f'encrypted_text: ',{encrypted_text})
