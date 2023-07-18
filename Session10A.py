from Session10 import Stack, ScreenInterface


def main():
    interface1 = ScreenInterface(title="App Homepage")
    interface2 = ScreenInterface(title="Product1")
    interface3 = ScreenInterface(title="Product2")

    stack = Stack()
    stack.push(interface1)
    stack.push(interface2)
    stack.push(interface3)
    stack.push(ScreenInterface(title="Product2 info"))

    stack.pop()
    stack.pop()
    stack.pop()

    stack.push(ScreenInterface(title="App Settings"))
    stack.push(ScreenInterface(title="Account Settings"))
    stack.push(ScreenInterface(title="Change Password"))

    stack.iterate()


if __name__ == "__main__":
    main()
