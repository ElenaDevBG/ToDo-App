files = ["a.txt", "b.txt", "c.txt"]

for filename in files:
    file = open("../files/" + filename, "r")
    print(file.read())
    file.close()