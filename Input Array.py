l=[1,2,3]
print("Existing List : ",l)
a=input("Enter one or more numbers separated by commas : ")
for i in a.split(","):
    l.append(int(i))
print("New List : ",l)
