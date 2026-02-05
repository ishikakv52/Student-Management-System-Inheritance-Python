import datetime 
x=datetime.datetime.now()
class Cal:
    def __init__(self,name,rollno,days,a,b,c,t,perc):
        self.name=name
        self.rollno=rollno
        self.days=days
        self.a=a
        self.b=b
        self.c=c
        self.t = a + b + c
        self.perc = self.t / 3
        
    # def s(self):
    #     print(self.days)    
    def att_per(self):
        absent=int(input("Enter the number of absent: "))
        print("Total Absent : ",absent)
        t=self.days-absent
        percentage=t/self.days*100
        print("Total percentage. : ",percentage)
    def library(self):
        title=input("Enter title of the book : ") 
        name=input("enter author of the book: ")
        date=x.strftime("%x") 

        print("Title : ",title)
        print("Name : ",name)
class Management(Cal):
    def salary(self):
        total_sal=eval(input("Enter your total salary : "))
        absent=int(input("Enter the number of absents : "))
        present=self.days-absent
        t=total_sal/self.days
        s=t*present
        print("Salary of ",present," days :",s)


class Student(Management):
    def per(self):
        self.name=input("Enter name:")
        self.rollno=int(input("Enter rollno. : "))
        self.a=eval(input("Enter marks of first subject : "))
        self.b=eval(input("Enter marks of second subject : "))
        self.c=eval(input("Enter marks of third subject : "))
        self.t=self.a+self.b+self.c
        self.perc=self.t/3
        return self.perc
    def result(self):
        r=str(self.rollno)
        n=str(self.name)
        a=str(self.a)
        b=str(self.b)
        c=str(self.c)
        t=str(self.t)
        p=str(self.perc)
        file=r
        f=open(file+".txt","w")
        f.write("Name : "+n+"\nRoll no :"+r+"\nMarks of subject A : "+a+"\nMarks of subject B : "+b+"\nMarks of subject C : "+c+"\nTotal : "+t+"\nPercentage : "+p)
        f.close()
        print("Result created✅")
days=30
name=input("Enter name:")
rollno=int(input("Enter rollno. : "))
a=eval(input("Enter marks of first subject : "))
b=eval(input("Enter marks of second subject : "))
c=eval(input("Enter marks of third subject : "))
t = a + b + c
per = t / 3
# c = Cal(name, rollno, days, a, b, c, t, per)

cal = Cal(name, rollno, days, a, b, c, t, per)


m = Management(name, rollno, days, a, b, c, t, per)

# m.att_per()
# m.salary()
# c.att_per()    
s = Student(name, rollno, days, a, b, c, t, per)


# s.library()
# s.per()
s.result()
