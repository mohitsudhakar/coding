def addLarge(num1, num2) -> int:
    res = ''
    num1 = num1[::-1]
    num2 = num2[::-1]
    l = len(num1) if len(num1) > len(num2) else len(num2)
    carry = 0
    for i in range(l):
        n1 = int(num1[i]) if i < len(num1) else 0
        n2 = int(num2[i]) if i < len(num2) else 0
        r = (n1 + n2 + carry) % 10
        carry = (n1 + n2 + carry) // 10
        res += str(r)

    res = res[::-1]
    return int(res)

if __name__ == '__main__':
    ans = addLarge('1237', '234')
    print(ans)

