# print("need to complete some variables ")
# print(round(2**3+56-32*3.434545465546565,2))
# print("\n---------------------------------------------------\n\n")
# print("..........................String Methods ................\n\n\n")
# string = input("enter your name\n")
# print("captilize method gives:  \n",string.capitalize())
# print("now casefold method of string gives : \n ",string.casefold())
# print("center method to print the text in center (aligning text in center) :\n",string.center(20))
# print ("count gives \n:  ",string.count("s"))
# print("encode method (å):\n ",string.encode())
# txt = "My name is tejå"
# print(txt.encode(encoding="ascii",errors="backslashreplace"))
# print(txt.encode(encoding="ascii",errors="ignore"))
# print(txt.encode(encoding="ascii",errors="namereplace"))
# print(txt.encode(encoding="ascii",errors="replace"))
# print(txt.encode(encoding="ascii",errors="xmlcharrefreplace"))
# print("endswith method :",string.endswith("s",))
# text = "H\tE\tL\tL\tO"
# print("expandtabs method:---------\n\n\n ")

# print(text.expandtabs())
# print(text.expandtabs(2))
# print(text.expandtabs(4))
# print(text.expandtabs(10))
# txct = "Hello, welcome to my world."
# print ("find function :\n",txct.find("e"))
# txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
# print("fromat function Used format method :",tx1)
# print("txt1 is alnum :",txt1.isalnum)
# print("tx1 is alpha :",txt1.isalpha)
# print(txt1.isascii())
# a = "\u0030" #unicode for 0
# b = "\u0047" #unicode for G

# print(a.isdecimal())
# print(b.isdecimal())
# c = "\u0030" #unicode for 0
# d = "\u00B2" #unicode for ²

# print(c.isdigit())
# print(d.isdigit())

#identifier
# txt = "Demo"
# x = txt.isidentifier()
# # print(x)
# a = "MyFolder"
# b = "Demo002"
# c = "2bring"
# d = "my demo"

# print(a.isidentifier())
# print(b.isidentifier())
# print(c.isidentifier())
# print(d.isidentifier())

# Check if all the characters in the texts are in lower case:

# a = "Hello world!"
# b = "hello 123"
# c = "mynameisPeter"

# print(a.islower())
# print(b.islower())
# print(c.islower())


# Check if the characters are numeric:

# a = "\u0030" #unicode for 0
# b = "\u00B2" #unicode for &sup2;
# c = "10km2"
# d = "-1"
# e = "1.5"

# print(a.isnumeric())
# print(b.isnumeric())
# print(c.isnumeric())
# print(d.isnumeric())
# print(e.isnumeric())


# txt = "Hello! Are you #1?"
# x = txt.isprintable()
# print(x)

# txt = "   "
# x = txt.isspace()
# print(x)

# a = "HELLO, AND WELCOME TO MY WORLD"
# b = "Hello"
# c = "22 Names"
# d = "This Is %'!?"
# print(a.istitle())
# print(b.istitle())
# print(c.istitle())
# print(d.istitle())

# Check if all the characters in the texts are in upper case:
# a = "Hello World!"
# b = "hello 123"
# c = "MY NAME IS PETER"
# print(a.isupper())
# print(b.isupper())
# print(c.isupper())



# Join all items in a tuple into a string, using a hash character as separator:
# myTuple = ("John", "Peter", "Vicky")
# x = "#".join(myTuple)
# print(x)

# Remove spaces to the left of the string:
# txt = "     banana     "
# x = txt.lstrip()
# print("of all fruits", x, "is my favorite")


# Using the letter "O" as the padding character:
# txt = "banana"
# x = txt.ljust(20, "O")
# print(x)

# Make the first letter in each word upper case:
# txt = "Welcome to my world"
# x = txt.title()
# print(x)


# Check if position 7 to 20 starts with the characters "wel":
# txt = "Hello, welcome to my world."
# x = txt.startswith("wel", 7, 20)
# print(x)

# Fill the strings with zeros until they are 10 characters long:
# a = "hello"
# b = "welcome to the jungle"
# c = "10.000"
# print(a.zfill(10))
# print(b.zfill(10))
# print(c.zfill(10))

# txt = "Hello My Name Is PETER"
# x = txt.swapcase()
# print(x)
# output :hELLO mY nAME iS peter


# strinf indexing (string is basically  an array in python)
# array = "Hi iam Revuss"
# print(len(array))
# for x in array:
#     print(x)
# if "Hi" in array:
#     print("yes it contains that")
# print("iam" in array)
# print ("hey" not in array)


# my_name = "revuss"
# slicing Function for my_name 
# print(my_name[-6:-1])




