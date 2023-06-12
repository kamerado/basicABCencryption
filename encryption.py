#!/usr/bin/env python3

alphabet1 = 'abcdefghijklmnopqrstuvwxyz'
alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
my_file = ''
encrypt = ''
de = ''

def encrypts(a, b, n):
    global encrypt
    encrypted_file = open(n, 'w')
    for i in a:
        if i == ' ':
            encrypt += ' '
        else:
            if i in alphabet1:
                position = alphabet1.find(i)
                new_position = (position + b) % 26
                encrypt += (alphabet1[new_position])
            elif i in alphabet2:
                position = alphabet2.find(i)
                new_position = (position + b) % 26
                encrypt += (alphabet2[new_position])
    print('New encrypted file', n, 'has been created\n\n')
    encrypted_file.write(encrypt)
    encrypted_file.close()

def decrypt(c, d, n):
    global de
    decrypt_file = open(n, 'w')
    for i in c:
        if i == ' ':
            de += ' '
        else:
            if i in alphabet1:
                position = alphabet1.find(i)
                new_position = (position - d) % 26
                de += (alphabet1[new_position])
            elif i in alphabet2:
                position = alphabet2.find(i)
                new_position = (position - d) % 26
                de += (alphabet2[new_position])
    print('New decrypted file', n, 'has been created\n\n')
    decrypt_file.write(de)
    decrypt_file.close()

while True:
    print('Be sure to open this program in the directory of the file you are working with '
          '\notherwise include correct path of file\n')
    INPUT = input('Type "E" to encrypt a file \n'
                  'Type "D" to decrypt a file \n'
                  'Type "X" to exit\n'
                  'Input: ')
    if INPUT.lower() == 'e':
        try:
            file_name = input('\ninput file name to encrypt(include path): ')
            my_key = input('input a number to use as key: ')
            new_file = input('Enter a new file name: ')
            my_key = int(my_key)
            my_file = open(file_name, 'r')
            content = my_file.readlines()
            content = str(content)
            print(content)
            content = content[2:-2]
            encrypts(content, my_key, new_file)
        except Exception as err:
            print('\n', err)

    elif INPUT.lower() == 'd':
        try:
            file_name = input('\ninput file name to decrypt(include path)')
            key = input('input a number for key: ')
            new_file = input('Enter a new file name: ')
            key = int(key)
            file = open(file_name, 'r')
            content = file.readlines()
            content = str(content)
            content = content[2:-2]
            decrypt(content, key, new_file)
        except Exception as err:
            print('\n', err)
    elif INPUT.lower() == 'x':
        break
    elif INPUT == '69':
        print('nice...')

    else:
        print('\nNot a valid input.')
        pass
