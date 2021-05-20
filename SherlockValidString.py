def SherlockValidString(s):
    if len(s) == 2:
        print(True)

    set_str = list(set(s))  # list with uniq chars
    count_chars = []

    for i in set_str:
        count_chars.append(s.count(i))

    count_chars = sorted(count_chars)  # sorted list with the count each of char

    uniq_cnt_chr = list(set(count_chars))

    len_uniq_cnt_chr = len(uniq_cnt_chr)

    if len_uniq_cnt_chr == 1:
        return True
    elif len_uniq_cnt_chr == 2 and count_chars.count(1) == 1:
        return True
    elif len_uniq_cnt_chr == 2 and (count_chars.count(count_chars[-1]) == 1) and (count_chars[-1] == count_chars[-2] + 1):
        return True
    else:
        return False