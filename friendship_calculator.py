def friendship_calculator(name1,name2):
    name1,name2=name1.lower().strip(), name2.lower().strip()
    score=0
    shared_letter=set(name1)&set(name2)
    vowels=set('aeiou')
    score+=len(shared_letter)*5
    score+=len(vowels&shared_letter)*10
    return min(score,100)
def run_friendship_calculator():
    print("💖Friendship compatibility calculator")
    name1= input("Enter your name: ")
    name2= input("Enter your friend's name: ")
    score=friendship_calculator(name1,name2)
    print(f"\n {score}")
run_friendship_calculator()

