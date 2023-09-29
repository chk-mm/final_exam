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
    pl = str(num)
    chk = []
    for i in pl:
        chk.append(int(i))

    chk = chk[::-1]
    s = 0
    while (s<len(pl)):
        tmp = sum_digit(chk[s]*2)
        chk[s] = tmp
        s+=2
    checksum = 0
    for z in chk:
        checksum = checksum + z
    if checksum < 10:
        return 10-checksum
    elif checksum == 10:
        return 0
    else:
        tmp_cal = abs(100-checksum)
        tmp_str = str(tmp_cal)
        return int(tmp_str[-1])

print(luhn(62))
print(luhn(250219941))
