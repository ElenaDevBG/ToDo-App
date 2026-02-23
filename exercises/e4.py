filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for filename in filenames:
    file = open("../files/" + filename, "w")
    file.write("Hello")
    file.close()