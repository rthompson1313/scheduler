
#this is a change
#this is aslo a change
import collections as col

class Employee:
    """Class defining the employess attributes and functions"""
    def __init__(self):
        self.ID = None
        self.Name = 'Employee'
        self.Positions = []
        self.Max_Hours = None
        self.Pay_Rate = None
        self.Est_Week_hours = None
    
    def set_name(self, name):
        self.Name = name
    
    def set_id(self, id):
        self.ID = id
        
    #def set_default_positions(self):
    
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
    
    #Emps = None         #Dictionary containing employee Key numbers and objects
    #ID = None           #Employee ID
    #Name = None         #Employee Name 
    def __init__(self):
        '''Emps is a dictionary who's items are a Key which is the employee ID, and a
        value which is the employee object'''
        self.Emps = {}
        #self.ID = None
        #self.Name = 'employee'
        self.Key = 100
        #self.Pos = [] #default value
    
    def add_employee(self):
        '''Checks for next available employee Key and adds a new employee
        object to the Emps dictionary.'''
        #get new ID
        key = self.get_available_key()
        
        #instanciate new employee object
        self.Emps[key] = Employee()
        #self.Emps[key].set_id(self.ID)
        #self.Emps[key].set_name(self.Name)
        #self.Emps[key].set_default
        self.Emps = col.OrderedDict(sorted(self.Emps.items()))
        print 'key', key
        
    def remove_employee(self, key):
        '''Removes the employee matching the key from the Emps dictionary'''
        del self.Emps[key]
        self.Emps = col.OrderedDict(sorted(self.Emps.items()))
        
    def get_available_key(self):
        '''Check for the next available ID number, initialize
        the first ID to the Default value'''
        if len(self.Emps) == 0 :
            return self.Key
        else:
            self.Key += 1
        return self.Key
            
            



    
