import string, random
def password(a):
    passwordCharacters = string.punctuation + string.ascii_letters + string.digits
    passwords = []
    for i in range(a):
        passwords.append(random.choice(passwordCharacters))

    print(''.join(passwords))

password(9)