# Azaan Dawson amdg 

def even_indexes(x):
  evens = []
  for i,v in enumerate(x):
    if i % 2 ==0 :
      evens.append(v)
    else:
      continue
  return evens    

lst = [1,34,54,67,2,45,654,123]
# answer [1, 54, 2, 654]
print('the numbers at even indexes were ' + str(even_indexes(lst)))
