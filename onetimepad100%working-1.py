def one_time_pad(plaintext, key):
    # 1. Check if the key is long enough. Raise an exception with an error message if it's not
    if len(key) < len(plaintext):
        raise Exception('Key is too short. Aborting')
def binary(integer, length=8):
    return format(integer, '#0{}b'.format(length+2))

def str_to_spaces(plaintext):
    for character in plaintext:
        print(f'{character} ', end='')
        continue
        # The extra space is needed. end='' stops print() from making a new line for each character.
        # Print an empty line after the loop. What happens if we delete this part? What happens if we remove , end='' above?


def str_to_ascii(plaintext):
    for character in plaintext:
        ascii_code = ord(character)
        print(f'{ascii_code} ', end='')
def str_to_hex(plaintext):
    for character in plaintext:
        ascii_code = ord(character)
        hex_code = hex(ascii_code)
        binary1= binary(ascii_code)
        print(f'{hex_code} ', end='')
def str_to_hex1(plaintext,key):#biinary olaintext
    for character in plaintext:
        ascii_code = ord(character)
        hex_code = hex(ascii_code)
        binary1 = binary(ascii_code)
        print(f'{binary1} ', end='')

def str_to_hex2(plaintext, key):#binary-key
    for character in key:
        ascii_code = ord(character)
        hex_code = hex(ascii_code)
        binary1 = binary(ascii_code)
        print(f'{binary1} ', end='')
def str_to_hex6(plaintext, key):  # ciphertext-ascii-code
    for i in range(max(len(plaintext), len(key))):
        plaintext_ascii_code = ord(plaintext[i])
        key_ascii_code = ord(key[i])
        ciphertext_ascii_code = ord(plaintext[i % len(plaintext)]) ^ ord(key[i % len(key)])
        temporary_list3.append(chr(ciphertext_ascii_code))
        ciphertext = ''.join(temporary_list3)
    print (f'Temporary List: {temporary_list3} ', end=' ')
    #print(f'{temporary_list3} ', end=' ')
    print('')
    print ("Ciphertext:")
    for integer in (ciphertext):
        print(f'{integer } ', end=' ')
    
   
temporary_list = []
def str_to_hex3(plaintext, key):#ciphertext-ascii-code
    for i in range(max(len(plaintext), len(key))):
         plaintext_ascii_code = ord(plaintext[i])
         key_ascii_code = ord(key[i])
         ciphertext_ascii_code = ord(plaintext[i % len(plaintext)]) ^ ord(key[i % len(key)])
         temporary_list.append(hex(ciphertext_ascii_code)[2:])
         #ciphertext_ascii_code = ''.join(temporary_list)
         print(f'{ciphertext_ascii_code} ', end=' ' )
#do not touch
temporary_list1 = []
def str_to_hex4(plaintext, key):#ciphertext-ascii-code
    for i in range(max(len(plaintext), len(key))):
         plaintext_ascii_code = ord(plaintext[i])
         key_ascii_code = ord(key[i])
         ciphertext_ascii_code = ord(plaintext[i % len(plaintext)]) ^ ord(key[i % len(key)])
         temporary_list1.append(hex(ciphertext_ascii_code))
         ciphertext_hex = " ".join(temporary_list1)
    print(f'{ciphertext_hex} ', end=' ' )



temporary_list2 = []
def str_to_hex5(plaintext, key):  # ciphertext-ascii-code
    for i in range(max(len(plaintext), len(key))):
        plaintext_ascii_code = ord(plaintext[i])
        key_ascii_code = ord(key[i])
        ciphertext_ascii_code = ord(plaintext[i % len(plaintext)]) ^ ord(key[i % len(key)])
        temporary_list2.append(binary(ciphertext_ascii_code))
        ciphertext_binary= " ".join(temporary_list2)
    print(f'{ciphertext_binary } ', end=' ')
temporary_list3 = []


if __name__ == '__main__':
    print('Plaintext:')
    str_to_spaces('hello')
    print('')
    print('Plaintext ASCII Codes:')
    str_to_ascii('hello')
    print('')
    print('Plaintext Hex:')
    
    str_to_hex('hello')
    
    print('')
    print('Plaintext Binary:')
    str_to_hex1('hello','PWN3D')
    print('')
    print('Key:')
    str_to_spaces('PWN3D')
    print('')

    print('Key ASCII Codes:')
    str_to_ascii('PWN3D')
    print('')
    print('Key Hex:')
    str_to_hex('PWN3D')
    print('')
    print('Key Binary:')
    str_to_hex2('hello','PWN3D')
    print('')
    print('Performing XOR')
    print('')
    
    
    print('Ciphertext Binary:')
    str_to_hex5('hello', 'PWN3D')
    print('')
    #do not touch
    print('Ciphertext Hex:')
    str_to_hex4('hello','PWN3D')
    print('')
    print('Ciphertext ASCII Codes:')
    str_to_hex3('hello', 'PWN3D')
    print('')
    #print('Ciphertext:')
    str_to_hex6('hello', 'PWN3D')
    #print('')

    #print('Ciphertext:')
    #str_to_hex5('hello','PWN3D')
    #one_time_pad(hello, PWN3D)



