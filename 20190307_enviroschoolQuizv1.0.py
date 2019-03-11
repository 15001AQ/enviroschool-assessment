from appJar import gui

questionList = []

app = gui("Environment Quiz","500x500") 

class Question:
    def __init__(self,quesText,cans,pans1,pans2,pans3):
        self.quesText = quesText
        self.cans = cans
        self.pans1 = pans1
        self.pans2 = pans2
        self.pans3 = pans3
        
    def show(self):
        #app.setLabel("Question 1",self.quesText)
        #self.answer1 = app.getEntry("Your Answer:")
        print(self.quesText)
    
  
#main routine
'''
def settingQues(answer1):
    while answer1 != cans:
        ques.append(Question("Whats your name?", "anna", "bob", "grgr", " grg"))
        app.addLabel("Question 1", "")
        app.addLabelEntry("Your Answer:")
        ques[0].show()
        break
'''
questionList.append(Question("How long?","7","3","2","5"))
questionList.append(Question("How high?","7","3","2","5"))
#app.go()