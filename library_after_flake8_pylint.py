''' Class that declares library instance details '''
class Library():
    ''' The Library class object '''
    # Variables to be identical when instanced
    listOfClients = []
    listOfEmployees = []
    listOfBooks = []

    # Variables to be defined when instanced
    def __init__(
            self, library_owner=None,
            library_coowner=None, library_name=None):
        # If the library_owner isn't populated, then use the default value
        if library_owner is None:
            self.library_owner = "Dylan Scott"
        else:
            self.library_owner = library_owner

        # If the library_coowner isn't populated, then use the default value
        if library_coowner is None:
            self.library_coowner = ""
        else:
            self.library_coowner = library_coowner

        # If the library_name isn't populated, then use the default value
        if library_name is None:
            self.library_name = "Durham Books!"
        else:
            self.library_name = library_name

    # __str__ function: returns the below string when the
    # object itself is passed into the 'print' function
    def __str__(self):
        return "This is the 'BookPublisher' class"

    # __repr__ function: returns the below string when
    # the object itself is passed is called by itself
    def __repr__(self):
        return "BookPublisher()"

    def print_the_owners(self):
        ''' Prints the owner(s) of the Library '''
        if self.library_coowner == "":
            print("The owner of '" + self.library_name +
                  "' is " + self.library_owner + ".")
        else:
            print("The owners of '" + self.library_name + "' are " +
                  self.library_owner + " and " + self.library_coowner + ".")

    def generate_list_of_client(self):
        ''' Print out a list of all clients of the library '''
        print("List of all clients:")
        client_list = list(dict.fromkeys(self.listOfClients))
        for client in client_list:
            print("  " + client.fullName)

    def generate_list_of_employees(self):
        ''' Print out a list of all employees of the library '''
        print("List of all employees:")
        employee_list = list(dict.fromkeys(self.listOfEmployees))
        for employee in employee_list:
            print("  " + employee.fullName)

    def generate_list_of_books(self):
        ''' Print out a list of all books in the library '''
        print("List of all books:")
        book_list = list(dict.fromkeys(self.listOfBooks))
        for book in book_list:
            print("  " + book.title)
