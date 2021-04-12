def selection_sort(l):
    n = len(l)
    for i in range(n):
        low_index = i
        for j in range(i + 1, n):
            if l[j] < l[low_index]:
                low_index = j
        l[i], l[low_index] = l[low_index], l[i]
    return l

def SynchronizingTables(N, ids, salary):
    new_salary = []
    ids_sort = selection_sort(ids.copy())
    salary_sort = selection_sort(salary.copy())
    for i in range(N):
        for j in range(N):
            if ids[i] == ids_sort[j]:
                new_salary.append(salary_sort[j])
    return new_salary

#print(SynchronizingTables(7,[98,23,61,49,1,79,9],[1,15,32,47,68,39,24]))