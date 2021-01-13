#Azaan DAwson amdg

def odd_num_index(x):
  for i,v in enumerate(x):
    if v % 2 != 0:
      print(i,v)
    else:
      continue
lst = [1,2,4,2,34,234,54,3,45,1,232,32,5]
'''
answer
0 1
7 3
8 45
9 1
12 5
'''
print(odd_num_index(lst))
