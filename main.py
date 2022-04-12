# Random Day Trip Generator

print("Welcome! Thanks for choosing Day Trip Generator to plan your next vacation at random!")


destination_list = ["California", "Texas", "Florida"]

for destination in destination_list:
    user_input = input(f"We chose {destination} as your destination. Does this sound good? Enter yes or no.")
    if user_input == "yes":
        print("Awesome! Let's move on.")
        break
    elif user_input == "no":
        print("That's okay. Let's try again.")


transportation_list = ["Rental Car", "Train", "Plane"]

for transportation in transportation_list:
    user_input = input(f"We chose a(n) {transportation} for your transportation. Does this sound good? Enter yes or no.")
    if user_input == "yes":
        print("Awesome! Let's move on.")
        break
    elif user_input == "no":
        print("That's okay. Let's try again.")


food_list = ["Sushi Bar", "Steakhouse", "Pizzeria"]

for food in food_list:
    user_input = input(f"We chose a {food} for your dining. Does this sound good? Enter yes or no.")
    if user_input == "yes":
        print("Awesome! Let's move on.")
        break
    elif user_input == "no":
        print("That's okay. Let's try again.")


entertainment_list = ["Festival", "Lakehouse", "Waterpark"]

for entertainment in entertainment_list:
    user_input = input(f"We have chosen {entertainment} as your entertainment. Does this sound good? Enter yes or no.")
    if user_input == "yes":
        print("Congrats! We have now completed your next vacation!")
        break
    elif user_input == "no":
        print("That's okay. Let's try again.")

print("Now let's go over everything.")

print(f"Destination: {destination}")
print(f"Transportation: {transportation}")
print(f"Dining: {food}")
print(f"Entertainment: {entertainment}")

user_input = input("Are you ready to finalize your trip? Enter yes or no.")

if user_input == "yes":
    print(f"Great! We have you arriving in {destination} by a {transportation}. You will spend the day at a {entertainment}. After that, you will end the night at a {food}, to wrap up your fun filled day, here in beautiful {destination}!")
elif user_input == "no":
    print("That's okay. Let's try this again.")





    










