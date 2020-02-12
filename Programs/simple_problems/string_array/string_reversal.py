# Python program to reverse a
# string with special characters


import re
regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')


def reverse(sample_string):
    str_len = len(sample_string)
    sample_list = list(sample_string)
    counter = str_len
    temp = list(range(str_len))
    for i in range(str_len):
        # print(i, sample_list[i])
        new_index = str_len - i - 1
        temp[new_index] = sample_list[i]
        # print(new_index)
        # print(temp)
    return temp


print(reverse("h@llo"))


# def reverse_special_char_ignore(sample_string):
