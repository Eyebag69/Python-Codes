list_1 = input("Enter a list:")
li = list(map(int ,list_1.split()))
li2 = li[: : -1]
print(f"input list is: {li}")
print(f"reversed list is: {li2}")