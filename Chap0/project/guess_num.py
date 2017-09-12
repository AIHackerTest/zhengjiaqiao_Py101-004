# generate a number
import random
correct_num = random.randint(0,20)

print("""
let's take a guess,How old do you think I am?
if you guess it correctly, I will give you a little gift.
remember, you have only 10 chances!
""")
n=1
while n <= 10:
    # player input number
    player_input = input("please input a number >>")
    n= n + 1
    left_times = 10 - n + 1

    # make sure player inputed a number
    if player_input.isdigit() == True:
        guess_num = int(player_input)
        # check the number
        if guess_num < correct_num :
            print("I konw that I look so young, but I am not kid! try again!")
        elif guess_num > correct_num:
            print("Do I look so old? you'd better revision your answer before I beat you up!")
        elif guess_num == guess_num:
            print("finally! I thought that you would never figur it out,this is your gift, you win!")
            exit(0)
    else:
        print("you should input a number!")

    print("you have %d times left" % left_times)
