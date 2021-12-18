print("lists and operators ")
print("unitl 3pm today try as fast as possible")
ele = 23
print(ele<22)
print(ele>22)
print(ele<20 and  ele>22)
print(ele<20 or  ele>22)
print(not(ele<20 and  ele>22))
x = 2
y = 3
print(x is y)
print(x is not y)

# now the using lists with operators thing

x = ["aron","paul"]
print("ap" in x)
#list operations access , change item, add list item ,loop list, list comprehension , sort list , copy list , join lists , list methods ,list exercises

print(x[1])
x[1] ="balck widow"
print(x)
x[1:1] = ["apollo","hermes"]
print(x)
x.insert(0,"king")
print(x)
x.append("revuss")
print(x)
y = ["salmon","peter"]
x.extend(y)
print(x)
x.remove("revuss")
print(x)
x.pop(4)
print(x)
x.pop()
print(x)
del x[0]
print(x)
y.clear()
print(y)
del x


new_list = ["apple","banana","camel"]
for x in new_list:
    print(x)
for x in range(len(new_list)):
    print(new_list[x])  
print("\n\n\n\n\nWhile Loop\n\n\n\n")     
i=0
while i<len(new_list):
    print(new_list[i])
    i = i+1
print("\n\n\n\n\n")
[print(x) for x in new_list]    

x = ["apple","banana","carrot","betroot"]
b=[]
# for i in x:
#     if "a" in i:
#         b.append(i)
# print(b)    

# b = [i for i in x if "a" in i]
# print(b)
# b = [i for  i in x if "a" in i]
# print(b)
# b = [i for i in x if i!="apple"]
# print(b)
# b = [i for i in x if i != "banana"]
# print(b)

# complete copy of list

# b =[i for i in x]
# print(b)

# list  = [i for i in range(10) if i < 5]
# print(list)
# list  = [k for k in range(20) if k<10]
# list = [i.upper() for i in x]
# print(list)
# list = [i.capitalize() for i in x]
# print(list)

# now sorting the list

x.sort()
print(x)
x.sort(reverse=True)
print(x)
a = [12,34,45,6,78,90]
a.sort()
print(a)
a.sort(reverse= True)
print(a)