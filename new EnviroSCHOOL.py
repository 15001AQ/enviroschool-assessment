
from appJar import gui

level = 0
x = level
y = level
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
            return True
            #app.setLabel("wrongOrRight", "Your answer is wrong, please try again.")
        else: 
            return False
            #app.setLabel("wrongOrRight", "Correct Answer!")
                
        refreshQ()
  
class Options:
    def __init__(self,opAns):
        self.opAns = opAns
    
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

def refreshQ():
    app.setLabel("Questions",questionList[x].show())
    app.changeOptionBox("Your Answer:",optionBoxList[y].showOp())


def getAnswer():
    return str(app.getOptionBox("Your Answer:"))
    
    
def check(button):
    global x
    global y
    if button == "Enter Answer":
        if questionList[x].correctOrNot(getAnswer()) == True:
            #if x < len(questionList)-1:
            x += 1
            y += 1
            refreshQ()
        if questionList[x].correctOrNot(str(app.getOptionBox("Your Answer:"))) == False:
            #if x < len(questionList)-1:
            #x -= 1
            #y -= 1
            refreshQ()
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
app.setSize(1200,400)
app.addLabel("Questions", "")
app.addLabel("wrongOrRight", "")
app.addLabelOptionBox("Your Answer:","")
app.setOptionBoxWidths("Your Answer:",100)

app.addButtons(["Enter Answer", "Go back"],check)
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