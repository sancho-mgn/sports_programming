actual_string = ''
actual_idx = 1
undo_memory = []
len_mem = len(undo_memory)

def BastShoe(char):

    global actual_string
    global undo_memory
    global actual_idx
    global len_mem

    if char == '':
        return actual_string

    try:
        inp_data = char.split(' ', 1)
        cmd = int(inp_data[0])
    except ValueError:
        return actual_string

    if len(inp_data) > 1:
        chars = inp_data[1]
    else:
        chars = ''

    if int(cmd) == 1:
        if chars == '':
            return actual_string
        else:
            App_chr(chars)

    elif int(cmd) == 2:
        if chars == '' or actual_string == '':
            return actual_string
        else:
            Del_chr(chars)

    elif int(cmd) == 3:
        if chars == '':
            return ''
        else:
            index = Return_index(chars)
            return index

    elif int(cmd) == 4 and chars == '':
        if len(undo_memory) == 0:
            return actual_string
        else:
            Undo_act()

    elif int(cmd) == 5 and chars == '':
        if len(undo_memory) == 0:
            return actual_string
        else:
            Redo_act()
    else:
        return actual_string

    return actual_string


def App_chr(S):
    global actual_string
    global undo_memory
    global actual_idx
    global len_mem

    if actual_idx != 1:
        undo_memory = undo_memory[len_mem - actual_idx:len_mem - actual_idx + 1]
        actual_idx = 1

    if len(undo_memory) == 0:
        actual_string = S
        undo_memory.append(actual_string)
    else:
        actual_string = undo_memory[-1] + S
        undo_memory.append(actual_string)

    return actual_string


def Del_chr(N):
    global actual_string
    global undo_memory
    global actual_idx
    global len_mem

    if actual_idx != 1:
        undo_memory = undo_memory[len_mem - actual_idx:len_mem - actual_idx + 1]
        actual_idx = 1

    str_len = len(actual_string)
    try:
        if int(N) >= str_len:
            actual_string = ''
        else:
            actual_string = actual_string[:str_len - int(N)]
        undo_memory.append(actual_string)

        return actual_string
    except ValueError:
        return actual_string


def Return_index(i):
    global actual_string

    try:

        if int(i) >= len(actual_string) or int(i) < 0:
            return ''
        else:
            index = actual_string[int(i)]
            return str(index)
    except ValueError:
        return ''


def Undo_act():
    global actual_string
    global undo_memory
    global actual_idx

    if actual_idx == len(undo_memory):
        actual_idx = len(undo_memory)
    else:
        actual_idx += 1
    actual_string = undo_memory[len(undo_memory) - actual_idx]

    return actual_string


def Redo_act():
    global actual_string
    global undo_memory
    global actual_idx

    if actual_idx == 1:
        actual_string = undo_memory[len(undo_memory) - actual_idx]
    else:
        actual_idx -= 1
        actual_string = undo_memory[len(undo_memory) - actual_idx]

    return actual_string