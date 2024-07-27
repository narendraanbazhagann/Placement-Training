def bmii(w,h):
    return w / (h ** 2)

w= float(input("Enter your weight in kg: "))
h= float(input("Enter your height in meters: "))
bmi= bmii(weight, height)
print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("You are underweight.")
elif 18.5 <= bmi < 24.9:
    print("You have a normal weight.")
elif 25 <= bmi < 29.9:
    print("You are overweight.")
else:
    print("You are obese.")
