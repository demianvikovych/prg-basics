test_results = [
    False, True, False, True, True,
    True, True, False, True, True,
    False, True, True, True, False
]
question_number = len(test_results)
correct_answers = sum(test_results)
incorrect_answers = question_number - correct_answers
percentage_correct = (correct_answers / question_number) * 100

print('TEST STATISTICS')
print('===============')
print('Number of questions:', question_number)
print('Number of correct answers:', correct_answers)
print('Number of incorrect answers:', incorrect_answers)
print('Percentage of correct answers: {:.2f}%'.format(percentage_correct))
