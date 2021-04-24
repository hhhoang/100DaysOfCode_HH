# Part of 100 Days of Code Course on Udemy by Angel Yu
# https://replit.com/@hhhoang/quiz-game-start#main.py

question_data = [{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"&quot;Typewriter&quot; is the longest word that can be typed using only the first row on a QWERTY keyboard.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Furby was released in 1998.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The word &quot;news&quot; originates from the first letters of the 4 main directions on a compass (North, East, West, South).","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"An eggplant is a vegetable.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Cucumbers are usually more than 90% water.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"You are allowed to sell your soul on eBay.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The average woman is 5 inches \/ 13 centimeters shorter than the average man.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Kissing someone for one minute burns about 2 calories.","correct_answer":"True","incorrect_answers":["False"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"The commercial UK channel ITV stands for &quot;International Television&quot;.","correct_answer":"False","incorrect_answers":["True"]},{"category":"General Knowledge","type":"boolean","difficulty":"medium","question":"Instant mashed potatoes were invented by Canadian Edward Asselbergs in 1962.","correct_answer":"True","incorrect_answers":["False"]}]
class Question():
  def __init__(self, text, answer):
    self.text = text
    self.answer = answer
class Quiz:
  def __init__(self, q_list):
    self.question_number = 0
    self.question_list = q_list
    self.score = 0
  
  def still_has_question(self):
    return self.question_number < len(self.question_list)

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False):")
    self.check_answer(user_answer, current_question.answer)
    
  def check_answer(self, user_answer, correct_answer):
    if user_answer.lower() == correct_answer.lower():
      print("You got it right!")
      self.score += 1
    else:
      print("That is wrong")
    print(f"The correct answer was: {correct_answer}.")
    print(f"Your current score is: {self.score}/{self.question_number}")
    print("\n")
    

question_bank = []
for question in question_data:
  q_text = question['question']
  q_answer = question['correct_answer']
  new_question = Question(q_text, q_answer)
  question_bank.append(new_question)

quiz = Quiz(question_bank)
while quiz.still_has_question():
  quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
