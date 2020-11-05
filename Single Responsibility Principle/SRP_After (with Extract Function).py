# Print names
def Print_Names(person):
    print("First name is: %s"%(person.first_name))
    print("Second name is: %s"%(person.surname_name))

''' Class that declares person instance '''
class Person():
    ''' The Person class object '''

    # Variables to be identical when instanced
    listOfAwards = []

    # Variables to be defined when instanced
    def __init__(self, first_name, surname_name):
        self.first_name = first_name
        self.surname_name = surname_name

    # __str__ function
    def __str__(self):
        return "BookPublisher(first_name=%s, surname_name=%s)"%(self.first_name, self.surname_name)

    # __repr__ function
    def __repr__(self):
        return "BookPublisher(first_name=%s, surname_name=%s)"%(self.first_name, self.surname_name)

    # Extract function
    def Extract(self):
        print("Time to print the names!")
        Print_Names(self)

''' Class that declares award instance '''
class Award():
    ''' The Award class object '''

    # Variables to be defined when instanced
    def __init__(self, award_name):
        self.award_name = award_name

    # __str__ function
    def __str__(self):
        return "BookPublisher(award_name=%s)"%(self.award_name)

    # __repr__ function
    def __repr__(self):
        return "BookPublisher(award_name=%s)"%(self.award_name)

# Add the award to the person's list
def add_to_awards_list(person, award):
    ''' Adds award to person's personal list '''
    print("'%s' added to %s's list."%(award.award_name, person.first_name))
    person.listOfAwards.append(award)

# Create instances
person1 = Person("Adam", "Duncanson")
award1 = Award("Python Award!")

# Add award to person's list
add_to_awards_list(person1, award1)

# Call Extract function
person1.Extract()