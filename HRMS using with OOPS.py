                                   # Human Relation Management System
# BLL: Business Logic Layer
class Employee:
    emp_list=[]
    def __init__(self):
        self.id=0
        self.name=0
        self.age=0
        self.mob=0
    def addemployee(self):
        Employee.emp_list.append(self)

    def searchemployee(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                self.name=id.name
                self.age=id.age
                self.mob=id.mob
                return
    def deleteemployee(self):
        for e in Employee.emp_list:
            if(e.id==self.id):
                Employee.emp_list.remove(e)
        Employee.emp_list.pop()

    def modifyemployee(self):
        for e in Employee.emp_list:
             if(e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                return

class Manager(Employee):
     def __init__(self):
         self.branch=0
         super().__init__()

     def addmanager(self):
         Employee.emp_list.append(self)

     def searchmanager(self):
         for e in Employee.emp_list:
              if(e.id==self.id):
                  self.name=e.name
                  self.age=e.age
                  self.mob=e.mob
                  self.branch=e.branch
                  return

     def deletemanager(self):
         for e in Employee.emp_list:
             if(e.id==self.id):
                 Employee.emp_list.remove(e)
             Employee.emp_list.pop()

     def modifymanager(self):
         for e in Employee.emp_list:
             if(e.id==self.id):
                 e.name=self.name
                 e.age=self.age
                 e.mob=self.mob
                 e.branch=self.branch
                 return


class Trainer(Employee):
    def __init__(self):
        self.course=0
        super().__init__()

    def addtrainer(self):
        Employee.emp_list.append(self)

    def searchtrainer(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                self.course=e.course
                return

    def deletetrainer(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                Employee.emp_list.remove(e)
            Employee.emp_list.pop()

    def modifytrainer(self):
        for e in Employee.emp_list:
            if (e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                e.course=self.course
                return


class Director(Employee):
    def __init__(self):
        self.share=0
        super().__init__()

    def adddirector(self):
        Employee.emp_list.append(self)

    def searchdirector(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                self.name=e.name
                self.age=e.age
                self.mob=e.mob
                self.share=e.share
                return

    def deletedirector(self):
        for e in Employee.emp_list:
            if (e.id == self.id):
                Employee.emp_list.remove(e)
            Employee.emp_list.pop()

    def modifydirector(self):
        for e in Employee.emp_list:
            if (e.id==self.id):
                e.name=self.name
                e.age=self.age
                e.mob=self.mob
                e.share=self.share
                return


# PL: Presentation Layer
print("Welcome to HRMS")
def showEmployee(emp):
    print("EMP ID:",emp.id,"EMP NAME:",emp.name,"EMP AGE:",emp.age,"EMP MOB:",emp.mob)

def showManager(mng):
    print("MNG ID:", mng.id, "MNG NAME:", mng.name, "MNG AGE:", mng.age, "MNG MOB:", mng.mob,"MNG BRANCH:",mng.branch)

def showTrainer(tra):
    print("TRA ID:", tra.id, "TRA NAME:", tra.name, "TRA AGE:", tra.age, "TRA MOB:", tra.mob,"TRA COURSE:",tra.course)

def showDirector(dir):
    print("DIR ID:", dir.id, "DIR NAME:", dir.name, "DIR AGE:", dir.age, "DIR MOB:", dir.mob,"DIR SHARE:",dir.share)

def getmob():
    while(1):
         mob=input("Enter mob number:")
         if(mob.isdecimal()):
             if(len(mob)==10):
                 return mob
             else:
                 print("Enter the number for 10 digits")
         else:
              print("Enter mob no's with digits only")
while(1):
    ch=input("Enter choice: 1 ADD EMPLOYEE, 2 MANAGER, 3 TRAINER, 4 DIRECTOR, 5 EXIT:")
# EMPLOYEE
    if(ch==("1")):
        while(1):
            ch=input("Enter choice: 1 ADD EMPLOYEE, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
            if(ch=="1"):
                emp=Employee()
                emp.id=input("Enter the employee ID:")
                emp.name=input("Enter the employee NAME:")
                emp.age=input("Enter the employee AGE:")
                emp.mob=getmob()
                emp.addemployee()
            elif(ch=="2"):
                 emp=Employee()
                 emp.id=input("Enter the employee ID:")
                 emp.searchemployee()
                 showEmployee(emp)
            elif(ch=="3"):
                emp=Employee()
                emp.id=input("Enter the employee ID:")
                showEmployee(emp)
            elif(ch=="4"):
                emp=Employee()
                emp.id=input("Enter the update employee ID:")
                emp.name=input("Enter the update employee NAME:")
                emp.age=input("Enter the update employee AGE:")
                emp.mob=getmob()
            elif(ch=="5"):
                for i in Employee.emp_list:
                 showEmployee(i)
            elif(ch=="6"):
                print("Thanks for using Employee Department")
                break
            else:
                print("invalid choice")
    # MANAGER
    if(ch=="2"):
        while(1):
            ch = input("Enter choice: 1 ADD MANAGER, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
            if (ch == "1"):
             mng=Manager()
             mng.id = input("Enter the manager ID:")
             mng.name = input("Enter the manager NAME:")
             mng.age = input("Enter the manager AGE:")
             mng.mob = getmob()
             mng.branch = input("Enter the manager branch:")
             mng.addmanager()
            elif (ch == "2"):
             mng=Manager()
             mng.id = input("Enter the manager ID:")
             mng.searchmanager()
             showManager(mng)
            elif (ch == "3"):
             mng=Manager()
             mng.id = input("Enter the manager ID:")
             mng.deletemanager()
             showManager(mng)
            elif (ch == "4"):
             mng=Manager()
             mng.id = input("Enter the update manager ID:")
             mng.name = input("Enter the update manager NAME:")
             mng.age = input("Enter the update manager AGE:")
             mng.mob = getmob()
             mng.branch = input("Enter the update manager BRANCH:")
             mng.modifymanager()
            elif (ch == "5"):
             for i in Manager.emp_list:
               showManager(i)
            elif (ch == "6"):
              print("Thanks for using manager Department")
              break
            else:
                print("invalid choice")
# TRAINER
    if(ch == "3"):
       while(1):
           ch = input("Enter choice: 1 ADD TRAINER, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
           if (ch == "1"):
            tra=Trainer()
            tra.id = input("Enter the trainer ID:")
            tra.name = input("Enter the trainer NAME:")
            tra.age = input("Enter the trainer AGE:")
            tra.mob = getmob()
            tra.course = input("Enter the trainer course:")
            tra.addtrainer()
           elif (ch == "2"):
            tra=Trainer()
            tra.id = input("Enter the trainer ID:")
            tra.searchtrainer()
            showTrainer(tra)
           elif (ch == "3"):
            tra=Trainer()
            tra.id = input("Enter the trainer ID:")
            tra.deletetrainer()
           elif (ch == "4"):
            tra=Trainer()
            tra.id = input("Enter the update trainer ID:")
            tra.name = input("Enter the update trainer NAME:")
            tra.age = input("Enter the update trainer AGE:")
            tra.mob = getmob()
            tra.course = input("Enter the update trainer course:")
            tra.modifytrainer()
           elif (ch == "5"):
            for i in Trainer.emp_list:
             showTrainer(i)
           elif (ch == "6"):
            print("Thanks for using trainer Department")
            break
           else:
                print("invalid choice")
    # DIRECTOR
    if(ch == "4"):
       while(1):
           ch = input("Enter choice: 1 ADD DIRECTOR, 2 SEARCH, 3 DELETE, 4 MODIFY, 5 DISPLAY ALL, 6 EXIT:")
           if (ch == "1"):
            dir=Director()
            dir.id = input("Enter the director ID:")
            dir.name = input("Enter the director NAME:")
            dir.age = input("Enter the director AGE:")
            dir.mob = getmob()
            dir.share = input("Enter the director SHARE:")
            dir.adddirector()
           elif (ch == "2"):
            dir=Director()
            dir.id = input("Enter the director ID:")
            dir.searchdirector()
            showDirector(dir)
           elif (ch == "3"):
            dir=Director()
            dir.id = input("Enter the director ID:")
            dir.deletedirector()
           elif (ch == "4"):
            dir=Director()
            dir.id = input("Enter the update director ID:")
            dir.name = input("Enter the update director NAME:")
            dir.age = input("Enter the update director AGE:")
            dir.mob = getmob()
            dir.share = input("Enter the update director SHARE:")
            dir.modifydirector()
           elif (ch == "5"):
            for i in Director.emp_list:
             showDirector(i)
           elif (ch == "6"):
            print("Thanks for using director Department")
            break
    elif (ch == "5"):
        print("thanks for using HRMS")
        break
    else:
        print("Invalid choice")





