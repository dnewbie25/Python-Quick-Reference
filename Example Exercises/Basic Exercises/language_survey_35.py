class AnonymousSurvey:

  """Collects anonymous answers to survey questions"""
  
  def __init__(self, question):
    """Store a question and prepares to store answers"""
    self.question = question
    self.responses = []
    
  def show_questions(self):
    """show the survey questions"""
    print(self.question)
    
  def store_response(self, new_response):
    """store a single response to a survey"""
    self.responses.append(new_response)
    
  def show_results(self):
     """Show all the responses given"""
     print("Survey results")
     for response in self.responses:
        print(f"- {response}")  