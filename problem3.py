def middle_return(ch):
    if len(ch)%2 != 0:
        return ch[len(ch)//2]
    else:
        return ch[(len(ch)//2)-1] + ch[(len(ch)//2)]

print(middle_return('testing'))
print(middle_return('test'))
print(middle_return('middle'))

