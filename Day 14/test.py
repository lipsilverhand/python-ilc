list1 = []

num = int(input("Enter number of elements in list: "))
 

for i in range(1, num + 1):
    element = int(input("Enter elements: "))
    list1.append(element)

print(list1)
     
# print minimum element:
print("Smallest element is:", min(list1))