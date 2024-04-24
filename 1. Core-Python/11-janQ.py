# 1. 7 to the power of 4
def func(a,b):
    return a ** b
print(func(7,4))

# def 🧬(✨,🗑️):
#     return ✨ ** 🗑️
# print(🧬(7,4))

# 2. split the string
s = "Hi there Sam!"
print(s.split())

# 3. use .format() to print the following statement: The diameter of Earth is 12742 kilometers.
planet = "Earth"
diameter = 12742
print(f"The diameter of {planet} is {diameter} kilometers.")

# 4. grab the word "hello using indexing"
def find_string(lst):
    for i in lst:
        if type(i) == list:
            result = find_string(i)
            if result:
                return result
        elif type(i) == str:
            return i

lst = [1,2,[3,4],[5,[100,200,["hello"]],23,11],1,7]
print(find_string(lst))

# 5. Grab the word "hello" from this nested dictionary
def find_hello(d):
    target_word = d["kl"][3]["tricky"][3]["target"][3]
    return target_word

d = {"kl": [1, 2, 3, {"tricky": ["oh", "man", "inception", {"target": [1, 2, 3, "hello"]}]}]}

result = find_hello(d)
print(result)

# 6. Difference between tuple and list.

# 7. create a function that grabs the email website domain from a string in the form: **user@domain.com. it returns "domain.com" for passing "user@domain.com"
def get_domain(email):
    user, domain = email.split('@')
    return domain

email_address = "user@domain.com"
result = get_domain(email_address)
print(result)

# 8. create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. :findDog("is there a dog here?") --> True
def find_dog(s):
    return "dog" in s.lower()
print(find_dog("is there a dog here?"))

# 9. Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example: seq = ['soup','dog','salad','cat','great'] should be filtered down to: ['soup','salad']
seq = ['soup','dog','salad','cat','great']
result = list(filter(lambda word: word[0] == 's', seq))
print(result)

# 10. You are driving a little too fast, and a police officer stops you. Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket". If your speed is 60 or less, the result is "No Ticket". If speed is between 61 and 80 inclusive, the result is "Small Ticket". If speed is 81 or more, the result is "Big Ticket". Unless it is your birthday (encoded as a boolean value in the parameters of the function) -- on your birthday, your speed can be 5 higher in all cases.
def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5
    if speed <= 60:
        return "No Ticket"
    elif speed <= 80:
        return "Small Ticket"
    else:
        return "Big Ticket"

print(caught_speeding(81,True))

# 11. Write a program to input roll no, physics marks, chemistry marks and maths marks out of 100. Calculate the total marks and percentage and status(pass/fail). If this student scores above 40 in 3 subjects, status is pass otherwise fail. calculate grade is status is pass.
# If percentage > 70 : grade = "Distinction", If percentage > 60 : grade = "First Class", If percentage > 50 : grade = "Second Class", If percentage > 40 : grade = "Pass Class",

rollNo = int(input("Enter roll no: "))
physics = int(input("Enter physics marks: "))
chemistry = int(input("Enter chemistry marks: "))
maths = int(input("Enter maths marks: "))

total = physics + chemistry + maths
percentage = total / 3

if physics > 40 and chemistry > 40 and maths > 40:
    status = "Pass"
else:
    status = "Fail"

if percentage > 70:
    grade = "Distinction"
elif percentage > 60:
    grade = "First Class"
elif percentage > 50:
    grade = "Second Class"
elif percentage > 40:
    grade = "Pass Class"
else:
    grade = "Fail"
print(f"Total marks: {total}")
print(f"Percentage: {percentage}%")
print(f"Status: {status}")
print(f"Grade: {grade}")
