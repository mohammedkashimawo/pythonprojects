print("Welcome to the Mojjeasy Quiz")
confirm = input("Do you want to play? ").lower()
score = 0

if confirm == "yes":
    print("Press Enter to continue")

    ans1 = input("Who is the Vice President of Nigeria? - ")
    if ans1.lower() == "shettima":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans2 = input("What is the capital city of France? - ")
    if ans2.lower() == "paris":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans3 = input("Who is the President of Nigeria? - ")
    if ans3.lower() == "tinubu":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans4 = input("What is Nigeria’s currency? - ")
    if ans4.lower() == "naira":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans5 = input("How many states are in Nigeria? - ")
    if ans5.lower() == "thirty-six":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans6 = input("What is Nigeria’s national football team called? - ")
    if ans6.lower() == "supereagles":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans7 = input("When is Nigeria’s Independence Day? - ")
    if ans7.lower() == "october":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans8 = input("What year did Nigeria gain independence? - ")
    if ans8.lower() == "1960":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans9 = input("Which color is on Nigeria’s flag (other than white)? - ")
    if ans9.lower() == "green":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans10 = input("What is the capital city of China? - ")
    if ans10.lower() == "beijing":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans11 = input("What is the largest continent? - ")
    if ans11.lower() == "asia":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans12 = input("What is the currency of the UK? - ")
    if ans12.lower() == "pound":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans13 = input("Who is the President of the USA? - ")
    if ans13.lower() == "biden":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans14 = input("Which country is called Land of the Rising Sun? - ")
    if ans14.lower() == "japan":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans15 = input("Which desert is the largest in the world? - ")
    if ans15.lower() == "sahara":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans16 = input("What is the largest ocean? - ")
    if ans16.lower() == "pacific":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans17 = input("Which planet is closest to the sun? - ")
    if ans17.lower() == "mercury":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans18 = input("Who is the UN Secretary-General? - ")
    if ans18.lower() == "guterres":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans19 = input("Which planet is known for its rings? - ")
    if ans19.lower() == "saturn":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    ans20 = input("What is the chemical symbol for Gold? - ")
    if ans20.lower() == "au":
        print("Correct")
        score += 1
    else:
        print("Incorrect")

    print(f'Your total score is {score} out of 20!')

elif confirm == "no":
    print("Press Enter to continue")
    quit()
else:
    print("Invalid input. Exiting the quiz.")
    quit()
