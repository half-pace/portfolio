sum_scores = 0
n = 1
total_sub = 5
while n <= total_sub:
    score = int(input(f"Enter score {n}: "))
    if score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        n *= 1
        continue
    else:
        print(f"You entered: {score}")
        sum_scores += score
        n += 1
    

avg_score = sum_scores / 5 
if avg_score > 90:
    grade = "A"
elif 80 <= avg_score <= 89:
    grade = "B"
elif 70 <= avg_score <= 79:
    grade = "C"
elif 60 <= avg_score <= 69:
    grade = "D"
else:
    grade = "F"
    
print(f"Your average score is: {avg_score:.1f}")
print(f"Your grade is: {grade}")

""" 
mastery

1) Break: is used to exit a loop by skiping the rest of the iteration. Continue: Skips the current iteration and continue ahead with the rest of the iteration

Break: 

num = [1, 3, 5]

for i in num:

      if i == 3:

             break

             print("Found")

       print(i)

continue:



num = [1, 3, 5]

for i in num:

      if i == 3:

             continue

      print(i)

2) it produces 2, 5, 8, 11, 14, 17

3) The pattern which accumulates over each iteration is the accumulator pattern, ie, starts initially with 0 and increases according to the loop's iteration.

res = 1

for i in range(1, 11):

      res *= i

print(res)

4)for loop is a loop which is used to iterate on any iterable whereas, while loop is a loop that keeps running until a condition is met or changes. For loop is used when you know what to iterate over. While loop is used where continuous looping is required until condition changes. example for - iterating over a list etc; while - requesting access until access is granted, network connection request until request granted etc

5) infinite loop is a loop that keeps looping without any stop condition.

while True:

             print("1: Start")

             print("2. View")

             print("3. Quit")

             choice = input("Enter: ")

             if choice == "1":

                     print("Starting")

             elif choice == "2":

                      print("Viewing")

              elif choice == "3":

                       print("Bye")

                       break

              else:

                          print("invalid choice")

exercise 

prog 1

       
"""