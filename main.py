# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year%4 == 0 and year% 100 != 0 :
  print("It is leap year")
elif  year%4 == 0 and year% 100 == 0 and year%400 == 0:
  print("It is leap year")
else:
  print("It is not leap year")

