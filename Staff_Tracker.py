
#this is a change

class Employee:
    """Class defining the employess attributes and functions"""
    ID = None
    Name = None
    Positions = []
    Max_Hours = None
    Pay_Rate = None
    Est_Week_hours = None
    
    def set_name(self, name):
        self.Name = name
    
    def set_id(self, id):
        self.ID = id
    
    def add_position(self, position):
        self.Positions.append(position)
    
    def remove_position(self, position):
        self.Positions = filter(lambda a: a != position, self.Positions)
        
    def set_max_hours(self, max_hours):
        self.Max_Hours = max_hours
        
    def set_pay_rate(self, pay_rate):
        self.Pay_Rate = pay_rate
        
class Staff:
    '''Manages the employees list and ID numbers'''
    
    Emps = None         #Dictionary containing employee ID numbers and objects
    ID = None           #Employee ID
    Name = None         #Employee Name 
    def __init__(self):
        '''Emps is a dictionary who's items are a Key which is the employee ID, and a
        value which is the employee object'''
        self.Emps = {}
        self.ID = 100
        self.Name = None
    
    def add_employee(self):
        '''Checks for next available ID then asks 
        User to input employee name. Adds the ID and new employee
        object to the Emps dictionary.'''
        #get new ID
        id = self.get_available_id()
        
        #get user input
        name = raw_input('Enter Employee Name: ') 
        
        #instanciate new employee object
        self.Emps[id] = Employee()
        self.Emps[id].set_id(id)
        self.Emps[id].set_name(name)
        
        #debug feedback that all worked as expected
        print 'ID: ', self.Emps[id].ID
        print 'Name: ', self.Emps[id].Name
        
    def get_available_id(self):
        '''Check for the next available ID number, initialize
        the first ID to the Default value'''
        if len(self.Emps) == 0 :
            return self.ID
        else:
            self.ID += 1
        return self.ID
            
            



    
