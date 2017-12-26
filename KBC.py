# My KBC
# This is Game like KBC, I took all thee question from one of those episode.
# Play this python game
# Hope you will enjoy
# Day: Friday; Dec 22, 2K17
# Programmer : Vinod Rathore

print """ Namaskar, Deviyo or Sajjano. \nI Vinod Rathore, Welcomes all of you in this game. Firstly, I am making aware you about the rule of the game"\n## Rules :::::::::::::\n\t # You should reply your answer either 'A/B/C/D' or 'a/b/c/d', No other answer will be acceptable.\n\t # If you will misbehave then I shall terminate the game anytime. \n\t #You have 2 lifeline :\n\t\t 1. Double Dip \n\t\t 2. Fifty-Fifty(50-50). \n\t * If you use double dip then you are eligible to answer two times and if you use 50-50, we will remove two answers from the option. \n\t * You are eligible to use lifeline only if you will reach on 1st stage.\n\n ::::::::::::  Hope, you will enjoy the Game :::::::::::::"""
print "\n Now the game is starting \n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::"

wrong_count = 0

# First Question
def first_question() :
    global wrong_count
    while wrong_count < 3  :
        print "First question for Rs. 10000 is : \n\n1. Which of these words means 'revolution' in Arabic?" 
        print "\tA. Isteqbaal\tB. Intikhaab\tC. Inquilab\tD. Intequam"
        answer = raw_input("> ")
        if answer == 'C' or answer =='c' :
            print "Sahi Jawab, You won Rs. 10000."
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            second_question()
        elif answer == 'a' or answer =='b' or answer =='d' or answer =='A' or answer =='B' or answer =='D' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()

# Second Question            
def second_question() :
    global wrong_count
    while wrong_count < 3  :
        print "Second question for Rs. 20000 is : \n\n2. In cricket, which of these modes of dismissals always involves the wicket-keeper ?" 
        print "\tA. LBW\tB. Caught and Bowled\tC. Run Out\tD. Stumping"
        answer = raw_input("> ")
        if answer == 'D' or answer =='d' :
            print "Nice Played, You won Rs. 20000."
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            third_question()
        elif answer == 'a' or answer =='b' or answer =='c' or answer =='A' or answer =='B' or answer =='C' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()

# Third Question            
def third_question() :
    global wrong_count
    while wrong_count < 3  :
        print "Third question for Rs. 40000 is : \n\n3. Which scientist has been named for the Bharat Ratna in 2013? "
        print "\tA. Prof C N R Rao\tB. Pro U R Rao\tC. Prof Yash Pal\tD. Dr K Radhakrishnan"
        answer = raw_input("> ")
        if answer == 'a' or answer =='A' :
            print "Nice Played, You won Rs. 40000."
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            fourth_question()
        elif answer == 'b' or answer =='c' or answer =='d' or answer =='B' or answer =='C' or answer =='D' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()

# Fourth Question
def fourth_question() :
    global wrong_count
    while wrong_count < 3  :
        print "Fourth question for Rs. 80000 is : \n\n4. Which of these is the administrative head of a district in India ? "
        print "\tA. DM\tB. DCP\tC. DSP\tD. DIG"
        answer = raw_input("> ")
        if answer == 'a' or answer =='A' :
            print "Nice Played, You won Rs. 80000."
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            fifth_question()
        elif answer == 'b' or answer =='c' or answer =='d' or answer =='B' or answer =='C' or answer =='D' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()

# Fifth Question
def fifth_question() :
    global wrong_count
    while wrong_count < 3  :
        print "Fifth question for Rs. 160000 is : \n\n5. Which scholar started the Mohammedan Anglo Oriental College which later became the Aligarh Muslim University ? "
        print "\tA. Syed Ahmad Khan\tB. Muhammad Iqbal\tC. Maulana Mohomed Ali\tD. Dr Zakir Hussain"
        answer = raw_input("> ")
        if answer == 'a' or answer =='A' :
            print "Nice Played, You won Rs. 160000."
            print "Congrats, Now this 1.6 Lac are your's. and also after this you are having lifelines according to rule of game."
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            sixth_question()
        elif answer =='b' or answer =='c' or answer =='d' or answer =='B' or answer =='C' or answer =='D' :
            print "Opps! 'Galat jawab' But You Won 1.6 Lac"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()

# Sixth Question
def sixth_question() :
    global wrong_count
    while wrong_count < 3  :
        print "Sixth question for Rs. 320000 is : \n\n6. Which is the oldest mountain range in India ?"
        print "\tA. Nilgiris \tB. Aravalli \tC. Vindhya \tD. Satpura"
        answer = raw_input("> ")
        if answer == 'B' or answer =='b' :
            print "Nice Played, You won Rs. 320000."
            
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            seventh_question()
        elif answer == 'a' or answer =='c' or answer =='d' or answer =='A' or answer =='C' or answer =='D' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()
            
# Seventh Question
def seventh_question() :
    global wrong_count
    while wrong_count < 3  :
        print "Seventh question for Rs. 640000 is : \n\n7. In October 2013, which actress was honored by the British House of Commons ?"
        print "\tA. Vidya Balan \tB. Madhuri Dixit \tC. Sonakshi Sinha \tD. Kareena Kapoor"
        answer = raw_input("> ")
        if answer == 'D' or answer =='d' :
            print "Nice Played, You won Rs. 320000."
            
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            eighth_question()
        elif answer == 'a' or answer =='b' or answer =='c' or answer =='A' or answer =='B' or answer =='C' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()
            
# Eighth Question
def eighth_question() :
    global wrong_count
    while wrong_count < 3  :
        print "Eighth question for Rs. 1250000 is : \n\n8. IWhat was the first Grand Slam tennis title won by Sania Mirza ?"
        print "\tA. US Open \tB. Australian Open \tC. Wimbledon \tD. French Open"
        answer = raw_input("> ")
        if answer == 'B' or answer =='b' :
            print "Nice Played, You won Rs. 1250000."
            
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            ninth_question()
        elif answer == 'a' or answer =='c' or answer =='d' or answer =='A' or answer =='C' or answer =='D' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()
            
# Ninth Question
def ninth_question() :
    global wrong_count
    while wrong_count < 3  :
        print "Eighth question for Rs. 2500000 is : \n\n9. Which ruler of the Delhi Sultanate was called 'Lakh Baksh' for his generosity ?"
        print "\tA. Firoz Tughlaq \tB. Alauddin Khilji \tC. Qutb-ud-din Aibak \tD. Bahlul Lodi"
        answer = raw_input("> ")
        if answer == 'C' or answer =='c' :
            print "Nice Played, You won Rs. 2500000."
            
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            tenth_question()
        elif answer == 'a' or answer =='b' or answer =='d' or answer =='A' or answer =='B' or answer =='D' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()

# Tenth Question
def tenth_question() :
    global wrong_count
    while wrong_count < 3  :
        print "Tenth question for Rs. 5000000 is : \n\n10. The president of which African country was conferred the Indira Gandhi Peace Prize in September 2013 ?"
        print "\tA. Nigeria \tB. Kenya \tC. Ethiopia \tD. Liberia"
        answer = raw_input("> ")
        if answer == 'D' or answer =='d' :
            print "Nice Played, You won Rs. 5000000."
            
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            eleventh_question()
        elif answer == 'a' or answer =='b' or answer =='c' or answer =='A' or answer =='B' or answer =='C' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()

# Eleventh Question
def eleventh_question() :
    global wrong_count
    while wrong_count < 3  :
        print "Eleventh question for Rs. 10000000 is : \n\n11. Who is the first Indian Women to conquer the highest peak of all seven continent ?"
        print "\tA. Bachendri Pal \tB. Santosh Yadav \tC. Premlata Agrawal \tD. Sucheta Kandethankar"
        answer = raw_input("> ")
        if answer == 'c' or answer =='C' :
            print "Nice Played, You won Rs. 10000000."
            
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            twelfth_question()
        elif answer == 'a' or answer =='b' or answer =='d' or answer =='A' or answer =='B' or answer =='D' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()
# Twelfth Question
def twelfth_question() :
    global wrong_count
    while wrong_count < 3  :
        print "Twelfth question for Rs. 30000000 is : \n\n12. In Which theatre was 'Raja Harishchandra' , India's first feature film, commercially released 100 years ago on 3rd May ?"
        print "\tA. Coronation Cinematograph \tB. Olympia theatre \tC. Maratha Mandir \tD. Edward Theatre"
        answer = raw_input("> ")
        if answer == 'a' or answer =='A' :
            print "Nice Played, You won Rs. 30000000."
            
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            last_question()
        elif answer == 'b' or answer =='c' or answer =='d' or answer =='B' or answer =='C' or answer =='D' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()
# Last Question
def last_question() :
    global wrong_count
    while wrong_count < 3  :
        print "This is the last question for Rs. 50000000 is : \n\n13. Who presented the National flag to the constituent Assembly on 14 August 1947 on behalf of the Women of India ?"
        print "\tA. Sarojini Naidu \tB. Vijay laxmi Pandit \tC. Laxmi Sehgal \tD. Hansa Mehta"
        answer = raw_input("> ")
        if answer == 'd' or answer =='D' :
            print "Cheers..., You won Rs. 50000000."
            
            print ":::::::::::::::::::::::::::::::::::::::::::::::::::"
            winning_speach()
        elif answer == 'a' or answer =='b' or answer =='c' or answer =='A' or answer =='B' or answer =='C' :
            print "Sorry! 'Galat jawab' you lost the game"
            lost_game()
            exit(0)
        else :
            wrong_count += 1
            elinimination()



def lost_game() :
    print "Better luck next time"
    
def elinimination() :
    if wrong_count < 3 :
                print "Please provide answer in correct manner else we will eliminate you"
    else :
        print "You eliminited"
        
def winning_speach() :
    print  """ Wow!!!!! You are now the owner of Rs. 5 Crore, You played incredibly. Everyone who is present here definiatly enjoyed your journey of this game. We wish for your bright future."""
    exit(0)
first_question()

