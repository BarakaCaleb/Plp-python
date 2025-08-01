#Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.
#Create a tuple containing the names of five of your favorite books. Then, use a for loop to print each book name on a separate line.
#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color. Ask the user for input and store the information in the dictionary. Then, print the dictionary to the console.
#Write a program that accepts user input to create two sets of integers. Then, create a new set that contains only the elements that are common to both sets.
#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.


input_string = input("Enter a list of integers separated by spaces")
integer_list = [int(num) for num in input_string.split()]
total_sum = sum(integer_list)
print("The sum of the integers is:", total_sum)



fav_books = ("Atomic Habits", "Javascript for dummies", "Rich Dad poor Dad")

for book in fav_books:
    print(book)


personal_intel = {}

personal_intel['name'] = input("Enter your name: ")
personal_intel['age'] = input("Enter your age: ")
personal_intel['favorite_color'] = input("Enter your favorite color: ")
print("Personal Information:", personal_intel)


