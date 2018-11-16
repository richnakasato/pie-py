import random

def str_to_num(s):
    if not s:
        return 0
    s_idx = 0
    neg = False
    if s[s_idx] == '-':
        s_idx += 1
        neg = True
    ret = 0
    for char in s[s_idx:]:
        ret *= 10
        ret += ord(char) - ord('0')
    if neg:
        return -ret
    return ret

def num_to_str(n):
    neg = False
    if n < 0:
        neg = True
        n = -n
    out_str = ''
    while n:
        c = chr(ord('0') + n%10)
        out_str = c + out_str
        n//=10
    if neg:
        return '-' + out_str
    return out_str


def main():
    for times in range(100):
        n = random.randint(-1000, 1000)
        s = str(n)
        assert str_to_num(s) == n
        assert num_to_str(n) == s

if __name__ == "__main__":
    main()

