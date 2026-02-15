# Context management
#     Instead of using try-except-finally
#     Two ways of implementing:
#     1. Class based - __enter__, __exit__
#     when used the instance of the class along with "with"
#     __enter__ and __exit__ would be called
#     2. Function based
#     contextlib.contextmanager can be used as a decorator
#     The function should have a single yield
#     the statements before yield are __enter__
#     the statements after yield are __exit__


class Indenter:
    def __init__(self):
        print("In init")
        self.level = 0

    def __enter__ (self):
        print("In Enter level before is:",self.level,",level after is:",self.level +1)
        self.level += 1
        return self

    def __exit__ (self, exc_type, exc_val, exc_tb):
        print("In Exit level before is:", self.level, ",level after is:", self.level + 1)
        self.level -= 1

    def print (self, text):
        print(' ' * self.level + text)


with Indenter() as indent:
    indent.print('hi!')
    with indent:
        indent.print('hello')
        with indent:
            indent.print('bonjour')
    indent.print('hey')


from contextlib import contextmanager

@contextmanager
def open_file(path, mode):
    the_file = open(path, mode)
    yield the_file
    the_file.close()

files = []

for x in range(100000):
    with open_file('foo.txt', 'w') as infile:
        files.append(infile)

for f in files:
    if not f.closed:
        print('not closed')
