data = input("please enter the String:   ")
list = ["ing", "ion", "ness", "es", "s", "ed", "ly"]

first = data[:1]
if (data == first):
    print("")
else:
    for i in list:
        if i in data:
            data = data.replace(i, "")
            break

print(data)


