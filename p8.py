def Score(i,ans,s):
    if (ans==q[i]):
        print("="*60)
        print("Correct Answer !!!    +1 Point")
        return (s+1)
    else:
        print("="*60)
        print("Wrong Answer !!!    +0 Point")
        return s

def Remark(s):
    if s==5:
        print("Outstanding")
    if s==4:
        print("Excellent")
    if s==3:
        print("Good")
    if s==2:
        print("Read more to score more")
    if s==1:
        print("Needs to take interest")
    if s==0:
        print("General knowledge will always help you. Take it seriously.")

import random
q1=''' '''
q2='''b '''
q3='''c '''
q4='''d '''
q5='''e '''
q={q1:'a',q2:'a',q3:'a',q4:'a',q5:'a'}
name=input("Enter your name    ->    ")
print("="*60)
while True:
    p=input('''Enter "play" to play Quiz
Enter "quit" to exit    ->    ''')
    if p!="play" and q!="quit":
        print("Sorry ! Invalid Choice. Please try again")
        print("="*60)
    if p=="quit":
        print("Ok ! See you next time",name, "!")
        print("="*60)
        break
    if p=="play":
        print(name,", Welcome to this MCQ Quiz")
        print("="*60)
        print()
        l1=list(q.items())
        random.shuffle(l1)
        d1=dict(l1)
        qno=1
        s=0
        for i in d1:
            print("Question no. -",qno)
            print("-"*16)
            qno=qno+1
            print(i)
            print("="*60)
            while True:
                a=input('''Do you want to skip this question ? "yes"/"no"    ->    ''')
                if a!="yes" and a!="no":
                    print("Sorry ! Invalid Choice. Please try again")
                    print("="*60)
                    continue
                else:
                    break
            if qno<6 and a=="yes":
                while True:
                    h=input('''Do you want to continue playing ?
Enter yes/no    ->    ''')
                    if h!="yes" and h!="no":
                        print("Sorry ! Invalid Choice. Please try again")
                        print("="*60)
                        continue
                    else:
                        break
                if h=="yes":
                    print("="*60)
                    print(name,"your current score is:",s)
                    print("="*60)
                if h=="no":
                    print("="*60)
                    print("Final Score:",s)
                    break
            if a=="no":
                while True:
                    ans=input("Enter your option -a/b/c/d-  ->   ")
                    if ans!="a" and ans!="b" and ans!="c" and ans!="d":
                        print("Sorry ! Invalid Choice. Please try again")
                        print("="*60)
                        continue
                    else:
                        break
                s=Score(i,ans,s)
                print("="*60)
                print(name, "your current score is: ",s)
                print("="*60)
        print("Remarks :", end=' ')
        Remark(s)
        break
    
