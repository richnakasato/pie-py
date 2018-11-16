def remove_specified_chars(s, r):
    remove_set = set(r)
    output = list()
    for char in s:
        if char not in remove_set:
            output.append(char)
    return ''.join(output)

def remove_specified_chars2(s, r):
    # two pointer method to perform inplace remove
    s_list = list(s)
    src = 0
    dst = 0
    remove_set = set(r)
    while src < len(s):
        if s_list[src] not in remove_set:
            s_list[dst] = s_list[src]
            dst += 1
        src += 1
    return ''.join(s_list[:dst])


def main():
    s = "Battle of the Vowels: Hawaii vs. Grozny"
    r = ["a", "e", "i", "o", "u"]
    assert remove_specified_chars(s, r) == "Bttl f th Vwls: Hw vs. Grzny"
    assert remove_specified_chars2(s, r) == "Bttl f th Vwls: Hw vs. Grzny"

if __name__ == "__main__":
    main()

