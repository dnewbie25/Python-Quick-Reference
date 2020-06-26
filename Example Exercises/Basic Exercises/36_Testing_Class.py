from language_survey_35 import AnonymousSurvey

# Define a question and make a survey

question = "What language did your first learn to speak? "
my_survey = AnonymousSurvey(question)

# Show the question and store the response
my_survey.show_questions()

print("Enter 'q' at any time to quit")
while True:
  response = input()
  if response == 'q':
    break
  
  my_survey.store_response(response)

# Show the survey results

my_survey.show_results()