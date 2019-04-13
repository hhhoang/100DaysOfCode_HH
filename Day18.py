# https://www.codewars.com/kata/rainfall/train/python
# loops, string separation
def mean(town, strng):
    temp = get_temperature(town, strng)
    if len(temp) == 0:
        return -1 
    else:
        return sum(temp)/len(temp)

def variance(town, strng):
    temp = get_temperature(town, strng)
    mean_temp = mean(town, strng)
    var = []
    for i in temp:
        var.append((i - mean_temp)**2) 
    if len(var) == 0:
        return -1
    else:
        return (sum(var)/len(var))
      
def get_temperature(town, strng):
    temp = []
    for line in strng.split("\n"):
        data = line.split(":")
        if data[0] == town:
            for elem in data[1].split(","):
                t = elem.split(" ")
                temp.append(float(t[1]))
    return temp
