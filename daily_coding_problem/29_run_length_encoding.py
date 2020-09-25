"""
This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings.
The basic idea is to represent repeated successive characters as a single count and character.
For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits
and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""

def fn(word):
    prev = word[0]
    curr_count = 0
    i = 0
    res = ""
    while i < len(word):
        while i < len(word) and word[i] == prev:
            curr_count += 1
            prev = word[i]
            i += 1
        res = res + str(curr_count) + prev
        curr_count = 0
        if i < len(word):
            prev = word[i]
    return res


if __name__ == '__main__':
    res = fn("AAAABBBCCDAA")
    print(res)
    assert res == "4A3B2C1D2A"