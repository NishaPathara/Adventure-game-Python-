import time
import random
import string
import enum


class Color(enum.Enum):
    red = '\033[31m'
    green = '\033[32m'
    orange = '\033[33m'
    blue = '\033[34m'
    purple = '\033[35m'
    cyan = '\033[36m'
    lightgrey = '\033[37m'
    darkgrey = '\033[90m'
    lightred = '\033[91m'
    lightgreen = '\033[92m'
    yellow = '\033[93m'
    lightblue = '\033[94m'
    pink = '\033[95m'
    lightcyan = '\033[96m'

    @classmethod
    def get_color(cls):
        return random.choice([color.value for color in cls])


def typewriter_simulator(message_to_print):
    for char in message_to_print:
        print(char, end='')
        if char in string.punctuation:
            time.sleep(.5)
        time.sleep(.03)
    print(Color.get_color() + '')


def print_pause(message_to_print, delay=2):
    message = typewriter_simulator(message_to_print)
    time.sleep(delay)


def valid_input(prompt, options):
    while True:
        response = input(prompt).lower()
        if response in options:
            return response
        else:
            print_pause("Sorry, invalid input!\n")


def intro(monster):
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + monster + " is somewhere around "
                "here and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                " dagger.")


def field(monster, weapon, cave_visited_flag):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    while True:
        response1 = valid_input("What would you like to do?\nPlease"
                                " enter 1 or 2.\n", ['1', '2'])
        if response1 == '1':
            house(monster, weapon, cave_visited_flag)
        else:
            cave(monster, weapon, cave_visited_flag)
        break


def house(monster, weapon, cave_visited_flag):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door"
                " opens and out steps a " + monster + ".")
    print_pause("Eep! This is the " + monster + "'s house!")
    print_pause("The " + monster + " attacks you!")
    if cave_visited_flag == 0:
        print_pause("You feel a bit under-prepared for this,"
                    " what with only having a tiny dagger.")
    while True:
        response2 = valid_input("Would you like to (1) fight"
                                " or (2) run away?\n", ['1', '2'])
        if response2 == '1':
            fight(monster, weapon, cave_visited_flag)
            break
        else:
            runaway(monster, weapon, cave_visited_flag)
            break


def fight(monster, weapon, cave_visited_flag):
    if cave_visited_flag == 0:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + monster + ".")
        print_pause("You have been defeated!")
    else:
        print_pause("As the " + monster + " moves to attack,"
                    " you unsheath your new " + weapon + ".")
        print_pause("The " + weapon + " shines brightly in your "
                    "hand as you brace yourself for the attack")
        print_pause("But the " + monster + " takes one look at "
                    " your shiny new toy and runs away!")
        print_pause("You have rid the town of the "
                    + monster + ". You are victorious!")


def runaway(monster, weapon, cave_visited_flag):
    print_pause("You run back into the field. Luckily,"
                "you don't seem to have been followed.")
    field(monster, weapon, cave_visited_flag)


def cave(monster, weapon, cave_visited_flag):
    if cave_visited_flag == 0:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical " + weapon + "!")
        print_pause("You discard your silly old dagger and take the "
                    + weapon + " with you.")
        print_pause("You walk back out to the field.")
        cave_visited_flag = 1
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten all the good stuff."
                    "It's just an empty cave now.")
        print_pause("You walk back out to the field.")
    field(monster, weapon, cave_visited_flag)


def play_again():
    input_again = valid_input("Would you like to play again? (y/n)\n",
                              ['y', 'n'])
    if input_again == "y":
        print_pause("Excellent! Restarting the game ...\n")
    if input_again == 'n':
        print_pause("Thanks for playing! See you next time.\n")
        exit(0)


def play():
    cave_visited_flag = 0
    monster = random.choice(["Murlocs", "Reaper",
                             "Zinyak", "Brutalisk", "Straga"])
    weapon = random.choice(["Boomerang", "Halberd",
                            "Mattock", "Katana", "Jadewand"])
    intro(monster)
    field(monster, weapon, cave_visited_flag)


def game():
    while True:
        play()
        play_again()


if __name__ == '__main__':
    game()
