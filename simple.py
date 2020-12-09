states_dict = {"AP": "INDIA", "TELANGANA":"INDIA",
               "HOUSTON": "USA", "TEXAS": "USA",
               "SYDNEY": "AUSTRALIA"}


def country_method(inp_dict):
    out_dict = {}
    param = []
    for k,v in inp_dict.items():
        try:
            key_val = out_dict[v]
        except KeyError:
            out_dict[v] = [k]
        else:
            key_val.append(k)

    return out_dict


print(country_method(states_dict))

# function name changes with decorators