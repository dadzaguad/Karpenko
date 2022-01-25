def sum_seq(acc):
    n = int(input())
    if n == 0:
        return acc
    else:
        return sum_seq(acc + n)


print(sum_seq(0))
