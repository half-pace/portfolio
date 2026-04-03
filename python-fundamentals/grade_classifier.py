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