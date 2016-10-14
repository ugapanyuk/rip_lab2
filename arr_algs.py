def arr_min(arr):
  mn = arr[0]
  for i in range(1, len(arr)):
    cur = arr[i]
    if cur < mn:
      mn = cur
  return mn
  
def arr_avg(arr):
  sm = 0
  for i in range(len(arr)):
    sm+=arr[i]
  return sm / len(arr)

arr1 = [-10,3,2,1,-4.5,-15.5]
print(arr_min(arr1))  
arr2 = [2,2,4,4]     
print(arr_avg(arr2))
