def first_no_repeat(string):
    if not string:
        return None
    counts = dict()
    for char in string:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    for char in string:
        if counts[char] == 1:
            return char
    return None


def main():
    assert first_no_repeat(None)==None
    assert first_no_repeat("")==None
    assert first_no_repeat("total")=="o"
    assert first_no_repeat("teeter")=="r"
    assert first_no_repeat("aaa")==None

if __name__ == "__main__":
    main()

