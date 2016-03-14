class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


# Write a function revstring(mystr) that uses a stack to reverse the
# characters in a string.

def revstring(mystr):
    s = Stack()
    for el in range(len(mystr)):
        s.push(mystr[el])
    res = ""
    while not s.isEmpty():
        res = res + s.pop()
    return res


print revstring("abraca")
