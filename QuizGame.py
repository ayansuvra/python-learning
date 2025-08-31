def question():
    score = 0

    print("Q1. Which language is used for web apps?\n1. Python\n2. JavaScript\n3. C++\n4. Java")
    ans2 = int(input("Give your ans : "))
    if ans2 == 2:
        score += 1
    else:
        print("Wrong answer, 2 is the correct answer")

    print("Q2. What does HTML stand for?\n1. Hyper Trainer Marking Language\n2. Hyper Text Markup Language\n3. Hyper Text Marketing Language\n4. Hyper Text Markup Leveler")
    ans3 = int(input("Give your ans : "))
    if ans3 == 2:
        score += 1
    else:
        print("Wrong answer, 2 is the correct answer")

    print("Q3. Which of the following is a Python framework?\n1. Django\n2. React\n3. Angular\n4. Laravel")
    ans4 = int(input("Give your ans : "))
    if ans4 == 1:
        score += 1
    else:
        print("Wrong answer, 1 is the correct answer")

    print("Q4. What is the output of print(2**3)?\n1. 6\n2. 8\n3. 9\n4. 5")
    ans5 = int(input("Give your ans : "))
    if ans5 == 2:
        score += 1
    else:
        print("Wrong answer, 2 is the correct answer")

    print("Q5. Which keyword is used to define a function in Python?\n1. func\n2. define\n3. def\n4. function")
    ans6 = int(input("Give your ans : "))
    if ans6 == 3:
        score += 1
    else:
        print("Wrong answer, 3 is the correct answer")

    print("Q6. What is the correct file extension for Python files?\n1. .pyth\n2. .pt\n3. .py\n4. .pyt")
    ans7 = int(input("Give your ans : "))
    if ans7 == 3:
        score += 1
    else:
        print("Wrong answer, 3 is the correct answer")

    print("Q7. Which of the following is NOT a programming language?\n1. Python\n2. HTML\n3. Java\n4. C++")
    ans8 = int(input("Give your ans : "))
    if ans8 == 2:
        score += 1
    else:
        print("Wrong answer, 2 is the correct answer")

    print("Q8. What does 'int' stand for in Python?\n1. Integer\n2. Internal\n3. Interval\n4. Integration")
    ans9 = int(input("Give your ans : "))
    if ans9 == 1:
        score += 1
    else:
        print("Wrong answer, 1 is the correct answer")

    print("Q9. Which company developed Java?\n1. Microsoft\n2. Sun Microsystems\n3. Apple\n4. Google")
    ans10 = int(input("Give your ans : "))
    if ans10 == 2:
        score += 1
    else:
        print("Wrong answer, 2 is the correct answer")

    print("Q10. What is used to comment a single line in Python?\n1. //\n2. <!-- -->\n3. #\n4. /* */")
    ans11 = int(input("Give your ans : "))
    if ans11 == 3:
        score += 1
    else:
        print("Wrong answer, 3 is the correct answer")

    print("Your total score is:", score)

print("Welcome to Quiz Game")
ask = input("Do you want to start?(yes/no) : ")
if ask.lower()!="yes":
    quit()
else:
    print("Let's Start The Game!!")
    print("+1 point for correct answer and 0 for wrong answer")
    question()