def play_game(): 
    question_list=[["1. _____ is capital of India","2. _____ is Tony stark's real name","3. _____ player has 5 ballon D'ors in soccer","4. _____ is brain of computer "]
                   ,["1. HTML stands for _____ ","2. In _____ year world war II ended", "3. Silicon valley is situated in _____", "4. _____ eggs are there in a dozen"]
                   ,["1. Neutron was discovered by _____", "2. _____ is the only mammal that cannot jump.", "3. _____ is the name for brain cells.", "4. spaceX is owned by _____"]]#this is list of beginner level questions saved in question_list1
    i=0
    j=0
    for question in question_list: #this for loop will print 1 question at a time from question_list1 
        print question_list[k][i]
        answer=raw_input("enter your answer ").lower() #user is asked to enter his answer for the printed question
        answer_list=[["delhi","robert dowrey jr.","lionel messi","cpu"],
                     ["hyper text markup language","1945","california","12"],
                     ["chadwick","elephant","neurons","elon musk"]] #this is the answer list containing answers to corresponding questions
        while answer!=answer_list[k][j]: #while loop will check that if correct answer is equal to correct answer in answer list 
              answer=raw_input("your answer din't match,enter again! ")#if answer is wrong then user is prompted to answer again 
        solution=question_list[k][i].replace("_____",answer)#replace method is used to replace _____ with correct answer and it is stored in a variable solution 
        print solution
        i+=1 #incrementing i
        j+=1 #incrementing j
      
def play_again():
    
     print  "Do you want to play again?"
     
     again=raw_input("enter yes or no ")# taking input from user wheather he wants to play again or not
     while again!="yes":
         again=raw_input("something got wrong enter again ")# taking input from user wheather he wants to play again or not
     
     print "1. beginner              difficulty level-> *"
     print "2. intermediate          difficulty level-> **"
     print "3. hard                  difficulty level-> ***"
     print "choose your level"
     level_list=["beginner","intermediate","hard","expert"]
     level=raw_input("Enter level you want to play.")#level takes the input of difficulty level you will enter
     k=0
     for levels in level_list:
         if level==level_list[k]:
            play_game()
            play_again()
         k+=1
     else:
          print "\t\t\t\tthankyou for playing"



print "                                                                    Welcome to the quiz"
print "         levels to choose:" #choose a level beginner,intermediate or hard
print "1. beginner              difficulty level-> *"
print "2. intermediate          difficulty level-> **"
print "3. hard                  difficulty level-> ***" 
level_list=["beginner","intermediate","hard","expert"]
level=raw_input("choose your level")# level takes the input of difficulty level you will enter
k=0
for levels in level_list:
    if level==level_list[k]:
       play_game()
       play_again()
    k+=1

