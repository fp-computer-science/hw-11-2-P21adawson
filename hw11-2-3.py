# Azaan DAwson amdg

def find_thing(x,y): 
  for i,v in enumerate(x):
    if x == str(x):
      print(str(y) + ' is found at index ' + str(x.find(y)))
      break
    else:
      if y not in x:
        print(-1) 
      else:   
        if y == v :
          print(str(y) +' is found at index ' +str(i) )
          break
        elif y!= v :
          continue 
     
user_input = ['c','h','i','c','k','e','n']       
user_input2 = 'chicken'
element_to_find = 'k'  
find_thing(user_input2, element_to_find) 
