def rreplace(data, old, new):
    li = data.rsplit(old, 1)
    return new.join(li)


data = input("please enter the String:   ")
list = ["ness", "es", "s", "ed", "d", "ing", "ion", "ly", "ful"]

i = 2
while (i < len(data)):
    if data[i:] in list:
        print(data[i:])
        data = rreplace(data, data[i:], "")
        i = 2
    i = i + 1
print(data)


