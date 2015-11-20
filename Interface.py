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
sch = Shift_Tracker.Schedules()

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
        self.button = Button(self, text = 'Add Employee', width = 15, command = self.add_employee)
        self.button.grid(row = 0, column = 0)
        
    def add_employee(self):
        print 'start add_emp'
        emps.add_employee()
        self.update()
        print 'end add_emp'
        
    def add_shift(self):
        week.add_shift()
        
        
    def clear_emps(self):
        print 'start clear_emps'
        #do only if we allready have an emps list
        if len(emps.Emps) > 0:
            #delete the previous buttons
            for key in emps.Emps:
                #self.name = emps.Emps[key].Name
                #str_name = str(self.name)
                self.button_name.destroy()
        print 'end clear_emps'
        
    def update(self):
        '''Update the display with new employees and shifts'''
        print 'start update'
        #specifies the starting row for the buttons on the window
        count = 2
         
        
        for key in emps.Emps:
            '''iterate through the employee dict and create a button for each'''
            self.name = emps.Emps[key].Name
            #print self.name
            str_name = str(self.name)
            
            '''create a button that passes the employee ID when clicked'''
            self.button_name = Button(self, text = str_name, command=lambda
                k=key: self.emp_popup(k))
            self.button_name.grid(row = count, column = 0)
            
            '''Create the ID label and increase the row count'''
            self.id = Label(self, text = str(emps.Emps[key].ID))
            self.id.grid(row = count, column = 1)
            count = count +1
        print 'end update'
    
    def emp_popup(self, key):
        print 'start emp_popup'
        '''Get current employee parameters'''
        name = str(emps.Emps[key].Name)
        ID = str(emps.Emps[key].ID)
        positions = emps.Emps[key].Positions
        pay_rate = emps.Emps[key].Pay_Rate 
        pos_row_count = 2
        
        '''create poopup window'''
        top = Toplevel()
        top.title(name + "'s Parameters")
        top.geometry('200x250')
        
        
        
        '''create employee parameter access'''
        #name widget
        self.name_label = Label(top, text = 'name', width = 8)
        self.name_label.grid(row = 0, column = 0)
        self.name_entry = Entry(top, bd =2, width = 10)
        self.name_entry.insert(0, name)
        self.name_entry.grid(row = 0, column = 1)
        self.name_entry.bind('<Return>', lambda e: self.submit_data(key))
        
        #ID widget
        self.id_label = Label(top, text = 'ID', width = 8)
        self.id_label.grid(row = 1, column = 0)
        self.id_entry = Entry(top, bd =2, width = 10)
        self.id_entry.insert(0, ID)
        self.id_entry.grid(row =1, column = 1)
        self.id_entry.bind('<Return>', lambda e: self.submit_data(key))
        
        #positions widget
        self.pos_label = Label(top, text = 'Positions', width = 8)
        self.pos_label.grid(row = 2, column = 0)
        for pos in sch.Positions:
            match = False
            for emp in emps.Emps[key].Positions:
                if emp == pos:
                    match = True
            self.pos_button = Checkbutton(top, text = str(pos), offvalue = None, onvalue = pos, width = 10)
            self.pos_button.grid(row = pos_row_count, column = 1)
            pos_row_count += 1
        
        '''create done button'''
        self.done = Button(top, text ='Done', command=top.destroy)
        self.done.grid()
        
        print 'end emp_popup'
        
    def submit_data(self, key):
        print 'start submit'
        self.clear_emps()
        #grab the data from the popup entrys
        name = self.name_entry.get()
        ID = self.id_entry.get()
        #pos = self.pos_entry.get()
        
        #load new data into employee object
        emps.Emps[key].Name = name
        emps.Emps[key].ID = ID
        
        #handle positions lists
        #print pos
        #emps.Emps[key].Positions = pos
        
        self.update()
        print 'end submit'
       
        
        

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