#importing the appjar module
from appJar import gui

#setting my variables.
#score = the points the player accumulates - tries = the amount of times they get a question wrong
score = 0
tries = 0
#totalTries is the amount of tries the player took over the whole quiz - it displays at the end.
totalTries = 0
#"x" is the question number. 0 is the first question number.
x = 0
#"y" is the option box answers number. 0 is the first option box answers number.
y = 0

#my lists
questionList = []
optionBoxList = []

#setting name and size of the GUI
app = gui("Environment Quiz","500x400") 

#*****CLASSES*****

#defining the Question class.
#This class will store what the correct answer is and what all the wrong answers are, it will also store the questions. 
class Question:
    #this method in my Question class is initialising all of the variables
    #these variables will tell me the question and what answer is right or wrong
    def __init__(self,quesText,cans,wans1,wans2,wans3):
        self.quesText = quesText
        self.cans = cans
        self.pans1 = wans1
        self.pans2 = wans2
        self.pans3 = wans3
        
    #this method displays the question, and it is commonly called throughout my code
    def show(self):
        app.setLabel("Questions",self.quesText)
    
    #this method decides if the answer given by the user is correct or not
    #it does this by getting the option box answer chosen by the user, and sets it as userAnswer
    #then if userAnswer is correct, it returns True back to the function "check"
    #if userAnswer is incorrect, it returns False back to the function "check" and it makes a label appear which tells you you're wrong.
    def correctOrNot(self, userAnswer):
        self.userAnswer = app.getOptionBox("Your Answer:")
        if self.userAnswer != self.cans:
            app.setLabel("wrongOrRight", "Your answer is wrong, please try again.")
            return False
        else: 
            return True
        
        refreshQ()

#defining the Options class.
#This class will store the different option box answers for each question
class Options:
    def __init__(self,opAns):
        self.opAns = opAns
    
    #this method changes the option box answers to fit what the new question is
    def showOp(self):
        app.changeOptionBox("Your Answer:",self.opAns)
    
#*****MAIN ROUTINE*****

#defining the launch function.
#this function is what runs when you press either the "Start" or "Exit" button
def launch(button):
    #pressing the "Start" button results in a sub window called "questions" to pop up, this window has several labels and buttons on it.
    if button == "Start":
        app.hide()
        app.showSubWindow("questions")
        app.setLabelSticky("cornerScore", "left")
        app.setLabel("cornerScore", "Score: {}\nTries: {} ".format(score, tries))        
        app.setLabel("Questions",questionList[x].show())
        app.changeOptionBox("Your Answer:",optionBoxList[y].showOp())
    #pressing the "Exit" button results in the program stopping.
    elif button == "Exit":
        app.stop()

#defining the showResults function.
#this function shows the user their final results (score and totalTries) after they've finished the quiz
def showResults():
    global score, totalTries, x, y
    app.setLabel("Display","                 Congratulations!\nYou finished the quiz with a score of {}\nYou clicked the wrong answer {} times".format(score, totalTries))
    #setting all the variables so the user can restart if they want to
    x = 0
    y = 0
    score = 0
    tries = 0
    totalTries = 0
    #calling finishButton function
    finishButton(button)
    
#defining the finishButton function.
#this function is used for the 2 buttons in the finishing window
def finishButton(button):
    #pressing the "Restart Quiz" button will close the finishing window and go back to the menu
    if button == "Restart Quiz":
        app.setLabel("wrongOrRight", "-----")
        app.hideSubWindow("finish")
        app.show()
    #pressing the "Close Program" button will close the whole program
    elif button == "Close Program":
        app.stop()
    
#defining the refreshQ function.
#this function is used to change the question label and option box answers
def refreshQ():
    global score, tries, x, y
    #there is no question number 4, so if x equals 4, the question window will close and the finish window will open
    if x == 9:
        app.hideSubWindow("questions")
        app.showSubWindow("finish")
        #calling showResults function
        showResults()
    #x can be anything 0 or above, so putting x as the list number makes the code a lot more flexible
    #the label below calls the question number to the method "show" in the Question class.
    app.setLabel("Questions",questionList[x].show())
    #shows the user their score and tries throughout the quiz
    app.setLabel("cornerScore", "Score: {}\nTries: {} ".format(score, tries))
    #y can be anything 0 or above, so putting y as the list number makes the code a lot more flexible
    #the label below calls the option box number to the method "showOp" in the Options class.
    app.changeOptionBox("Your Answer:",optionBoxList[y].showOp())   

#defining the getAnswer function.
#this function may seem useless, but it is used to alleviate any confusion with the program
#appJar is not widely used and isn't as developed as other GUI modules, so piling on a lot of code in one line might cause problems in the program
def getAnswer():
    return str(app.getOptionBox("Your Answer:"))
        
#defining the check function
#this function is used to check whether the answer is correct after the user presses the "Enter Answer" button
#if the answer is correct, it will add the correct score. if the answer is wrong, it will add the correct number of tries
#this function also has a "Go back" button, when pressed, the questions window will close and reveal the menu again
def check(button):
    global x, y, score, tries, totalTries
    if button == "Enter Answer":
        #this while loop keeps looping until either x or y is increased, and if a score is added.
        while questionList[x].correctOrNot(getAnswer()) == True:
            #adding one to the question number becuse the question just answered was correct
            x = x + 1
            #adding one to the option box number becuse the question just answered was correct
            y = y + 1
            #these if statements below determine what points the user will receive
            #no wrong answers = 4 points, 1 wrong answer = 3 points, 2 wrong answers = 2 points, 3 wrong answers = 1 point, MORE THAN 3 wrong answers = no points
            #all throughout the totalTries variable is counting each try to display at the end
            if tries == 0:
                #this label tells the user they got the answer correct
                app.setLabel("wrongOrRight", "Correct Answer!")
                score = score + 4
                tries = 0
            elif tries == 1:
                app.setLabel("wrongOrRight", "Correct Answer!")
                totalTries = totalTries + tries
                score = score + 3
                tries = 0
            elif tries == 2:
                app.setLabel("wrongOrRight", "Correct Answer!")
                totalTries = totalTries + tries
                score = score + 2
                tries = 0
            elif tries == 3:
                app.setLabel("wrongOrRight", "Correct Answer!")
                totalTries = totalTries + tries
                score = score + 1
                tries = 0
            elif tries > 3:
                totalTries = totalTries + tries
                score = score
                #this label tells the user they got the answer correct, but they receive no points because they had more than 3 tries
                app.setLabel("wrongOrRight", "Correct Answer!\nBut.. you had {} tries, so you receive 0 points\nMaximum amount of tries is 3".format(tries))
                if x == 9:
                    app.setLabel("wrongOrRight", "Correct Answer!\nBut.. you had {} tries, so you receive 0 points\nMaximum amount of tries is 3".format(tries))         
                    tries = 0
            #calls the refreshQ function   
            refreshQ()
            break
        #this while loop keeps looping until the user gets a correct answer
        #each time this while loop loops, a try is added
        while questionList[x].correctOrNot(getAnswer()) == False:
            tries = tries + 1
            refreshQ()
            break
    elif button == "Go back":
        app.hideSubWindow("questions")
        x = 0
        y = 0
        score = 0
        tries = 0
        app.setLabel("wrongOrRight", "-----")
        app.show()

#*****SETTING UP THE VARIOUS WINDOWS*****

#SETTING UP THE START MENU
app.addLabel("title", "Welcome to my Environment Quiz")
app.addLabel("belowtitle", "In this quiz, you will be asked various questions\n        on the problems with our environment")
app.addLabel("belowbelowtitle", "Press Start to begin.")
app.setBg("pale green")
app.setLabelBg("title","spring green")
app.setLabelBg("belowtitle", "light green")
app.setLabelBg("belowbelowtitle","spring green")
app.addButtons(["Start", "Exit"],launch)

#CREATING SUB WINDOW FOR QUESTIONS
app.startSubWindow("questions", modal=True)
app.setBg("pale green")
app.setSize(450,400)
app.addLabel("Questions", "", 0)
app.setLabelBg("Questions", "spring green")
app.getRow()
app.addLabel("wrongOrRight", "-----", 1)
app.addLabelOptionBox("Your Answer:","", row=2)
app.setOptionBoxWidths("Your Answer:",25)
app.addLabel("cornerScore", "", 0, 2)
app.addButtons(["Enter Answer", "Go back"],check, row=3, colspan=3)
app.stopSubWindow()

#CREATING SUB WINDOW FOR FINISH
app.startSubWindow("finish", modal=True)
app.setBg("pale green")
app.setSize(400,400)
app.addLabel("Display", "")
app.setLabelBg("Display", "spring green")
app.addButtons(["Restart Quiz","Close Program"],finishButton)
app.stopSubWindow()

#These lines of code are for adding each question to the list. They are going straight to the Question class
#The variables in the Question class are in the order; question text, correct answer, wrong ans1, wrong ans2 and wrong ans3
#The order the strings are in the lines of code below correlate to the order of the Question class, which means the class will identify them as each variable.
questionList.append(Question("What is water pollution caused by?","sewage, oil spills", "people swimming","people driving boats","climate change"))
questionList.append(Question("What is causing global warming?","carbon dioxide emission","summer season","moving closer to the sun","overpopulation"))
questionList.append(Question("What could we use to produce renewable energy?","wind turbines, solar energy","burning coal","use plastic","fossil fuels"))
questionList.append(Question("What are the effects of climate change?","ice melting, rising temps", "more food will grow","less nasty weather","nothing bad will happen"))
questionList.append(Question("How many acres of forest is cut down every second?","One and a half acres","Two acres","One acre","Half an acre"))
questionList.append(Question("How much pollution is in the world?","14 billion pounds","7 billion pounds","20 billion pounds","10 billion pounds"))
questionList.append(Question("What will happen when our ozone layer is depleted?","Many plants will die in a few days","Humans would die instantly","Everything would be on fire","Nothing will happen"))
questionList.append(Question("What do oil spills do?","They make the water harmful to animals","They make the water slippery","Nothing happens","We lose money"))
questionList.append(Question("Click the renewable energy:","Hydro","Coal","Gas","Oil"))
questionList.append(Question("When have we estimated there will be no more rain forests?","In 100 years","In 250 years","In 75 yearse","In 175 years"))

#These lines of code are for adding option box answers to a list. They are going straight to the Options class
#The variable in the Option class is just "opAns", this means that the answers below are all apart of "opAns" as their own list.
optionBoxList.append(Options(["sewage, oil spills", "people swimming","people driving boats","climate change"]))
optionBoxList.append(Options(["carbon dioxide emission","summer season","moving closer to the sun","overpopulation"]))
optionBoxList.append(Options(["wind turbines, solar energy","burning coal","use plastic","fossil fuels"]))
optionBoxList.append(Options(["ice melting, rising temps", "more food will grow","less nasty weather","nothing bad will happen"]))
optionBoxList.append(Options(["One and a half acres", "Two acres","One acre","Half an acre"]))
optionBoxList.append(Options(["14 billion pounds", "7 billion pounds","20 billion pounds","10 billion pounds"]))
optionBoxList.append(Options(["Many plants will die in a few days", "Humans would die instantly","Everything would be on fire","Nothing will happen"]))
optionBoxList.append(Options(["They make the water harmful to animals", "They make water slippery","Nothing happens","We lose money"]))
optionBoxList.append(Options(["Hydro", "Coal","Gas","Oil"]))
optionBoxList.append(Options(["In 100 years", "In 250 years","In 75 years","In 175 years"]))

#this starts the gui after the program has read all the code
app.go()