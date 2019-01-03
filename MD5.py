import hashlib


def main():
    msg = input("Enter message: ")
    hash = hashlib.md5()
    hash.update(msg.encode('utf-8'))

    print("MD5 Hash: {}".format(hash.hexdigest()))


if __name__ == "__main__":
    main()
