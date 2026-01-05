import time
import msvcrt
from colorama import Fore, Style, init

init()  # Initialize colorama

# Welcome message
print(Fore.CYAN + "Welcome to Online Examination System\n" + Style.RESET_ALL)

# Login
username = input("Enter username: ")
password = input("Enter password: ")

valid_user = False
with open("students.txt", "r") as file:
    for line in file:
        stored_user, stored_pass = line.strip().split(",")
        if username == stored_user and password == stored_pass:
            valid_user = True
            break

if not valid_user:
    print(Fore.RED + "Access Denied. Exiting..." + Style.RESET_ALL)
    exit()

print(Fore.GREEN + f"\nLogin Successful! Welcome, {username}\nStarting Exam...\n" + Style.RESET_ALL)

# Exam settings
total_exam_time = 30  # total exam time in seconds
questions = [
    {"question": "What is the output of print(2 + 3)?",
     "options": ["1", "5", "23", "Error"], "answer": "5"},
    {"question": "Which keyword is used to define a function in Python?",
     "options": ["func", "define", "def", "function"], "answer": "def"}
]

score = 0
start_time = time.time()

for i, q in enumerate(questions, 1):
    elapsed = time.time() - start_time
    remaining_time = total_exam_time - elapsed
    if remaining_time <= 0:
        print(Fore.YELLOW + "\n⏰ Time is up! Auto-submitting your exam..." + Style.RESET_ALL)
        break

    print(Fore.MAGENTA + f"\nQ{i}: {q['question']}" + Style.RESET_ALL)
    for idx, option in enumerate(q["options"], 1):
        print(f"{idx}. {option}")

    user_answer = ""
    print("Enter option number: ", end="", flush=True)

    while True:
        elapsed = time.time() - start_time
        remaining_time = int(total_exam_time - elapsed)

        # Show live countdown
        print(f"\rTime remaining: {remaining_time} sec | Your answer: {user_answer}", end="", flush=True)

        if remaining_time <= 0:
            print(Fore.YELLOW + "\n⏰ Time is up! Auto-submitting your exam..." + Style.RESET_ALL)
            break

        # Non-blocking input
        if msvcrt.kbhit():
            char = msvcrt.getwch()
            if char == "\r":  # Enter pressed
                print()
                break
            elif char == "\b":  # Backspace
                if len(user_answer) > 0:
                    user_answer = user_answer[:-1]
            else:
                user_answer += char

        time.sleep(0.1)  # small delay to reduce CPU usage

    if remaining_time <= 0:
        break  # exit if time expired

    # Validate answer
    if user_answer.isdigit() and 1 <= int(user_answer) <= len(q["options"]):
        selected_option = q["options"][int(user_answer) - 1]
        if selected_option.lower() == q["answer"].lower():
            score += 1
            print(Fore.GREEN + "✅ Correct!\n" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"❌ Wrong! Correct answer: {q['answer']}\n" + Style.RESET_ALL)
    else:
        print(Fore.YELLOW + "⚠️ Invalid input! Moving to next question.\n" + Style.RESET_ALL)

# Calculate results
total_questions = len(questions)
percentage = (score / total_questions) * 100
result = "PASS" if percentage >= 50 else "FAIL"
exam_time = time.strftime("%Y-%m-%d %H:%M:%S")

# Display final results
print(Fore.CYAN + "\n===== Exam Results =====" + Style.RESET_ALL)
print(Fore.CYAN + f"Student: {username}" + Style.RESET_ALL)
print(Fore.CYAN + f"Score: {score}/{total_questions}" + Style.RESET_ALL)
print(Fore.CYAN + f"Percentage: {percentage:.2f}%" + Style.RESET_ALL)
if result == "PASS":
    print(Fore.GREEN + f"Result: {result}" + Style.RESET_ALL)
else:
    print(Fore.RED + f"Result: {result}" + Style.RESET_ALL)
print(Fore.CYAN + f"Date & Time: {exam_time}" + Style.RESET_ALL)
print(Fore.CYAN + "========================\n" + Style.RESET_ALL)

# Save results
with open("results.txt", "a") as result_file:
    result_file.write(
        f"{username} | Score: {score}/{total_questions} | "
        f"Percentage: {percentage:.2f}% | Result: {result} | {exam_time}\n"
    )

print(Fore.GREEN + "✅ Your result has been saved for future reference in 'results.txt'." + Style.RESET_ALL)
