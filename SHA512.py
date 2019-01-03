import hashlib


def main():
    msg = input("Enter message: ")
    hsh = hashlib.sha512()

    hsh.update(msg.encode('utf-8'))

    print("SHA 512 Hash: {}".format(hsh.hexdigest()))


if __name__ == "__main__":
    main()
