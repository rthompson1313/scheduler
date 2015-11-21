#diff check
import Shift_Tracker
import Staff_Tracker
import Assigner
import time
import collections as col
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
        self.label0.grid(row = 1, column = 3)
        self.label1 = Label(self, text = 'Tuesday', width = 10)
        self.label1.grid(row = 1, column = 4)
        self.label2 = Label(self, text = 'Wednesday', width = 10)
        self.label2.grid(row = 1, column = 5)
        self.label3 = Label(self, text = 'Thursday', width = 10)
        self.label3.grid(row = 1, column = 6)
        self.label4 = Label(self, text = 'Friday', width = 10)
        self.label4.grid(row = 1, column = 7)
        self.label5 = Label(self, text = 'Saturday', width = 10)
        self.label5.grid(row = 1, column = 8)
        self.label6 = Label(self, text = 'Sunday', width = 10)
        self.label6.grid(row = 1, column = 9)
        self.label7 = Label(self, text = 'Name', width = 15)
        self.label7.grid(row =1, column = 0, columnspan = 2)
        self.label8 = Label(self, text = 'ID', width = 5)
        self.label8.grid(row =1, column = 2)
        
        #Create add employees button
        self.add_emp = Button(self, text = '+', width = 1, command = self.add_employee)
        self.add_emp.grid(row = 0, column = 0, columnspan = 2)
        '''#Create remove employee button
        self.remove_emp = Button(self, text = '-', width = 1, command = self.remove_employee)
        self.remove_emp.grid(row = 0, column = 1)'''
        
    def add_employee(self):
        #print 'start add_emp'
        self.clear_emp_buttons()
        emps.add_employee()
        self.update()
        #print 'end add_emp'
        
    def remove_employee(self, key):
        #print 'Remove Employee', key
        self.clear_emp_buttons()
        emps.remove_employee(key)
        self.update()
        
        
    def add_shift(self):
        week.add_shift()
        
    def add_position(self, pos, key):
        print 'Add Position', key, pos
        emps.Emps[key].add_position(pos)
        print emps.Emps[key].Positions
        
    def remove_position(self, pos, key):
        print 'Remove Position', key, pos
        emps.Emps[key].remove_position(pos)
        print emps.Emps[key].Positions
        
    def clear_emp_buttons(self):
        #print 'start clear_emp_buttons'
        ##print 'len emps', len(emps.Emps)
        #do only if we allready have an emps list
        if len(emps.Emps) > 0:
            #delete the previous buttons
            for key in emps.Emps:
                '''iterate through the employee dictionary and destroy 
                the buttons and labels with the associated keys'''
                self.name_buttons[key].destroy()
                self.id_labels[key].destroy()
                print key, 'destroyed'
        #print 'end clear_emp_buttons'
        #time.sleep(2)
        
    def update(self):
        '''Update the display with new employees and shifts'''
        #print 'start update'
        #specifies the starting row for the buttons on the window
        count = 2
        #dictionary to hold button instances
        self.name_buttons = {}
        #dictionary to hold label instaces
        self.id_labels = {}
         
        for key in emps.Emps:
            '''iterate through the employee dict and create a button for each'''
            self.name = emps.Emps[key].Name
            ##print self.name
            str_name = str(self.name)
            
            '''create a button that passes the employee key when clicked'''
            self.name_buttons[key] = Button(self, text = str_name, command=lambda
                k=key: self.emp_popup(k))
            self.name_buttons[key].grid(row = count, column = 0, columnspan = 2)
            print key, 'created'
            
            '''Create the ID label and increase the row count'''
            self.id_labels[key] = Label(self, text = str(emps.Emps[key].ID))
            self.id_labels[key].grid(row = count, column = 2)
            count = count +1
            ##print count, emps.Emps[key].Name, key
        #print 'end update'
        
    '''def remove_emp_popup(self):
        
        top = Toplevel()
        top.title('Remove Employee')
        top.geometry('200x250')
        
        #instructions labal
        message = 'Select the Employees to remove'
        instruct = Label(top, text = message)
        instruct.grid()'''
        
    
    def emp_popup(self, key):
        #print 'start emp_popup'
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
        
        '''create employee parameter access labels and entrys'''
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
        
        print key, 'Positions', emps.Emps[key].Positions
        for pos in sch.Positions:
            '''iterate through the available positions'''
            self.match = False
            for emp in emps.Emps[key].Positions:
                '''check if the employee has any matches'''
                if emp == pos:
                    self.pos_button = Checkbutton(top, text = str(pos), width = 10, 
                        command = lambda p = pos, k = key: self.remove_position(p,k))
                    self.pos_button.select()
                    self.match = True
            if self.match == False:
                self.pos_button = Checkbutton(top, text = str(pos), width = 10, 
                    command = lambda p = pos, k = key: self.add_position(p,k))
                self.pos_button.deselect()
            self.pos_button.grid(row = pos_row_count, column = 1)
            pos_row_count += 1
        
        #remove employee widget
        self.remove_emp = Button(top, text = 'Remove Employee', command = lambda 
            k=key: self.remove_employee(k))
        self.remove_emp.grid(column = 0, columnspan = 2)
        
        '''create done button'''
        self.done = Button(top, text ='Done', command=top.destroy)
        self.done.grid(column = 0, columnspan = 2)
        
        #print 'end emp_popup'
        
    def submit_data(self, key):
        #print 'start submit'
        self.clear_emp_buttons()
        #grab the data from the popup entrys
        name = self.name_entry.get()
        ID = self.id_entry.get()
        #pos = self.pos_entry.get()
        
        #load new data into employee object
        emps.Emps[key].Name = name
        emps.Emps[key].ID = ID
        
        #handle positions lists
        ##print pos
        #emps.Emps[key].Positions = pos
        
        self.update()
        #print 'end submit'
       
        
        

root = Tk()
root.title('Test')
root.geometry('960x480')
app = Application(root)
root.mainloop()
