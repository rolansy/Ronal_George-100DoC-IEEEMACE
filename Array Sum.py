a=input("Enter one or more numbers separated by commas : ")
l=[]
for i in a.split(","):
    l.append(int(i))
print("List : ",l)
def arr_sum(l):
    print("Sum : ",sum(l))
arr_sum(l)