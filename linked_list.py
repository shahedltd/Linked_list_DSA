class Node:
    def __init__(self, data):
        self.data = data
        self.nextvalue = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        current = self.head
        while current is not None:
            print(f"Your current value is: {current.data}")
            current = current.nextvalue

if __name__ == "__main__":
    number1 = Node(1)
    number2 = Node(2)
    number3 = Node(3)
    number4 = Node(4)
    number5 = Node(5)

    linkedlist = LinkedList()

    linkedlist.head = number1

    number1.nextvalue = number2
    number2.nextvalue = number3
    number3.nextvalue = number4
    number4.nextvalue = number5
    number5.nextvalue = None

    linkedlist.print_list()