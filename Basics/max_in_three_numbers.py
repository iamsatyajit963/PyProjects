# Write a python Program to find and display the maximum of three given numbers
x, y, z = input("Enter three values: ").split()
def maximum(x,y,z):
    lst = [x, y, z ]
    return max(lst)

print(maximum(x,y,z))

# Time Complexity:  O(1)
# Auxiliary Space: O(1)