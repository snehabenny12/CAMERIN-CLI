import time

print("Welcome to Online Examination System")

username = input("Enter username: ")
password = input("Enter password: ")

file = open("students.txt", "r")

valid_user = False

for line in file:
    line = line.strip()
    stored_user, stored_pass = line.split(",")

    if username == stored_user and password == stored_pass:
        valid_user = True
        break

file.close()

if not valid_user:
    print("Access Denied. Exiting...")
    exit()

print("Login Successful!")

print("\nStarting Exam...\n")

questions = [
    {
        "question": "What is the output of print(2 + 3)?",
        "options": ["1", "5", "23", "Error"],
        "answer": "5"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["func", "define", "def", "function"],
        "answer": "def"
    }
]
score = 0
for q in questions:
    print(q["question"])
    
    for option in q["options"]:
        print(option)

    user_answer = input("Enter your answer: ")



    if user_answer == q["answer"]:
        score += 1
        print("Correct!")
    else:
        print("Wrong!")

    print()


print()
print("Exam Finished")
print("Your Score:", score)
total_questions = len(questions)
percentage = (score / total_questions) * 100

print("Percentage:", percentage)
if percentage >= 50:
    result = "PASS"
else:
    result = "FAIL"

print("Result:", result)

result_file = open("results.txt", "a")

current_time = time.strftime("%Y-%m-%d %H:%M:%S")

result_file.write(
    f"{username} | Score: {score} | Percentage: {percentage} | Result: {result} | {current_time}\n"
)

result_file.close()




