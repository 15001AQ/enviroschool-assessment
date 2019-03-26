
from appJar import gui
import random

score = 0
tries = 0
x = 0
y = 0
questionList = []
optionBoxList = []

app = gui("Environment Quiz","1200x400") 

class Question:
    def __init__(self,quesText,cans,pans1,pans2,pans3):
        self.quesText = quesText
        self.cans = cans
        self.pans1 = pans1
        self.pans2 = pans2
        self.pans3 = pans3
        
    def show(self):
        app.setLabel("Questions",self.quesText)
    
    
    def correctOrNot(self, userAnswer):
        self.userAnswer = app.getOptionBox("Your Answer:")
        if self.userAnswer != self.cans:
            app.setLabel("wrongOrRight", "Your answer is wrong, please try again.")
            return False
        else: 
            app.setLabel("wrongOrRight", "Correct Answer!")
            return True
                
        refreshQ()
  
class Options:
    def __init__(self,opAns):
        self.opAns = opAns
        #self.cans = "sewage, oil spils", "carbon dioxide emission", "wind turbines", "ice melting"
    
    def showOp(self):
        app.changeOptionBox("Your Answer:",self.opAns)
        return self.opAns
    
#main routine
def launch(win):
    if win == "Start":
        app.showSubWindow("questions")
        app.setLabel("Questions",questionList[x].show())
        app.changeOptionBox("Your Answer:",optionBoxList[y].showOp())
    elif win == "Exit":
        app.stop()

def showResults(button):
    global score, tries, x, y
    app.setLabel("Display","Congratulations!\nYou finished the quiz with a score of {}".format(score))
    x = 0
    y = 0
    score = 0
    tries = 0
    if button == "Restart Quiz":
        app.hideSubWindow("finish")
    elif button == "Close Program":
        app.stop()
    

def refreshQ():
    global score, tries, x, y
    print(score)
    print(tries)
    if x == 4:
        app.hideSubWindow("questions")
        app.showSubWindow("finish")
        showResults()
    app.setLabel("Questions",questionList[x].show())
    app.changeOptionBox("Your Answer:",optionBoxList[y].showOp())


def getAnswer():
    return str(app.getOptionBox("Your Answer:"))
    
    
def check(button):
    global x, y, score, tries
    if button == "Enter Answer":
        while questionList[x].correctOrNot(getAnswer()) == True:
            x = x + 1
            y = y + 1
            if tries == 0:
                score = score + 4
                tries = 0
            elif tries == 1:
                score = score + 3
                tries = 0
            elif tries == 2:
                score = score + 2
                tries = 0
            elif tries == 3:
                score = score + 1
                tries = 0
            refreshQ()
            break
        while questionList[x].correctOrNot(getAnswer()) == False:
            tries = tries + 1
            refreshQ()
            break
    elif button == "Go back":
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
app.setSize(870,400)
app.addLabel("Questions", "")
app.addLabel("wrongOrRight", "")
app.addLabelOptionBox("Your Answer:","")
app.setOptionBoxWidths("Your Answer:",50)
app.addButtons(["Enter Answer", "Go back"],check)
app.stopSubWindow()

#CREATING SUB WINDOW FOR FINISH
app.startSubWindow("finish", modal=True)
app.setBg("misty rose")
app.setSize(400,400)
app.addLabel("Display", "")
app.addButtons(["Restart Quiz","Close Program"],showResults)
app.stopSubWindow()


questionList.append(Question("What is water pollution caused by?","sewage, oil spills", "people swimming","people driving boats","climate change"))
questionList.append(Question("What is causing global warming?","carbon dioxide emission","summer season","moving closer to the sun","overpopulation"))
questionList.append(Question("What could we use to produce renewable energy?","wind turbines, solar energy","burning coal","use plastic","fossil fuels"))
questionList.append(Question("What are the effects of climate change?","ice melting", "more food will grow","less nasty weather","nothing bad will happen"))

optionBoxList.append(Options(["sewage, oil spills", "people swimming","people driving boats","climate change"]))
optionBoxList.append(Options(["carbon dioxide emission","summer season","moving closer to the sun","overpopulation"]))
optionBoxList.append(Options(["wind turbines, solar energy","burning coal","use plastic","fossil fuels"]))
optionBoxList.append(Options(["ice melting", "more food will grow","less nasty weather","nothing bad will happen"]))


app.go()