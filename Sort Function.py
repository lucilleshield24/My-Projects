def sort(lists):
    c = len(lists)
    for x in range(0,c-1):
        for n in range(0, c-1):
            a = lists[n]
            b = lists[n+1]
            if a > b:
                lists[n] = b
                lists[n+1] = a
            
    print(lists)
            
            
my_list = [6, 2, 5, 4, 1]