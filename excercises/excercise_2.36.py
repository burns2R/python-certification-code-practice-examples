def show_message(name, age):
    print(f'{name} is {age} years old.')

students = [('Tim', 20), ('Anna', 23)]

# Note: just standard “for item in list” for loop!!!
# Proof: https://wiki.python.org/moin/ForLoop
for student in students:
    show_message(student[0], student[1])