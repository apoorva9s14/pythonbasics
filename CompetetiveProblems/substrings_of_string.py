"given a string find substrings"
"""
"zab"
"z", "a", "b"
"""

def findSubstrings(inp_string):
    string_len = len(inp_string)
    out_strings = []
    for i in range(string_len):
        for j in range(string_len):
            if i < j+1:
                out_strings.append(inp_string[i:j+1])
    return out_strings

print(findSubstrings("zabc"))
