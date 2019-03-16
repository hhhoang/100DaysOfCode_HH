
#https://www.codewars.com/kata/pick-peaks/train/python


def pick_peaks(arr):
    print(arr)
    if len(arr) < 3:
        return {"pos": [], "peaks": []}  # no results from empty list or only 2 elements

    peaks = []  # init -- no results yet
    pos = []  # init -- no results yet

    max = arr[1]  # the second element as the maximum...
    max_pos = 1
    candidate = True  # ... candidate

    for i in range(2, len(arr)):  # through elements starting from the second one
        if arr[i] > max:
            max = arr[i]  # better candidate
            max_pos = i
            candidate = True
        elif arr[i] == max:  # if equal, local maximum was still the same
            candidate = True
        elif arr[i] < max:  # if lower then possible candidate to output
            if candidate:
                peaks.append(max)
                pos.append(max_pos)
            max = arr[i]  # start again...
            candidate = False  # being smaller it cannot be candidate

    # if candidate:  # if the peak at the very end
    # lst.append(m)
    print(pos, peaks)
    return {"pos": pos, "peaks": peaks}