# Longest palidromic substring

def lps_count(s):
    def check(s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return j-i-1
    longest = 0
    for i in range(len(s)):
        longest = max(longest, check(s, i, i), check(s, i, i+1))
    return longest

def lps(s):
    def check(s, i, j):
        while i >= 0 and j < len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return s[i+1:j]
    longest = ""
    for i in range(len(s)):
        longest = max(longest, check(s, i, i), check(s, i, i+1), key=len)
    return longest


if __name__ == '__main__':
    string = 'abcbbabbdef'
    count = lps_count(string)
    substr = lps(string)
    print(substr, count)