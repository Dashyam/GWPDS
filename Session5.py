"""
    Whatever, we write in main file , is executed by main thread

"""


def main():
    a = 10
    b = 2 * a
    print("b is :", b)


print("name", __name__)  # __name__ is also known as dunder
if __name__ == "__main__":
    main()
