import hashlib

# ------------------ hashlib


def print_hashalgo():
    print(sorted(hashlib.algorithms_guaranteed))
    print(sorted(hashlib.algorithms_available))


def hash_sample():
    mprogram = """for i in range(10):
    print(i)
    """

    # for code in mprogram.encode("utf8"):
    #     print(code, chr(code))

    print(mprogram)
    # encode does not work with string, so converting string to unicode
    original_hash = hashlib.sha256(mprogram.encode("utf8"))

    # hexadecimal representation of the secure hash
    print(f"SHA256: {original_hash.hexdigest()}")

    # ----- Simulate hash modified
    mprogram += "print('code change')"
    print(mprogram)
    new_hash = hashlib.sha256(mprogram.encode("utf8"))
    print(f"SHA256: {new_hash.hexdigest()}")

    if new_hash.hexdigest() == original_hash.hexdigest():
        print("The code has not been changed")
    else:
        print("The code has been modified")


# ------------------ Tests

hash_sample()
