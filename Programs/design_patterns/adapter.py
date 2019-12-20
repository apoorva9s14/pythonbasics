"""
Adapter design pattern
"""

# -----------------------------------------------------------------------
# If interface name used by the client is missing in a Class
# redefine it in the class with the same interface name as used by the Client


class StringAdapter(str):
    def __init__(self, str_val):
        self.str_val = str_val

    def pop(self, ind):
        if ind == -1:
            return  self.str_val[:ind]
        return self.str_val[:ind] + self.str_val[ind+1:]


adapter_string = StringAdapter("Remove")
print(adapter_string.pop(-1))
