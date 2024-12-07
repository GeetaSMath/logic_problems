square_dict=dict()
for num in range(1,11):
    square_dict[num]=num*num
print(square_dict)


squ_dict=dict()
result={num:num*num for num in range(1,11)}
print(result)

squ_num=dict()
res={x:x**x for x in range(1,11) if x% 2==0}
print(res)


lst=["apple","banana","mango","orange"]
for index,i in enumerate(lst):
    print(index,i)
print(lst[2])

x=lst[0]="cucumber"

print(f"apple change to ",x)
lst2=[x for x in range(10) if x%2==0]
print(lst2)


lst_digit=[1,2,3,4,5]
lst_itm=["mango","apple","orange"]
result=[(i,j) for i in lst_digit for j in lst_itm]
print(result)

#remove duplicates from list

lst=[10,20,40,40,40,50,45]
print(f"remove duplicates",list(set(lst)))

#second largest number
item=[7,8,5,3,2]
x=list(set(item))
print(x)
print(x[-2])

lst = [0, 1, 9, 8, 4, 0, 0, 2, 7]

# Create a new list for non-zero elements
non_zero_elements = []
for x in lst:
    if x != 0:
        non_zero_elements.append(x)

# Count the zeroes
zero_count = lst.count(0)
print(zero_count)

# Add the zeroes to the end of the list
rearranged = non_zero_elements + [0] * zero_count

print("After moving zeroes:", rearranged)

lst_in = [0, 1, 9, 8, 4, 0, 0, 2, 7]
rearrange = [x for x in lst_in if x != 0] + [0] * lst.count(0)
print(rearrange)

