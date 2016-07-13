"""
2D
"""
x = int(input("What is the length of your shape?: "))
y = int(input("What is the width of your shape?: "))
angle = int(input("What is the angle of your shape? :"))
if x == y and angle == (90):
    print("Your shape is a square")
elif x != y or angle == (90):
    print("Your shape is a rectangle")
    
