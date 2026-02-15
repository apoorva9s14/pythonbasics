class IterExample:
    def __init__(self,data):
        self.data = data

    def __iter__(self):
        self.data = 0
        return self

    def __next__(self):
        if self.data < 10:
            self.data += 1
            return self.data + 100
        else:
            raise StopIteration


new_obj = IterExample(10)
for each in new_obj:
    print(each)
iter_obj = iter(new_obj)

# print(next(iter_obj))
# print(next(iter_obj).data)
# print(next(iter_obj).data)
# print(next(iter_obj).data)
# print(next(iter_obj).data)
while True:
    try:
        print(next(iter_obj))
    except StopIteration:
        print("iter complete")
        break