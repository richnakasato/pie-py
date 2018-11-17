def reverse_words(s):
    src = 0
    dst = len(s) - 1
    out = [None] * len(s)
    stack = list()
    while src < len(s):
        while src < len(s) and s[src] != ' ':
            stack.append(s[src])
            src += 1
        while len(stack):
            out[dst] = stack.pop()
            dst -= 1
        if src < len(s):
            out[dst] = s[src]
            src += 1
            dst -= 1
    return ''.join(out)


def main():
    s = "Do or do not, there is no try."
    r = "try. no is there not, do or Do"
    assert reverse_words(s) == r

if __name__ == "__main__":
    main()

