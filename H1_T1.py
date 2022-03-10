def answer(x: int):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        t0 = 0
        t1 = 1
        t2 = 1
        i = 2
        while i < x:
            old_t2 = t2
            old_t1 = t1
            old_t0 = t0
            t2 = old_t2 + old_t1 + old_t0
            t1 = old_t2
            t0 = old_t1
            i += 1
        return t2


n = int(input())
print(answer(n))



