


def maxsubarrayproduct(arr):
    max_product = 1
    negative_counter = 0
    for each in arr:
        if each <0:
            negative_counter+=1
            if negative_counter%2!=0:
                negative_value = each
                max_product = max(max_product, abs(max_product*each))
            else:
                max_product = max(max_product, max_product*each*-1)
            print("Iteration:,",each, "Max product:", max_product)
        else:
            if negative_counter%2!=0:
                max_product = max(max_product*-1, (max_product/abs(negative_value))*each)
            print("Iteration:,",each, "Max product:", max_product)
    return max_product

print(maxsubarrayproduct([1, -2, -3, -2, 7, -8, -2, 3]))