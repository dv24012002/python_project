print("Let's Start KBC Game.....")
Question_Intro = ["Question 1 for Rs. 1000 is.........",
"Question 2 for Rs. 2000 is.....",
"Question 3 for Rs. 3000 is.........",
"Question 4 for Rs. 4000 is........."
]
Questions = [
    "Who is the Father of Computer ? \n0.Charles Babbage     1.Guido van Russen \n2.Archimedes          3.Benjamin Franklin",
    "what is the name of india's first supercomputer ?\n0.PARAM-Siddhi      1.Fugaku\n2.LUMI        3.Param 8000",
    "In a computer, most processing takes place in _______?\n0.joystick     1.Monitor\n2.CPU        3.Router",
    "Scientific Name of Computer?\n0.Comet      1.Alpha\n2.Cobalt       3.Sillico sapiens"
]
answers = [["Charles Babbage","Guido van Russen","Archimedes","Benjamin Franklin"],
["PARAM-Siddhi","Fugaku","LUMI","Param 8000"],
["joystick","Monitor","CPU","Router"],
["Comet","Alpha","Cobalt","Sillico sapiens"]]
answer = ["Charles Babbage","Param 8000","CPU","Sillico sapiens"]
i = 0
rupees_won = 0
r = 1
while(i<len(Question_Intro)):
    print(Question_Intro[i])
    print(Questions[i])
    ans = int(input("Answer would be : "))

    if(answers[i][ans] == answer[i]):
        rupees_won += r*1000
        print("You've won {} rupees".format(rupees_won))
    else:
        print("Sorry Wrong Answer....you are out....")
        break
    i += 1
    r += 1
print("You're going home with your winning rupees of {}".format(rupees_won))

