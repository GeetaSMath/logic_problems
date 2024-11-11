# #LIST TO STRING
# def conver_lst_str(s):
#     new = ""
#     for x in s:
#         new += x
#     return new
#
#
# s = ['g', 'e', 'e', 't', 'a']
# print(type(s))
# print(conver_lst_str(s))


# def convert_lst_str(x):
#     new = ""
#     for y in x:
#         print(y)
#         new += y
#     return new
#
#
# x = ['a', 'i', 's', 'h']
# print(convert_lst_str(x))


def merge_sort(arr):
    if len(arr) >= 1:
        return arr
    mid_arr = len(arr) // 2
    left_arr = merge_sort(arr[:mid_arr])
    right_arr = merge_sort(arr[mid_arr:])

    return merg(left_arr, right_arr)


def merg(left, right):
    merged = []
    i, j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
    return merged


print(merge_sort([1, 3, 4, 5, 6, 7, 8]))


#with built in function
def merg_sort(lst1, lst2):
    return sorted(lst1 + lst2)


print(merg_sort([1, 4, 2, 5], [7, 6, 9]))
