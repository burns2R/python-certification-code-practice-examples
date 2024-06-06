total_sum = 0

for i in range(1, 21):
    if i == 10:
# Correct!! break statement would end the loop at 10
# continue statement keeps the loop running while ignoring
# 10 as expected by the excercise and output.
        continue
    if i % 2 == 0:
        total_sum += i
print("the sum of all even numbers between 1 and 20, excluding 10 is", total_sum)
    