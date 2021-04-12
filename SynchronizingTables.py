def SynchronizingTables(N, ids, salary):
    ids_sort = ids.copy()
    salary_sort = salary.copy()
    new_salary = []
    for i in range(N):
        low_index = i
        for j in range(i + 1, N):
            if ids[j] < ids[low_index]:
                low_index = j
            if salary[j] < salary[low_index]:
                low_index = j
        ids[i], ids[low_index] = ids[low_index], ids[i]
        salary[i], salary[low_index] = salary[low_index], salary[i]
    for i in range(N):
        for j in range(N):
            if ids[i] == ids_sort[j]:
                new_salary.append(salary_sort[j])
    return new_salary

#print(SynchronizingTables(3,[50,1,1024],[20,100,90]))