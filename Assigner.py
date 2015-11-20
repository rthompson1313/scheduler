import Shift_Tracker
import Staff_Tracker


class Assigner:
    Assignments = dict()
    
    def assign(self, emp_id, shift_id):
        shift_id = str(shift_id[0]) + str(shift_id[1])
        self.Assignments[shift_id] = emp_id

