from django.shortcuts import render
from quiz_app.models import QuizName, QuestionModel, Leaderboard
from django.core.mail import send_mail

# Create your views here.

'''Function for profile page when user login'''
def profile(request):
    quiz_list = QuizName.objects.order_by('quiz_name')    
    list_of_Quiz = {
        'text_1': "This is List of Quiz",
        'quiz_list': quiz_list,
        }
    return render(request, 'quiz_app/profile.html', context = list_of_Quiz)

'''Function for quiz'''
def quiz_questions(request, category_id):
    if request.method == 'POST':
        '''Get the questions from the QuestionModel Model based on catagory using forign key'''
        quiz_questions_list = QuestionModel.objects.filter(category=category_id).all()
        score = 0
        wrong = 0
        correct = 0
        total = 0
        for row in quiz_questions_list:
            quiz_name = row.category
            total += 1
            if row.answer == request.POST.get(row.question):
                score += 10 # For correct answers 10 marks added
                correct += 1
            else:
                wrong += 1 # For wrong answers 3 marks deducted
                score -= 3
        quiz_two_percent = (score/(total*10)) * 100
        quiz_result = {
            'user_name':request.user.username,
            'quiz_name':quiz_name,
            'score': score,
            'correct': correct,
            'wrong': wrong,
            'percent': quiz_two_percent,
            'total': total,
        }
        '''Saving the Quiz result to database'''
        user_name = request.user.username
        result = Leaderboard(name = user_name, quiz_name = quiz_name, 
                             total = total, correct= correct, 
                             incorrect = wrong, percentage =quiz_two_percent)
        result.save()
        
        '''Email part'''
        send_mail("Your Quiz Result", 
                  f"{quiz_result}",
                  "skill_test_quiz@result.com",
                  ["hachandan02@gmail.com", "byregowda@gmail.com", "hanumareddi02@gmail.com"])
        return render(request,'quiz_app/result.html', context = quiz_result)
        
    else:
        '''Get the questions from the QuestionModel Model based on catagory using forign key'''
        # pk = primary key
        quiz_list = QuizName.objects.get(pk=category_id) 
        quiz_questions_list = QuestionModel.objects.filter(category=category_id).all()
        for row in quiz_questions_list:
            quiz_name = row.category
        quiz_questions = {'quiz_list': quiz_list,
                          'quiz_questions_list': quiz_questions_list,
                          'id': quiz_list.id,
                          'quiz_name':quiz_name,
                }
        return render(request, 'quiz_app/quiz.html', context = quiz_questions)
 
'''Function to display the Leaderboard''' 
def leader(request):
    result_list_board = Leaderboard.objects.all().order_by('percentage')
    dict = {'heading': "The Last Quizz Results of the Users",
            'result_list': result_list_board}
    return render(request, 'quiz_app/leader.html', context = dict)