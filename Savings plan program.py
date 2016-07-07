"""
Savings plan program
"""
Amount = int(input("How much do you want to invest each year?: "))
Years = int(input("How many years do you want to invest for? :"))
Interest = 0
ValuePerYear = 0


for i in range (0,Years):
    print("Year      "+"Start      "+"Paid In      "+"Interest      "+"Final      ")
