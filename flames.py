name1=str(input("Enter your name :"))
name2=str(input("Enter your crush name :"))
name1=name1.lower()
name2=name2.lower()
(list1,list2,count,list3)=([],[],0,["Friends","Love","Attraction","Marriage","Enemy","Sister"])
for i in range(len(name1)):
    list1.append(name1[i])
for j in range(len(name2)):
    list2.append(name2[j])
count1=list1.count(" ")
count2=list2.count(" ")
for k in range(count1):
    list1.remove(" ")
for l in range(count2):
    list2.remove(" ")
for m in range(len(list1)):
    for n in range(len(list2)):
        if list1[m]==list2[n]:
            list2.remove(list2[n])
            list2.insert(n,"*")
            count=count+2
            break

#print(list1,list2)
length=len(list1)+len(list2)-count
a=6
miche=0
for o in range(5):
    list3.remove(list3[(length%a)-1])
    if (length%a)-1 != -1:
       list3=list3[(length%a)-1:]+list3[:(length%a)-1]
    a= a-1
print("Relationship between",name1,"and",name2,"is",list3[0])

