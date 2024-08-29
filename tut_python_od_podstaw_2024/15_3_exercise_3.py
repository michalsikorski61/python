result_exam = input('Enter the result of the exam (0-100): ')
result_exam = int(result_exam)
if result_exam >= 90:
    print('Very good result')
elif result_exam >= 80: # 80-89 because 90 is already checked
    print('Good result')
elif result_exam >= 70:
    print('Satisfactory result')
elif result_exam >= 60:
    print('Sufficient result')
elif result_exam < 60:
    print('Unsatisfactory result')
else:
    print('Invalid result')