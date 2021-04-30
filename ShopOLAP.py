def MergeListItem(N, items):
    dict_items = {}
    # spliting native list, convert list_items into dictionary
    for i in range(N):
        list_items = items[i].split()
        if dict_items.get(list_items[0]) == None:
            dict_items[list_items[0]] = int(list_items[1])
        else:
            dict_items[list_items[0]] += int(list_items[1])
    return dict_items


def SortedDictItem(dict_items):
    # sorting dictionary dict_items by values and keys
    dict_items = sorted(dict_items.items())
    dict_items.sort(key=lambda x: x[1], reverse=True)
    return dict_items


def ShopOLAP(N, items):
    dict_items = MergeListItem(N, items)
    dict_items_sort = SortedDictItem(dict_items)
    # unziping sorted dictionary into list
    list_res = []
    for i in dict_items_sort:
        list_res.append(i[0] + ' ' + str(i[1]))
    return list_res