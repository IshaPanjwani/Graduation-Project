import lovins
import EngLovinsRE

list = "experienced friends spend closed making".split()

lovinsOutput = []
lovinsREOutput = []

for i in list:
    lovinsOutput.append(lovins.stem(i))
    lovinsREOutput.append(EngLovinsRE.stem(i))
print(lovinsOutput)
print(lovinsREOutput)