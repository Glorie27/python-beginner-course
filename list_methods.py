list1 = [3, 4, 1, 5, 2]
list2 = ["banana", "apple", "mango", "oranges"]
list1.extend(list2)
list2.reverse()
print(list1)
list1.append("cherry")
print(len(list2))
list2.insert(1, "cherry")
list2.remove("banana")
list2.clear()
print(list2.index("mango"))
print(list2.count("mango"))
list.sort()

list3 = list2.copy()
print(list3)

del list2