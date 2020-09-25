"""
This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

def fn(string: str) -> int:

    # f(i) = ans till i
    # f(i) = f(i-1) if 1 <= int(string[i-1]) <= 9
    #        f(i-2) if 10 <= int(string[i-2:i] <= 26
    def rec(i):
        if dp[i] != -1:
            return dp[i]
        if i == 0:
            return 1

        ans = 0
        if i-1 >= 0 and 1 <= int(string[i-1]) <= 9:
            ans += rec(i-1)
        if i-2 >= 0 and 10 <= int(string[i-2:i]) <= 26:
            ans += rec(i-2)
        dp[i] = ans
        return dp[i]

    dp = [-1]*(len(string)+1)
    return rec(len(string))

if __name__ == '__main__':

    # res = fn("111111111111111111111111111111111111111111")
    res = fn("111")
    print(res)
