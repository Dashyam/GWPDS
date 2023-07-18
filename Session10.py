# Stack

class ScreenInterface:

    def __init__(self, title=""):
        self.title = title
        self.next = None
        self.previous = None

    def show(self):
        print(f">> {self.title}")


class Stack:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def iterate(self):
        if self.size != 0:
            temp = self.tail
            while True:
                temp.show()
                temp = temp.previous

                if temp is None:
                    break
        else:
            print("Stack is empty :)")
    def push(self, interface):

        self.size += 1

        if self.head is None:
            self.head = interface
            self.tail = interface
        else:
            self.tail.next = interface
            interface.previous = self.tail

            # Any newly interface will be added :)
            self.tail = interface

    def pop(self):
        if self.size != 0:
            self.size -= 1
            temp = self.tail.previous
            self.tail = temp
        else:
            print("Stack is empty :)")
