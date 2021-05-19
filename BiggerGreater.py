def BiggerGreater(string):
    for i in range(len(string)-1,0,-1):
        if string[i] > string[i-1]:
            tmp_str = list(string[i - 1:])
            char_max = sorted(tmp_str)
            char = char_max[char_max.index(tmp_str[0]) + 1]
            x = tmp_str.index(char)
            tmp_str[0], tmp_str[x] = tmp_str[x], tmp_str[0]
            string = string[:i-1] + ''.join(tmp_str[0]) + ''.join(sorted(tmp_str[1:]))
            return string
    string = ''
    return string