# this is a adventure game program
# G.Jayanth

import time
import random


def print_t(message):
    print(message)
    time.sleep(1.5)


def win():
    print("you have won the match GREAT!")


def lose():
    print("SORRY! you lost the match")

def restart_game():
    y = input("Do you want to play again(Y/N)")
    if y == "Y" or y == "y":
        game_intro()
    elif y == "N" or y == "n":
        print("THANKYOU - GOOD BYE")
    else:
        restart_game()    


def nitrocar():
    colour = ("red", "green", "blue", "yellow")
    car = random.choice(colour)
    print_t("you have selected "+car+" nitrocar for this game")
    directions = ("right", "left")
    dire = random.choice(directions)
    if dire == "right":
        print("you going to right.")
    while True:
        race = input("Do you want to race your car(Y/N)")
        if race == "Y" or race == "y":
            print("Over speed met with an accident")
            lose()
            x = input("Do you want to play again(Y/N)")
            if x == "Y" or x == "y":
                game_intro()
            else:
                print("THANK YOU - GOOD BYE")
            break

        elif race == "N" or race == "n":
            print("going slow good choice")
            win()
            y = input("Do you want to play again(Y/N)")
            if y == "Y" or y == "y":
                game_intro()
            else:
                print("THANKYOU - GOOD BYE")
            break
        else:
            print("please enter correct input.")

    while True:
        print("1.Go straight\n2.Go back")
        move = input("choose one direction from the above:   ")
        if move == "1":
            print_t("you wil reach your destination")
            win()
            y = input("Do you want to play again(Y/N)")
            if y == "Y" or y == "y":
                game_intro()
            else:
                print("THANKYOU - GOOD BYE")
            break
        elif move == "2":
            print("Your car has been damaged as you have met with an accident")
            lose()
            y = input("Do you want to play again(Y/N)")
            if y == "Y" or y == "y":
                game_intro()
            else:
                print("THANKYOU - GOOD BYE")
            break
        else:
            print("please enter correct input.")


def daves():
    print("which action you want to perform?\n1.jump\n2.run\n3.stop\n4.fight")
    movement = input("Enter any of the above choice:   ")
    if movement == "1":
        print("you are going to perform jump and you stay at same place")
        lose()
        y = input("Do you want to play again(Y/N)")
        if y == "Y" or y == "y":
            game_intro()
        else:
            print("THANKYOU - GOOD BYE")

    elif movement == "2":
        print("you are going to run until your last destination")
        win()
        y = input("Do you want to play again(Y/N)")
        if y == "Y" or y == "y":
            game_intro()
        else:
            print("THANKYOU - GOOD BYE")
    elif movement == "3":
        print("you going to perform the stop action")
        lose()
        y = input("Do you want to play again(Y/N)")
        if y == "Y" or y == "y":
            game_intro()
        else:
            print("THANKYOU - GOOD BYE")
    elif movement == "4":
        print("you are performing your fight option")
        win()
        y = input("Do you want to play again(Y/N)")
        if y == "Y" or y == "y":
            game_intro()
        else:
            print("THANKYOU - GOOD BYE")
    else:
        print("invalid input please try again")
        game_intro()


def game_intro():
    print_t("Hello! I am gamer, the gamer Bot.")
    print_t("Today we have two games available.")
    print("1.nitrocar with 3d effects and motion sensors.")
    print("2.daves with 2d effects.")
    response = input("Choose a number to play the game:  ")
    if response == "1":
        nitrocar()

    elif response == "2":
        daves()

    else:
        print("invalid response TRY-AGAIN")
        game_intro()


game_intro()
