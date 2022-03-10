def non_str(s: str):
    counter = [0] * 26
    dic = {}
    for i in range(len(s)):
        num = ord(s[i]) - ord("a")
        counter[num] += 1
        if counter[num] == 1:
            dic[s[i]] = i
        else:
            continue

    ans = []
    for j in range(26):
        if counter[j] == 1:
            ans.append(dic[chr(j + ord("a"))])
        else:
            continue
    if ans:
        return min(ans)
    else:
        return -1


pr = str(input())
print(non_str(pr))



