# eval() test
x = 10
y = 20
result = eval("x+y", {'x': 10, 'y': 30}, {'x': 1, 'y': 2})
print("y:", y)
print(result)
