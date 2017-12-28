# My KBC
# This is Game like KBC, I took all thee question from one of those episode.
# Play this python game
# Hope you will enjoy
# Day: Friday; Dec 22, 2K17
# Programmer : Vinod Rathore

import b
import random
print b.question_list[0]
print b.option_list[0]
wrong_count = 0
dd_count = 0
question_no = 1
answer = 'A'
ff_count = 0
# Question
def question() :
    global wrong_count
    global question_no
    global answer
    while wrong_count < 3  :
        print b.option_list[0],'\n'
        print  b.question_list[question_no]
        print b.option_list[question_no]
        print b.option_list[0],'\n'
        answer = raw_input("> ")
        check_ans()

def check_ans() :
    global question_no
    global answer
    global wrong_count
    quote_var = random.randint(0,4)
    
    right_ans = answer == b.ans_case1[question_no] or answer == b.ans_case1[question_no]
    
    wrong_ans = answer in b.ans_case3 and not (answer == b.ans_case1[question_no] or answer == b.ans_case1[question_no]) 
    
    quit = (answer == 'quit' or answer == 'Quit') and  question_no >=5
    
    dd_check = answer == 'DD' or answer == 'dd'
    ff_check = answer == 'ff' or answer == 'FF'
    if right_ans :
        if question_no ==13 :
            print b.quotes[5]
            exit(0)
        else :
            print b.quotes[quote_var] , b.prize[question_no]
            question_no += 1
            question()
    elif wrong_ans :
         print "Sorry! 'Galat jawab' you lost the game"
         lost_game()
    elif quit :
        print "Allright, You quit the game, but you was palying nicely . Now you won Rs %d in this game" % (b.prize[question_no])
        exit(0)
    elif dd_check :
        double_deep()
    elif ff_check :
        fifty_fifty()
    else :
        wrong_count += 1
        elinimination()

def double_deep() :
    global question_no
    global wrong_count
    global answer
    global dd_count
    dd_answer = 'a'
    dd_right_ans = dd_answer == b.ans_case1[question_no] or dd_answer == b.ans_case1[question_no]
    if dd_count < 1 and question_no <= 5 :
        print "You can not use this life line now, It can be usable after 5th question."
        wrong_count += 1
        elinimination()
    elif dd_count < 1 and question_no > 5 :
        dd_count = dd_count + 1
        dd_answer = raw_input("> ")
        if dd_right_ans :
            question()
        else :
            print b.option_list[0]
            print "This is your last chance to gave correct answer."
            answer = raw_input("> ")
            check_ans()        
    else :
        print b.option_list[0]
        print "You already used Double Deep lifeline, This will consider as missbehave"
        wrong_count += 1
        elinimination()

def fifty_fifty() :
    global question_no
    global wrong_count
    global answer
    global ff_count
    if ff_count < 1 and question_no <= 5 :
        print "You can not use this life line now, It can be usable after 5th question."
        wrong_count += 1
        elinimination()
    elif ff_count < 1 and question_no > 5 :
        ff_count = ff_count + 1
        print "Great You are using 50-50 life line now and we are going to remove two options"
        print b.option_list[0]
        print  b.question_list[question_no]
        print b.ff_option_list[question_no]
        print b.option_list[0]
        answer = raw_input("> ")
        check_ans()
    else :
        print b.option_list[0]
        print "You already used Fifty Fifty lifeline, This will consider as missbehave"
        wrong_count += 1
        elinimination()

def lost_game() :
    print b.option_list[0]
    print "\n\t\tBetter luck next time"
    print b.option_list[0]
    exit(0)
    
def elinimination() :
    if wrong_count < 3 :
        print "Please provide answer in correct manner else we will eliminate you"
    else :
        print b.option_list[0]
        print "\n\t\t\tYou eliminited"
        print b.option_list[0]
       
question()

