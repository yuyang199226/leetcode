class Foo(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, v):
        self.stack1.append(v)

    def pop(self):
        if self.stack2:
            return self.stack2.pop()
        else:
            if len(self.stack1) == 0:
                return None
            else:
                for i in range(len(self.stack1)):
                    self.stack2.append(self.stack1.pop())
                return self.stack2.pop()
