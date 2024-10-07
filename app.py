class school:
    def __init__(self,branch,teacher,department,avaliable):
        self.branch = branch
        self.teacher= teacher
        self.department=department
        self.avaliable=avaliable
   

    def show_info(self):
        print("-"*45)
        print("Branch: {}\nTeacher: {}\nDepartment: {}\nAvaliable Student: {}".format(self.branch,self.teacher,self.department,self.avaliable))
        print("-"*45)

    
    def teacher_name(self):
        print("Teacher name: ",self.teacher)

    def depart_change(self):
        new_depart=input("Please enter new department: ")
        print("***Old  Department***: ",self.department)
        self.department=new_depart
        print("-"*45)
        print("Branch: {}\nTeacher: {}\nDepartment: {}\nAvaliable Student: {}".format(self.branch,self.teacher,self.department,self.avaliable))
        print("-"*45)


while True:
    branch_name=input("Please enter branch name")
    teacher_info=input("please enter name")
    depart_info=input("please enter depart")
    avaliable_student=int(input("please enter avaliable student"))

    create_class=school(branch_name,teacher_info,depart_info,avaliable_student)
    print("--Welcome--")

    desicion=input("Please enter 1 if you want to change depart ")
    if desicion=="1":
        create_class.depart_change()
    else:
        print("Process is done!!!")   
        break 
