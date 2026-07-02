try:
    with open('doesnotexistfile.txt') as f:
        print(f.read())
except FileNotFoundError:
    print('This file does not exist')