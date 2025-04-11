print("Half Pyramid Pattern of Question Mark(?):")
n = int(input("Enter the number of Rows:"))
for i in range(n):
    for j in range(i+1):
        print("? ", end="")
    print()