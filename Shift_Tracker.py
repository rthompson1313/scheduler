'''
Written by Ryan Thompson.
Classes to define and manage the lists of shift objects
'''


class Shift:
    '''defines the parameters of a shift object'''
    ID = None
    Position = None
    Employee = None
    Start = None
    End = None
    Est_Hours = None
    
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
    Week = [[],[],[],[],[],[],[]] #A list of 7 lists, one for each day to hold the shift instances
        
    def add_shift(self):
        '''Appends a shift object to the specified day. Assigns the object an ID
        which is an integer decimal number representing the object's location in the 
        list.''' 
        #day representing a list item in Week 1-7
        day = raw_input('Enter Day: ')
        #map day to 0 - 6
        day = int(day) - 1
        #value assigned to the shift's id
        shift_id = None
        #temp value to hold the current location in the day list
        count = 0
        
        '''Searches through the list and looks for an empty location. Assigns a
        shift ID representing the earliest available location'''
        for i in self.Week[day]:
            if i is None:
                shift_id = count
                break
            count += 1
        if shift_id is None:
            shift_id = len(self.Week[day])
        #append a new empty item in the day list    
        self.Week[day].append([])
        #instanciate a new shift object in that day list location
        self.Week[day][shift_id] = Shift()
        #set the objects day and ID values
        self.Week[day][shift_id].ID = [day, shift_id]

        
    def remove_shift(self):
        '''removes a shift object from the day list by using integer input from the 
        user for the day numer (1-7) and the shift ID number'''
        day = int(raw_input('Enter Day: '))
        day = day - 1
        shift_id = int(raw_input('Enter ID: '))
        print 'day, id: ' , day, shift_id
        #remove the shift object but keep the item location in tact 
        self.Week[day][shift_id] = None
        print self.Week[day][shift_id]
                 
class Schedules:
    Name = None
    Weeks = []
    
    def set_name(self, name):
        self.Name = name
        
    #def add_week(self):



#Tests


