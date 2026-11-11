print("Hi ! Welcome to my first python program😊")
name = input("What is your name ? ")   ## Taking user name as input
age = int(input("What is your age ? "))  ## age as integer
hobby = input("What is your favourite thing to do? ")  ## hobby of the user
fav_subject = input("What was your favourite subject in school ? ") ## their fav_subject
strength = input("Can you tell one of your strengths? ") ## one of the strengths
fav_tv_show = input("Whats your favourite T.V Show ? ") ## their fav_tv_show


## Using f-strings to integrate variables inside strings , making the program more interactive
## just use the keyword before the string , and enclose the variable names inside curly brackets 

print("---------------------------------------------------------------")
print("")

print(f"Hii ! {name} , Pleasure to see you here !!. You are {age} years old and you like {hobby}.")
print(f"Your favourite subject in school was {fav_subject} and you are very {strength} person. Your favourite thing to watch on T.V is {fav_tv_show}.")