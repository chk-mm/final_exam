def rec_sum(lst_sum):
    if len(lst_sum) == 1:
        return lst_sum[0]
    else:
        return lst_sum[0] + rec_sum(lst_sum[1:])


print(rec_sum([1,2,5]))