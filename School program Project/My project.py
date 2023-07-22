import datetime


class SchoolProgram:
    def __init__(self, breakfast, lessons, lunch, skills, play):
        self.breakfast = breakfast
        self.lessons = lessons
        self.lunch = lunch
        self.skills = skills
        self.play = play

    def schedule(self, TimeofDay):
        while True:
            TimeofDay = input("Enter Breakfast, Lessons, Lunch,Lunch Break, Skills, Knock off: ").capitalize()
            TimeofDay = TimeofDay.strip()
            if "Breakfast" in TimeofDay:
                Time1 = datetime.time(8, 0)
                Time2 = datetime.time(8, 30)
                print(f"Breakfast starts at {Time1},Enjoy your breakfast and clean up by {Time2}")
                print("")
            elif "Lessons" in TimeofDay:
                Time2 = datetime.time(8, 30)
                Time3 = datetime.time(12, 00)
                print(f"Lessons Begin at {Time2} and End at {Time3}")
                print("")

            elif "Lunch" in TimeofDay:
                Time3 = datetime.time(12, 00)
                Time4 = datetime.time(12, 30)
                print(f"It's {Time3} ,Enjoy your lunch and clean up by {Time4}")
                print("")

            elif "Lunch Break" in TimeofDay:
                Time4 = datetime.time(12, 30)
                Time5 = datetime.time(13, 0)
                print(f"Lunch Break begins at {Time4}, have fun and remember to be in class at {Time5}")
                print("")

            elif "Skills" in TimeofDay:
                Time5 = datetime.time(13, 0)
                Time6 = datetime.time(15, 00)
                print(f"{Time5} and {Time6} is the time to practise and put your knowledge to the test")
                print("")

            elif "Knock off" in TimeofDay:
                Time6 = datetime.time(15, 00)
                print(f"It's {Time6}  it's time to knock off")
                break

    def foods(self, Breakfast):
        while True:

            choice = input("Enter select display or exit: ").capitalize()
            if "select" in choice:
                available_foods = ["Bread", "Eggs", "Blueberries", "Water", "Avocados", "Salami", "Oats", "Milk"]
                print(available_foods)
                your_choice = input("Choose from the list above:   ") + "\n "

                with open("student's food.text", "r") as file:
                    your_breakfast = file.readlines()
                your_breakfast.append(your_choice)

                with open("student's food.text", 'w') as file:
                    file.writelines(your_breakfast)
            elif "display" in choice:
                with open("student's food.text", "r") as file:
                    your_breakfast = file.readlines()
                for index, item in enumerate(your_breakfast):
                    row = f"{index + 1}-{item}".strip("\n")  # strip() was used to remove the white space between items
                    print(row)
            elif "exit" in choice:
                break


program = SchoolProgram("Eat and Enjoy", "Learning is fun", "Eat and Enjoy", "Reflect and Practise", "Run and have Fun")
print(program)
# print(program.foods("Breakfast"))
print(program.schedule("TimeofDay"))
