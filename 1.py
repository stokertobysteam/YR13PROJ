"""
1
"""
a = int(input("Please input the angle of your shape: "))
x = int(input("Please input the length of your shape: "))
y = int(input("Please input the width of your shape: "))

if a == (90) and x == y:
    print("Your shape is a square")
    
if a == (90) and x != y:
    print("Your shape is a rectangle")
    
if a == (60) or a == (120):
    print("Your shape is a Hexagonal")
    
if a != (90) or (60) or (120) and x == y:
    print("Your shape is a Rhombic")
    
if a != (90) and x != y:
    print("Your shape is a Parallelogram")
