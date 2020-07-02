import unittest
from language_survey_35 import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):
  """Test for the class AnonymousSurvey"""

  def setUp(self):
    """Create a survey and a set of reponses for use in all test methods"""
    # This method setUp( ) creates an instance that can be used in the test so you don't have to create a new instance for every test method
    question = "What languages did you first learn to speak?"
    self.my_survey = AnonymousSurvey(question)
    self.responses = ['English', 'Spanish', 'Finnish'] 


  def test_store_single_response(self):
    """Test that a single response is stored correctly"""
    #question = "What language did you first learn to speak? " -------->>>>can be replaced by using the setUp( ) method

    #my_survey = AnonymousSurvey(question) --------->>> This instance of the AnonymousSurvey class can be replaced by using the setUp( ) method

    #my_survey.store_response('English') # This is a method from AnonymousSurvey ---------->>>can be replaced by using the setUp( ) method
    self.my_survey.store_response(self.responses[0]) 
    self.assertIn(self.responses[0], self.my_survey.responses) # Ensures the response gets sotred in the response list we have defined in AnonymousSurvey

  def test_store_three_responses(self):
    """Test that three individual responses get sotred correctly"""
    #question = "What language did you first learn to speak? " --->>>>>can be replaced by using the setUp( ) method

    #my_survey = AnonymousSurvey(question) --------->>> This instance of the AnonymousSurvey class can be replaced by using the setUp( ) method

    #responses = ['English', 'Spanish', 'Finnish'] # We create a list here ---->>>>can be replaced by using the setUp( ) method

    for response in self.responses: # We loop through that list and pass each item into responses, the list from AnonymousSurvey
      self.my_survey.store_response(response)

    for response in self.responses: # Checks that each one of the languages we add to that list is in fact inside that list
      self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
  unittest.main()
