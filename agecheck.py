#age checker program
age = input("How old are you: \n")
movie = input("Enter movie title: \n")

if movie=="Sex on The Beach" and int(age) < 18:
    print("You are not allowed to see " + movie)

if movie=="Ayinla" and int(age) < 18:
    print("You are not allowed to see " + movie)

elif movie=="Sex on The Beach" and int(age) >= 18:
    print("Proceed to purchase ticket for " + movie)

elif movie=="Ayinla" and int(age) >= 18:
    print("Proceed to purchase ticket for " + movie)

else:
    print(movie + " is not on our list")





#if int(age) < 18:
   # print("The contents of " + str(movie) + " may not be suitable for you. Kindly purchase another movie ticket")
