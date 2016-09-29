#sorted function
def aaron_sort(value_list):
#copy given list to 'cloned_list' (so variable will not be changed)
    cloned_list = value_list
    sorted_list = []
    i = len(cloned_list)
    while i>0:
        mn = min(cloned_list)
        cloned_list.remove(mn)
        sorted_list.append(mn)
        i = i - 1
    print (sorted_list)

aaron_sort([67, 45, 2, 13, 1, 998])
aaron_sort( [89, 23, 33, 45, 10, 12, 45, 45, 45])
