def perm(selected, remain, cnt):
    if not remain:
        print(cnt, selected)
    else:
        for i in range(len(remain)):
            cnt += 1
            select_i = remain[i]
            remain_list = remain[:i] + remain[i + 1:]
            perm(selected + [select_i], remain_list, cnt)


print(perm([], [1, 2, 3, 4], 0))