def find_max_min(lists):
  max = lists[0]
  min = lists[0]
  for i in lists:
    if i < max:
      max = i
    if i > min:
      min = i
      
      
  if max == min:
    return [len(lists)]
    
    
  return [max,min]
  
  
print (find_max_min([1,2,34,56,78,90,43,3]))