import hashlib


def main():
    msg = input("Enter message: ")
    hsh = hashlib.sha256()

    hsh.update(msg.encode('utf-8'))
    print("SHA 256 Hash: {}".format(hsh.hexdigest()))


if __name__ == "__main__":
    main()
