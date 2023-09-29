def sum_digit(digit):
    res = 0
    if digit > 10:
        tmp_n = []
        tmp_sn = str(digit)
        for x in tmp_sn:
            tmp_n.append(int(x))
        for y in tmp_n:
            res += y
        if res > 10:
            return sum_digit(res)
        else:
            return res
    else:
        return digit
def luhn(num):
    checksum = 0
    pl = str(num)
    chk = []
    for i in pl:
        chk.append(int(i))
        checksum = checksum + int(i)

    chk = chk[::-1]
    s = 0
    while (s<len(pl)):
        checksum = checksum - chk[s]
        tmp = sum_digit(chk[s]*2)
        chk[s] = tmp
        checksum = checksum +chk[s]
        s+=2

    res = (10-(checksum%10))%10
    return res

print(luhn(62))
print(luhn(250219941))
