from appJar import gui

app = gui("Environment Quiz","500x500")

ques = []


class Question:
    def __init__(self,quesText,cans,pans1,pans2,pans3):
        self.quesText = quesText
        self.cans = cans
        self.pans1 = pans1
        self.pans2 = pans2
        self.pans3 = pans3
        
    def show(self):
        app.setLabel("question",self.quesText)
  
#main routine
ques.append(Question("Whats your name?", "anna", "bob", "grgr", " grg"))

ques[0].show()

app.addLabel("question", "")

app.go()