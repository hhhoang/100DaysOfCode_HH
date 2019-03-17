# https://www.codewars.com/kata/pick-peaks/train/python
# with M's help


def pick_peaks(arr):
   print("Input:", arr)
   if len(arr) < 3:
       return {"pos": [], "peaks": []}  # no results from empty list or only 2 elements

   peaks = []  # init -- no results yet
   pos = []  # init -- no results yet

   lookingForMax = arr[0] < arr[1]
   extreme = arr[0]
   extremePos = 0
   for i in range(1, len(arr)):  # through elements starting from the second one
       #print(i, arr[i])
       if lookingForMax:
           if arr[i] > extreme:
               extreme = arr[i]
               extremePos = i
               print("New max", extreme, "at", extremePos)
           elif arr[i] < extreme:
               print("Peak", extreme, "at", extremePos)
               peaks.append(extreme)
               pos.append(extremePos)
               lookingForMax = False
               extreme = arr[i]
               extremePos = i
       else:
           if arr[i] < extreme:
               extreme = arr[i]
               extremePos = i
               print("New min", extreme, "at", extremePos)
           elif arr[i] > extreme:
               print("Valley", extreme)
               lookingForMax = True
               extreme = arr[i]
               extremePos = i

   print(pos, peaks)
   return {"pos": pos, "peaks": peaks}
