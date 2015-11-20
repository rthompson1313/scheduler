#diff check
import Shift_Tracker
import Staff_Tracker
import Assigner
from Tkinter import *

user = None
shift = Shift_Tracker.Shift()
week = Shift_Tracker.Week()
emps = Staff_Tracker.Staff()
assign = Assigner.Assigner()

class Application(Frame):
  
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_display()

    def create_display(self):
        #Create week display labels
        self.label0 = Label(self, text = 'Monday', width = 10)
        self.label0.grid(row = 1, column = 2)
        self.label1 = Label(self, text = 'Tuesday', width = 10)
        self.label1.grid(row = 1, column = 3)
        self.label2 = Label(self, text = 'Wednesday', width = 10)
        self.label2.grid(row = 1, column = 4)
        self.label3 = Label(self, text = 'Thursday', width = 10)
        self.label3.grid(row = 1, column = 5)
        self.label4 = Label(self, text = 'Friday', width = 10)
        self.label4.grid(row = 1, column = 6)
        self.label5 = Label(self, text = 'Saturday', width = 10)
        self.label5.grid(row = 1, column = 7)
        self.label6 = Label(self, text = 'Sunday', width = 10)
        self.label6.grid(row = 1, column = 8)
        self.label7 = Label(self, text = 'Name', width = 15)
        self.label7.grid(row =1, column = 0)
        self.label8 = Label(self, text = 'ID', width = 5)
        self.label8.grid(row =1, column = 1)
        
        #Create add employees button
        self.button = Button(self, text = 'Add Employee', width = 15)
        self.button['command'] = self.add_employee
        self.button.grid(row = 0, column = 0)
        
    def add_employee(self):
        emps.add_employee()
        print 'Add Emp'
        self.update()
        
    def add_shift(self):
        week.add_shift()
        
    def update(self):
        '''Update the display with new employees and shifts'''
        print 'Update!'
        count = 2
        
        for key in emps.Emps:
            '''iterate through the employee dict and create a button for each'''
            self.name = emps.Emps[key].Name
            print self.name
            str_name = str(self.name)
            '''clear the previous button'''
    
            '''create a button that passes the employee ID when clicked'''
            self.button_name = Button(self, text = str_name, command=lambda
                k=key: self.emp_popup(k))
            self.button_name.grid(row = count, column = 0)
            
            '''Create the ID label and increase the row count'''
            self.id = Label(self, text = str(key))
            self.id.grid(row = count, column = 1)
            count = count +1
    
    def emp_popup(self, key):
        print 'here again, ', key
        '''Get current employee parameters'''
        name = emps.Emps[key].Name
        positions = emps.Emps[key].Positions
        pay_rate = emps.Emps[key].Pay_Rate 
        
        '''create poopup window'''
        top = Toplevel()
        top.title(str(emps.Emps[key].Name) + "'s Parameters")
        top.geometry('300x350')
        
        '''create done button'''
        self.done = Button(top, text ='Done', command=top.destroy)
        self.done.grid()
        
        '''create employee parameter access'''
        #cur_name = StringVar()
        self.name_entry = Entry(top, bd =4)
        self.name_entry.grid()
        #cur_name.set(str(self.name))
        #emps.Emps[key].Name = str(cur_name.get)
        
        '''create the submit button'''
        self.submit = Button(top, text ='Submit', command= lambda k=key: self.submit_data(k))
        self.submit.grid()
        
    def submit_data(self, key):
        print 'submit'
        data = self.name_entry.get()
        print 'new name is', data
        emps.Emps[key].Name = data
        
        self.update()
       
        
        

root = Tk()
root.title('Test')
root.geometry('960x480')
app = Application(root)
root.mainloop()
'''
class Application(Frame):
  
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.button_state = 0
        self.create_widgets()

    def create_widgets(self):
        self.button = Button(self, text = 'Off')
        self.button['command'] = self.update_state
        self.button.grid()
    def update_state(self):
        if self.button_state == 0:
            self.button['text'] = 'On'
            self.button_state = 1
        else:
            self.button['text'] = 'Off'
            self.button_state = 0

root = Tk()
root.title('Test')
root.geometry('200x100')
app = Application(root)
root.mainloop()



while(user is not 'q'):
    user = raw_input('what would you like to do: ')
    if user == 'add shift':
        week.add_shift()
    elif user == 'remove shift':
        week.remove_shift()
    elif user == 'add employee':
        emps.add_employee()
    elif user == 'remove employee':
        emps.remove_employee()
    elif user == 'assign shift':
        emp_id = raw_input('Enter Employee ID: ')
        shift_day = raw_input('Enter Shift Day: ')
        shift_num = raw_input('Enter Shift id: ')
        shift_id = [shift_day, shift_num]
        assign.assign(emp_id, shift_id)
    elif user == 'show shifts':
        for i in week.Week:
            print i
    elif user == 'q':
        user = user
    else:
        print 'not valid entry'
'''