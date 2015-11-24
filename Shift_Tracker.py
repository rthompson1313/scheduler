'''
Written by Ryan Thompson.
Classes to define and manage the lists of shift objects
'''


class Shift:
    '''defines the parameters of a shift object'''
    def __init__(self):
        self.ID = None
        self.Day = None
        self.Position = None
        self.Employee = None
        self.Start = None
        self.End = None
        self.Est_Hours = None
    
    def set_id(id):
        self.ID = id
    
    def set_position(position):
        self.Position = position
        
    #def set_employee(employee):
    
    def set_start(start):
        self.Start = start
        
    def set_end(end):
        self.End = end
        
class Week:
    '''Defines a week as a list of length 7 each representing a day of the week.
    Each of the 7 list items is another list which holds instances of shift objects
    These shift objects can be appended, deleted and modified as needed.
    ex. Week = [[obj0, obj1, obj2],[]...[]]'''
    #self.Week = [m={},t={},w={},th={},f={},s={},su={}] #A list of 7 dicts, one for each day to hold the shift instances
    def __init__(self):    
        self.Week = [{},{},{},{},{},{},{}]
        
    def add_shift(self, day):
        '''Appends a shift object to the specified day. Assigns the object an ID
        which is an integer decimal number representing the object's location in the 
        list.''' 
        #day representing a list item in Week 1-7
        #day = raw_input('Enter Day: ')
        #map day to 0 - 6
        #day = int(day) - 1
        #value assigned to the shift's id
        shift_id = None
        #temp value to hold the current location in the day list
        count = 0
        
        '''Searches through the list and looks for an empty location. Assigns a
        shift ID representing the earliest available location'''
        for key in self.Week[day]:
            if key is None:
                shift_id = count
                break
            count += 1
        if shift_id is None:
            shift_id = len(self.Week[day])    
        #instanciate a new shift object in that day list location
        self.Week[day][shift_id] = Shift()


        self.Week[day][shift_id].ID = shift_id
        self.Week[day][shift_id].Day = day
        print 'day',  self.Week[day][shift_id].Day, 'id', self.Week[day][shift_id].ID

        
    def remove_shift(self, day):
        '''removes a shift object from the day list by using integer input from the 
        user for the day numer (1-7) and the shift ID number'''
        #day = int(raw_input('Enter Day: '))
        #day = day - 1
        #shift_id = int(raw_input('Enter ID: '))
        #print 'day, id: ' , day, shift_id
        #remove the shift object but keep the item location in tact 
        self.Week[day][shift_id] = None
        print self.Week[day][shift_id]
                 
class Schedules:
    Name = None
    Weeks = []
    Positions = ['BT' ,'BB', 'CT']
    def set_name(self, name):
        self.Name = name
        
    #def add_week(self):



#Tests


