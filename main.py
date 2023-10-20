import random

class Student:
    def __init__(self, name, money=100):
        self.name = name
        self.money = money
        self.knowledge = 0
        self.happiness = 100

    def work(self):
        earnings = random.randint(10, 50)
        self.money += earnings
        self.happiness += 10
        print(f"{self.name} пішов на роботу і заробив {earnings} грошей.")

    def study(self):
        if self.money >= 20:
            self.money -= 20
            self.knowledge += 10
            self.happiness -= 5
            print(f"{self.name} витратив 20 грошей на навчання і збільшив свої знання.")
        else:
            print(f"{self.name} не має грошей для навчання!")

    def have_fun(self):
        self.money -= 30
        self.happiness += 20
        print(f"{self.name} витратив 30 грошей на відпочинок і покращив свій настрій.")

    def year_in_college(self):
        for _ in range(365):
            action = random.choice(["work", "study", "have_fun"])
            if action == "work":
                self.work()
            elif action == "study":
                self.study()
            else:
                self.have_fun()

            if self.money < 10:
                print(f"{self.name} залишилось дуже мало грошей! Він пішов на роботу, щоб заробити більше.")
                self.work()

            if self.knowledge < 50:
                print(f"{self.name} вирішив почати вчитися, бо йому потрібні більше знань.")
                self.study()

            if self.happiness < 30:
                print(f"{self.name} дуже нещасливий! Він вирішив піти відпочивати.")
                self.have_fun()

            print(f"День {_ + 1}: Гроші: {self.money}, Знання: {self.knowledge}, Настрій: {self.happiness}")

        print(f"{self.name} завершив рік у коледжі!")

student1 = Student("Роман")
student1.year_in_college()
