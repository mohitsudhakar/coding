"""
This problem was asked by Palantir.

Write an algorithm to justify text. Given a sequence of words and an integer line length k,
return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
There should be at least one space between each word. Pad extra spaces when necessary so that
each line has exactly length k. Spaces should be distributed as equally as possible, with the
extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
"""

def fn(words, k):
    res, curr, num_letters = [], [], 0
    for word in words:
        num_spaces = len(curr)
        if num_letters + num_spaces + len(word) > k:
            for i in range(k - num_letters):
                # len(curr)-1 since last item shouldn't have a space after it
                curr[i%(len(curr)-1)] += ' '
            res.append(''.join(curr))
            num_letters = 0
            curr = []
        curr += [word]
        num_letters += len(word)
    if curr:
        res += [' '.join(curr).ljust(k)]
    return res


if __name__ == '__main__':
    words = 'the quick brown fox jumps over the lazy dog'
    words = words.split(' ')
    print(words)
    k = 16
    ans = fn(words, k)
    print(ans)