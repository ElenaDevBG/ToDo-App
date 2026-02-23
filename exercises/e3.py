new_member = input("Add a new member: ")
file = open("../files/members.txt", "r")
members = file.readlines()
file.close()

file_w = open("../files/members.txt", "w")
members.append(new_member + "\n")
file_w.writelines(members)
file_w.close()