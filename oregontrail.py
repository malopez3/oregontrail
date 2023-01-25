#modeled after lesson from https://github.com/TEALSK12/2nd-semester-introduction-to-computer-science/blob/master/docs/units/3_unit/05_lesson/Unit_3_Project_Oregon_Trail_Starter_Code.py

import random
#colorama imported to change text colors
import colorama
colorama.init()

welcome = """
Welcome to the Oregon Trail! Set in the year 1850, the goal of the game is to travel
from Independence, Missouri to the Willamette Valley in Oregon, a 2000 mile journey. 
You will have 9 months from the start date to successfully complete your 
journey to Oregon. Each day you play in the game will cost you food and health. 
In order to successfully win the game, at least one person from your starting group 
must survive the journey to Oregon."""

#constant variables

#tracks numbers of days in each month
MONTHS_WITH_31_DAYS = [1,3,5,7,8,10,12]
MONTHS_WITH_30_DAYS = [4,6,9,11]
MONTHS_WITH_28_DAYS = [2]
MIN_MILES_PER_TRAVEL = 60
MAX_MILES_PER_TRAVEL = 100
MIN_DAYS_PER_TRAVEL = 3
MAX_DAYS_PER_TRAVEL = 7
TOTAL_MILES = 2000
MAX_HEALTH = 100
MIN_DAYS_PER_REST = 1
MAX_DAYS_PER_REST = 5

MIN_POUNDS_PER_HUNT = 5
MAX_POUNDS_PER_HUNT = 200
MIN_DAYS_PER_HUNT = 1
MAX_DAYS_PER_HUNT = 5

MIN_DAYS_LOST = 1
MAX_DAYS_LOST = 10

#random injury/death list
#injuries in this list have 0.1% chance of resulting in death and 5% chance of resulting in reduced health by 20

INJURY_LIST = ["Fever", "Dysentery", "Measles", "Cholera", "Typhoid", "Exhaustion", "Snakebite", "Broken leg", "Broken arm", 
"Drowning (survived)", "Food poisoning", "Bad cold", "Burns", "Broken arm", "Broken foot", "Broken hand", "Broken hip", 
"Broken leg", "Concussion", "Frostbite", "Infection", "Malaria", "Measles", "Pneumonia", "Scarlet Fever", "Smallpox", 
"Typhoid Fever", "Water Poisoning", "Accidental Gunshot", "Dehydration"]

FATAL_INJURY_LIST = ["Cholera", "Dysentery", "Typhoid", "Snakebite", "Drowning", "Malaria", "Rabies", "Scarlet Fever", "Smallpox",
"Typhoid Fever", "Accidental Gunshot"]

EVENT_LIST = ["Buffalo stampede", "Fire", "Theft", "Wagon accident"]

WEATHER_EVENT_LIST = ["Thunderstorm", "Fog", "Duststorm", "Hailstorm"]

#animals that you can hunt in the game

LARGE_ANIMAL_LIST = ["deer", "elk", "bear", "bison"]

SMALL_ANIMAL_LIST = ["squirrels", "rabbits"]

#at the beginning of the game you start with 0 miles traveled
milesTraveled = 0
#you begin with 500 pounds of food
food = 500
#health is at 100/100 at the beginning of the game
health = 100
day = 1
month = 4
year = 0
gameStatus = ''
command = ''
milesRemaining = TOTAL_MILES

def error():
    print("The command you entered is not valid, please try again with a new command.")
    print("You may type: 'travel', 'rest', 'hunt', 'status', or 'help'")

def travel():
    global milesTraveled
    global milesRemaining

    randomMilesTraveled = random.randint(MIN_MILES_PER_TRAVEL, MAX_MILES_PER_TRAVEL)
    milesTraveled += randomMilesTraveled
    
    milesRemaining = TOTAL_MILES - milesTraveled
    print(colorama.Back.GREEN + "TRAVEL")
    print(colorama.Back.RESET)

    print("You traveled " + str(randomMilesTraveled) + " miles for a total of " + str(milesTraveled) + " miles traveled.")
    print("You have " + str(milesRemaining) + " miles until you arrive in Oregon.")
    randomDaysTraveled = random.randint(MIN_DAYS_PER_TRAVEL, MAX_DAYS_PER_TRAVEL)
    print("You traveled " + str(randomDaysTraveled) + " days.")
    for day in range(randomDaysTraveled):
        addDay()

def rest():
    global health

    print(colorama.Back.GREEN + "REST")
    print(colorama.Back.RESET)

    if health < MAX_HEALTH:
        health += 15
        randomDaysResting = random.randint(MIN_DAYS_PER_REST, MAX_DAYS_PER_REST)

        for day in range(randomDaysResting):
            addDay()

        if health > MAX_HEALTH:
            health = MAX_HEALTH

        print("You rested for " + str(randomDaysResting) + " days and your health is " + str(health) + "/100")
    
    else:

        print("You are fully healed, you don't need to rest")


def hunt():
    #add what you got in the hunt
    global food

    global SMALL_ANIMAL_LIST
    global LARGE_ANIMAL_LIST

    print(colorama.Back.GREEN + "HUNT")
    print(colorama.Back.RESET)

    #add in randomizer for amount of food you can get
    randomPoundsHunting = random.randint(MIN_POUNDS_PER_HUNT, MAX_POUNDS_PER_HUNT)
    food += randomPoundsHunting

    #random number of days for hunting
    randomDaysHunting = random.randint(MIN_DAYS_PER_HUNT, MAX_DAYS_PER_HUNT)

    print("You spent " + str(randomDaysHunting) + " days hunting for food.")

    #animal hunted corresponds to number of pounds collected in the hunt
    if randomPoundsHunting <= 50:
        print("You collected " + str(randomPoundsHunting) + " pounds of food in your hunt from hunting " + random.choice(SMALL_ANIMAL_LIST) + ".")
    else:
        print("You collected " + str(randomPoundsHunting) + " pounds of food in your hunt from hunting " + random.choice(LARGE_ANIMAL_LIST) + ".")

    print("You now have " + str(food) + " total food in your inventory.")

    for day in range(randomDaysHunting):
        addDay()

def status():
    global year
    global food
    global health
    global FATAL_INJURY_LIST
    global INJURY_LIST
    global WEATHER_EVENT_LIST
    global EVENT_LIST


    if milesRemaining <= 0:
        win()
    #max time to finish the game
    #adjust based on the month that the user selected
    if year >= 1:
        print(colorama.Fore.RED + "YOU TOOK TOO LONG TO ARRIVE TO OREGON, THE GAME IS OVER")
        print(colorama.Fore.RESET)
        loss()
    elif health < 1:
        print(colorama.Fore.RED + "EVERYONE IN YOUR GROUP HAS DIED, THE GAME IS OVER")
        print(colorama.Fore.RESET)
        loss()
    elif food < 1:
        print(colorama.Fore.RED + "YOU RAN OUT OF FOOD AND STARVED TO DEATH, THE GAME IS OVER")
        print(colorama.Fore.RESET)
        loss()
        #SET HIGH PERCENTAGE TO TEST OUT
    elif random.random() >= 0.9995:
        #0.05% chance of suffering death injury
        print(colorama.Fore.RED + "YOU SUFFERED THE FOLLOWING INJURY AND DIED: " + random.choice(FATAL_INJURY_LIST))
        print(colorama.Fore.RESET)
        loss()
    elif random.random() >= 0.98:
        #2% chance at suffering an injury that reduces health
        print(colorama.Fore.RED + "YOU SUFFERED THE FOLLOWING INJURY, YOU SURVIVED BUT LOST 20 HEALTH: " + random.choice(INJURY_LIST))
        print(colorama.Fore.RESET)
        health -=20
    elif random.random() >= 0.98:
        #2% chance that there is a random event that causes loss in food
        print(colorama.Fore.RED + "THE FOLLOWING EVENT OCCURED RESULTING IN A LOSS OF 100 POUNDS OF FOOD: " + random.choice(EVENT_LIST))
        print(colorama.Fore.RESET)
        food -=100
    elif random.random() >= 0.98:
        #2% chance that there is a severe weather event that causes you to lose days
        randomDaysLost = random.randint(MIN_DAYS_LOST, MAX_DAYS_LOST)
        print(colorama.Fore.RED + "THE FOLLOWING SEVERE WEATHER EVENT OCCURRED, CAUSING YOUR GROUP TO LOSE " + str(randomDaysLost) + " DAYS OF TRAVEL: "
        + random.choice(WEATHER_EVENT_LIST))
        print(colorama.Fore.RESET)
        for day in range(randomDaysLost):
            addDay()

def check_status():
    global month
    global day
    global milesTraveled
    global health
    global food
    print(colorama.Back.GREEN + "STATUS")
    print(colorama.Back.RESET)
    print("Your health is " + str(health) + "/100.")
    print("You have " + str(food) + " total pounds of food.")
    print("You have " + str(milesRemaining) + " miles left to go until Oregon.")
    print()

    print("The current date is " + str(month) + "/" + str(day) + ".")

def win():
    global gameStatus
    print(colorama.Back.GREEN + "CONGRATULATIONS! You have made it to Oregon, you have won the game!!")
    print(colorama.Back.RESET)
    gameStatus = 'game over'
def loss():
    quit()

def quit():
    global gameStatus
    print("The game is now over.")
    gameStatus = 'game over'

def addDay():
    global day
    global food
    food -= 10
    global health
    if day == 0 or day == 7 or day == 14 or day == 21 or day == 28:
        health -= 10
    global month
    global year

    day+=1

    if day > 28 and month in MONTHS_WITH_28_DAYS:
        day = 1
        month += 1

    elif day > 30 and month in MONTHS_WITH_30_DAYS:
        day = 1
        month += 1

    elif day > 31 and month in MONTHS_WITH_31_DAYS:
        day = 1
        month += 1

    if month > 12:
        month = 1
        day = 1
        year = 1
    

#welcome user to the game
print(welcome)
print()

#Main game loop
while gameStatus != 'game over' and command != 'quit':
    
    #checks the status of the game to see if there is a win or a loss
    status()
    
    command = input("What would you like to do? You may type: 'travel', 'rest', 'hunt', 'status', 'help', or 'quit'\n")
    if command == 'travel':
        travel()
    elif command == 'rest':
        rest()
    elif command == 'hunt':
        hunt()
    elif command == 'status':
        #this tells the user what the current status is of the game
        check_status()
    elif command == 'help':
        help()
    elif command == 'quit':
        quit()
    else:
        error()