class MelRange:
    def __init__(self, *args):
        self.start = 0
        self.step = 1

        match len(args):
            case 1:
                self.stop = args[0]

            case 2:
                self.start, self.stop = args

            case 3:
                self.start, self.stop, self.step = args

            case _:
                raise SyntaxError

    def __iter__(self):
        val = self.start
        while val < self.stop:
            yield val
            val += self.step


for i in MelRange(10):
    print(i)


a = range(1)
b = range(2)

print(a == b)

