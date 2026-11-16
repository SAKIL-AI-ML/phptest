#problem 1
# str="hello"
# for i in str:
#     print(i,end=" ")
#problem 2
marks=0
details=(("John", "english",90), ("Alice", "physics",85), ("Bob", "chemistry",90), ("Charlie", "biology",74))
for i in range(len(details)):
    marks+=details[i][2]
avg=marks/4
print(avg)
list1=[]
for i in details:
    list1.append(abs(i[2]-avg))
index=list1.index(min(list1))
print(details[index][2])
list2=[]
for i in details:
    list2.append(i[2])
if len(list2)%2!=0:
    index=(len(list2)+1)//2
    print(list2[index-1],"is median")
else:
    index1=len(list2)//2
    index2=index1+1
    print((list2[index1-1]+list2[index2-1])/2,"is median")
#mode
dict1={"ram":90,"shyam":85,"hari":65,"gita":74}
for i in dict1:
    if dict1[i] == max(dict1.values()):
        print(i, "is the mode")