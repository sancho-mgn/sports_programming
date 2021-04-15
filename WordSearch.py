def splitter_to_words(string, len_splitter):
    '''Функция нарезает слова на слайсы элемента  + пробел'''
    text = string.split()
    lst_words = list()
    for i in text:
        while len(i) > len_splitter:
            lst_words.append(i[0:len_splitter])
            i = i[len_splitter:]
        lst_words.append(i + ' ')
    return lst_words


def align_lines(splitter_to_words, len_splitter):
    '''Функция выравнивает элементы согласно уканному срезу'''
    result = list()
    line = splitter_to_words[0]
    if len(splitter_to_words) == 1 and len(line[:-1]) <= len_splitter:
        result.append(line[:-1])
        return result
    lst = splitter_to_words[1:]
    for i in range(len(lst)):
        if len(line + lst[i][
                      :-1]) <= len_splitter:  # проверяем что предыдущий эл + текущий эл были не длинее заданного отрезка
            line += lst[i]
            continue
        else:
            if line[-1] == ' ':  # проверяем что сл. эл. пробел иначе отходим
                line = line[:-1]
            result.append(line)
            line = lst[i]
            if i == len(lst) - 1:
                if line[-1] == ' ':
                    line = line[:-1]
                result.append(line)
    return result

def WordSearch(lenn, s, subs):
    text = align_lines(splitter_to_words(s, lenn), lenn)
    result = [0]*len(text)
    for i in range(len(text)):
        if subs in text[i].split():
            result[i] = 1
    return result

#string = '1) строка разбивается на набор строк через выравнивание по заданной ширине.'
#len_splitter = 12
#subs = 'строк'
#print(WordSearch(len_splitter, string, subs))