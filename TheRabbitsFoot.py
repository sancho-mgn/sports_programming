def str_slice(s):
    # calc count columns and lines
    len_s = int((len(s) ** 0.5) * 10) / 10
    cnt_lin = int(len_s // 1) # берём нижнюю границу, количество строк
    cnt_col = int(len_s % 1 * 10) # берём верхнюю границу, количество столбцов
    if cnt_col * cnt_lin < len(s):
        cnt_lin += 1
        # cut the string into slices and save them to the list
        list_s = [s[i:i + cnt_lin] for i in range(0, len(s), cnt_lin)]
        list_s = [iter(it) for it in list_s]
        return list_s
    else:
        list_s = [s[i:i + cnt_lin] for i in range(0, len(s), cnt_lin)]
        list_s = [iter(it) for it in list_s]
        return list_s

def trans_list_of_lists(list_s):
    len_s = len(list_s)
    list_enc = []
    while len_s:
        tmp = []
        for i, v in enumerate(list_s):
            try:
                values = next(v)
            except StopIteration:
                break
            tmp.append(values)
        list_enc.append(''.join(tmp))
        len_s -= 1
    return list_enc

def TheRabbitsFoot(s, encode):
    if encode:
        # del spaces in string
        s = s.split()
        s = ''.join(s)
        list_s = str_slice(s)
        list_enc = trans_list_of_lists(list_s)
        return ' '.join(list_enc)
    else:
        s = s.split()
        res = ''
        for i in range(len(s)):
            for j in range(len(s)):
                if i < len(s[j]):
                    res += s[j][i]
        return res


#s = 'отдай мою кроличью лапку'
#s_dec = 'омоюу толл дюиа акчп йрьк'
#encode_dec = False
#encode = True
#print(TheRabbitsFoot(s, encode))
#print(TheRabbitsFoot(s_dec, encode_dec))