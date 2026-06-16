def encrypt(text, shift):
    shift = shift % 26
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


def main():
    print("Caesar Cipher Program")

    while True:
        print("\n1. Encrypt")
        print("2. Decrypt")
        print("3. Quit")
        choice = input("What do you want to do? ")

        if choice == "1" or choice == "2":
            msg = input("Type your message: ")
            valid = False
            while not valid:
                shift_val = input("Shift value: ")
                if shift_val.lstrip("-").isdigit():
                    shift_val = int(shift_val)
                    valid = True
                else:
                    print("that's not a number, try again")

            if choice == "1":
                print("Result:", encrypt(msg, shift_val))
            else:
                print("Result:", decrypt(msg, shift_val))

        elif choice == "3":
            print("bye!")
            break

        else:
            print("not a valid option")


main()