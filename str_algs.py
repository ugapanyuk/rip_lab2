def str_rev(pstr):
  res = ""
  for i in range(len(pstr)):
    res = pstr[i] + res 
  return res  

str1 = "qwerty"
print(str_rev(str1))