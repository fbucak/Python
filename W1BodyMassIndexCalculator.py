height=float(input("Please enter your height in m"))
weight=int(input("Please enter your weight in kg"))
print(weight/height**2)
if weight/height**2 <25:
    print("normal")
elif weight / height ** 2 >= 25 and height ** 2 / weight <= 30:
    print("over weight")
elif weight / height ** 2 > 30 and height ** 2 / weight < 40:
    print("obese")
else:
    print("extremly obse")