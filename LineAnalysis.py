def LineAnalysis(line):
    dot = line.count('.')
    star = line.count('*')

    if dot == 0 or star == 2:
        return True

    main_dots = 0

    for i in range(1, len(line)):
        if line[i] == '*':
            break
        main_dots += 1
    return main_dots * (star - 1) == dot