#   Practices

name = "Hello world Jay"
age = 17 
print(name, age)

# "+"字串相連
print("19\"" + name)
print(name.upper())
print(name.upper().islower())
print(len(name))

# 數字轉成字串
str1 = str(age)
print(str1 + name)

# 字串轉數字
float1 = float(str1)
print(float1 + age)

# input預設為string
n1 = float(input("輸入數字1="))
n2 = float(input("輸入數字2="))
print("加起來總共=" + str(int(n1+n2)))

