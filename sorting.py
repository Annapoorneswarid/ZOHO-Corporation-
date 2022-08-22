sort_list=[12,1,4,75,15,32,56,10,8,20]
print("Original list is:", sort_list)
for i in range(0,len(sort_list)):
    for j in range(i+1,len(sort_list)):
        if sort_list[i]>=sort_list[j]:
            sort_list[i],sort_list[j]=sort_list[j],sort_list[i]


print("After Sorting:",sort_list)