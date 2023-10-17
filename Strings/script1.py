my_name = "Gurpreet"
first_initial = my_name[0]
print(first_initial)

# Slicing Strings

first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
print(new_account)

temp_password = last_name[2:6]

# Concatenating Strings

first_name = "Julie"
last_name = "Blevins"


def account_generator(first_name, last_name):
    temp = first_name[:3] + last_name[:3]
    return temp


new_account = account_generator(first_name, last_name)

print(new_account)

# Sting Slicing

first_name = "Reiko"
last_name = "Matsuki"


def password_generator(first_name, last_name):
    temp_password = first_name[-3:] + last_name[-3:]
    return temp_password


temp_password = password_generator(first_name, last_name)

print(temp_password)

# Negative Indices
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"

second_to_last = company_motto[-2]
final_word = company_motto[-4:]

# Strings are Immutable
first_name = "Bob"
last_name = "Daily"


# first_name[0] = "R" # you cant do this as string are immutable
fixed_first_name = "R" + first_name[1:]


# Escape Characters
# password = "theycallme"crazy"91"
password = "theycallme\"crazy\"91"

# Iterating through Strings

def get_length(word):
    counter = 0
    for i in word:
        counter += 1
    return counter

# Strings and Conditionals (Part One)

def letter_check(word, letter):
    for i in word:
        if i == letter:
            return True
        else:
            return False

# Strings and Conditionals (Part Two)

def contains(big_string, little_string):
    if little_string in big_string:
        return True
    else:
        return False

def common_letters(string_one, string_two):
    empty_list = []

    for i in string_one:
        if i in string_two and not i in empty_list:
            empty_list.append(i)
    return empty_list

# Review


def username_generator(first_name, last_name):
    if len(first_name) < 3 or len(last_name) < 4:
        user_name = first_name + last_name
    else:
        user_name = first_name[:3] + last_name[:4]
    return user_name

def password_generator(user_name):
    password = ""
    for i in range(0,len(user_name)):
        print(i)
        password += user_name[i-1]
    return password


print(password_generator("Apple"))








