try:    
    subject1 = eval(input("Enter marks for Subject 1: "))
    subject2 = eval(input("Enter marks for Subject 2: "))
    subject3 = eval(input("Enter marks for Subject 3: "))
    subject4 = eval(input("Enter marks for Subject 4: "))
    subject5 = eval(input("Enter marks for Subject 5: "))

    aggregate_marks = subject1 + subject2 + subject3 + subject4 + subject5

    maximum_marks = 100 * 5  
    percentage_marks = (aggregate_marks / maximum_marks) * 100

    print("Aggregate Marks:", aggregate_marks)
    print("Percentage Marks:", percentage_marks)

except Exception as e:
    print("An error occurred:--------", e)   
