from math import sqrt

def jumpSearch(array, x, n):
  step = sqrt(n)
  
  previous = 0
  while array[int(min(step, n)-1)] < x: 
    previous = step 
    step += sqrt(n) 
    if previous >= n: 
      return -1
 
  while array[int(previous)] < x: 
    previous += 1

    if previous == min(step, n): 
      return -1

  if array[int(previous)] == x: 
    return previous 
      
  return -1
