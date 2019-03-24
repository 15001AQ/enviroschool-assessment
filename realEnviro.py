from appJar import gui

level = 0
x = level
questionList = []

app = gui("Environment Quiz","500x200") 

class Question:
    def __init__(self,quesText,cans,pans1,pans2,pans3):
        self.quesText = quesText
        self.cans = cans
        self.pans1 = pans1
        self.pans2 = pans2
        self.pans3 = pans3
        
    def show(self):
        app.setLabel("Questions",self.quesText)
    
    def correctOrNot(self):
        userAnswer = app.getOptionBox("Your Answer:")
        while userAnswer != self.cans:
            app.setLabel("wrongOrRight", "Your answer is wrong, please try again.")
            if userAnswer == self.cans:
                app.setLabel("wrongOrRight", "Correct Answer!")
                break
        swappingQ()
  
#main routine
def launch(win):
    if win == "Start":
        app.showSubWindow("questions")
        app.setLabel("Questions",questionList[x].show())        
    elif win == "Exit":
        app.stop()

    
def check(button):
    if button == "Enter Answer":
        questionList[x].correctOrNot()
    elif button == "Go back":
        app.stop()

def swappingQ():
    x = level
    if x == 0:
        x = x + 1
        app.setLabel("Questions",questionList[x].show())
        app.changeOptionBox("Your Answer:",["carbon dioxide emission","summer season","moving closer to the sun","overpopulation"])
    elif x == 1:
        x = x + 1
        app.setLabel("Questions",questionList[x].show())
        app.changeOptionBox("Your Answer:",["wind turbines, solar energy","burning coal","use plastic","fossil fuels"])  
    elif x == 2:
        x = x + 1
        app.setLabel("Questions",questionList[x].show())
        app.changeOptionBox("Your Answer:",["ice melting, rising temps and sea level", "more food will grow","less nasty weather","nothing bad will happen"])   
    else:
        app.stop()
            
#main routine - setting up the GUI
app.addLabel("title", "Welcome to my Environment Quiz")
app.addLabel("belowtitle", "In this quiz, you will be asked various questions\n        on the problems with our environment")
app.addLabel("belowbelowtitle", "Press Start to begin.")
app.setBg("light green")
app.addButtons(["Start", "Exit"],launch)

#CREATING SUB WINDOW FOR QUESTIONS
app.startSubWindow("questions", modal=True)
app.setBg("light green")
app.setSize(400,400)
app.addLabel("Questions", "")
app.addLabel("wrongOrRight", "")
app.addLabelOptionBox("Your Answer:",["sewage, oil spills", "people swimming","people driving boats","climate change"])

app.addButtons(["Enter Answer", "Go back"],check)
app.stopSubWindow()

app.startSubWindow("correct",modal=True)
app.setBg("red")
app.setSize(400,400)
app.addLabel("titl", x)
app.stopSubWindow()


questionList.append(Question("What is water pollution caused by?","sewage, oil spills", "people swimming","people driving boats","climate change"))
questionList.append(Question("What is causing global warming?","carbon dioxide emission","summer season","moving closer to the sun","overpopulation"))
questionList.append(Question("What could we use to produce renewable energy?","wind turbines, solar energy","burning coal","use plastic","fossil fuels"))
questionList.append(Question("What are the effects of climate change?","ice melting, rising temps and sea level", "more food will grow","less nasty weather","nothing bad will happen"))


app.go()