# Given a string, find the length of the longest substring without repeating characters.

def lengthOfLongestSubstring(string: str) -> int:
    h = {}
    i = j = 0
    longest = 0
    for s in string:
        if s in h and i <= h[s]:
            i = h[s] + 1
        longest = max(longest, j-i+1)

        h[s] = j
        j += 1

    print(string, longest)
    return longest

if __name__ == '__main__':
    tests = ['abcabcbb', 'bbbbb', 'pwwkew', 'dvdf']
    answers = [3, 1, 3, 3]
    for i, s in enumerate(tests):
        if answers[i] != lengthOfLongestSubstring(s):
            print("Test", i+1, "failed")
