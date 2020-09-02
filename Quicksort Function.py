test = [5, 8, 4, 6, 2, 3, 1, 1, 7]

def quicksort(lst):
    if len(lst) > 1:
        list1 = []
        list2 = []
        pivot = lst[0]
        for x in lst[1:]:
            if x < pivot:
                list1.append(x)
            else:
                list2.append(x)
        list1 = quicksort(list1)
        list2 = quicksort(list2)
        finallist = []
        finallist = list1 + [pivot] + list2
        return finallist
    else:
        return lst