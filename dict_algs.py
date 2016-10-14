ivan = {
"name" : "ivan" ,
"age" : 34 ,
"children" : [{
"name" : "vasja" ,
"age" : 32 ,
}, {
"name" : "petja" ,
"age" : 10 ,
}],
}
darja = {
"name" : "darja" ,
"age" : 41 ,
"children" : [{
"name" : "kirill" ,
"age" : 11 ,
}, {
"name" : "pavel" ,
"age" : 15 ,
}],
}
emps = [ ivan , darja]

def check(data):
  flag = False
  for i in data:
    if i['age'] > 18:
      flag = True
  return flag    

def test(emps):
  for i in emps:
    if check(i['children']):
      print(i['name'])

test(emps)