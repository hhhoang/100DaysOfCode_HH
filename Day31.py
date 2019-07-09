# https://www.codewars.com/kata/sort-and-transform/train/python
# converting the array into ASCII characters using chr() and sorted array using sorted()


def sort_transform(arr):
    arr_asc = sorted(arr)
    arr_desc = sorted(arr, reverse=True)
    number = []
    for i in arr:
        num = chr(i)
        number.append(num)
    number = sorted(number)
    first = chr(arr[0])+chr(arr[1])+chr(arr[-2])+chr(arr[-1])+"-"
    second = chr(arr_asc[0])+chr(arr_asc[1])+chr(arr_asc[-2])+chr(arr_asc[-1])+"-"
    third = chr(arr_desc[0])+chr(arr_desc[1])+chr(arr_desc[-2])+chr(arr_desc[-1])+"-"
    forth = number[0]+number[1]+number[-2]+number[-1]
    return first + second + third + forth
