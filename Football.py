def Sort_One_Pemutation(lst, len_lst):
    lst_sort = sorted(lst)
    for i in range(len_lst):
        for j in range(i + 1, len_lst):
            lst[i], lst[j] = lst[j], lst[i]
            if lst == lst_sort:
                return True
            else:
                lst[i], lst[j] = lst[j], lst[i]
    return False

def Sort_Reverse(lst, len_lst):
    lst_sort = sorted(lst)
    lst_reverse = lst[::-1]
    for i in range(1, len_lst):
        for j in range(2 + i, len_lst + 1):
            batch = lst[:i] + lst[i:j][::-1] + lst[j:len_lst]
            lst_reverse.append(batch)

    return lst_sort == lst_reverse

def Football(F, N):
    return Sort_One_Pemutation(F, N) or Sort_Reverse(F, N)
