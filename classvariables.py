class Wolf:
# Class variables
    classification = "canine"
    habitat = "forest"
    is_sleeping = False
    # Constructor method with instance variables name and age
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # method to wake up wolf (self needs to be passed as argument so
    # that all of the p

        self.is_sleeping = False
# method to put wolf to sleep
    def sleep(self):
        self.is_sleeping = True
# method that returns the sleep state of the wolf
    def show_sleep_state(self):
        if self.is_sleeping == False:
            return self.name + " is awake"
        else:
            return self.name + " is sleeping"
def main():
# initialising a wolf object and printing the initial sleep
# state which is awake
    silver_tooth = Wolf("Silver Tooth", 6)
    print(silver_tooth.show_sleep_state())
# changing sleep state to sleeping and then printing that state
    silver_tooth.sleep()
    print(silver_tooth.show_sleep_state())
# running main method
main()