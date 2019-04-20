#https://www.codewars.com/kata/list-filtering/train/python?
def filter_list(l):
  'return a new list with the strings filtered out'
  print(l)
  result = []
  for i in l:
      try:
          if i%1==0:
              result.append(i)
      except:
          pass
  return result
