
def main():
    min_length = 4
    password = str(input("Password: "))
    while len(password) < min_length:
        print("Password must be shorter than 4 characters")
        password = str(input("Password: "))

    print(len(password) * '*')


main()

