def rreplace(data, old, new):
    li = data.rsplit(old, 1)
    return new.join(li)


data = input("please enter the String:   ")
list = ["ness", "es", "s", "ed", "d", "ing", "ion", "ly", "ful"]

if (len(data) == 2):
    print(data)
else:
    for i in list:
        if data.endswith(i):
            data = rreplace(data, i, "")
print(data)


