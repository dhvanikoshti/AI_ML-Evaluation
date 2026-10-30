emp=[]

def create_emp(id,name,dept):
    emp_data={"id":id,"name":name,"dept":dept}
    for e in emp:
        if e.id==id:
            print("Please Enter another Id ")
            return
    emp.append(emp_data)

def get_data():
    for e in emp:
        print(e)

def mark_attendance(emp_id,date,status):
    attendance={"date":date,"status":status}
    for e in emp:
        if e.id==emp_id:
            if date==emp["date"]:
                print("Already Attendance Marked")
                return
            emp[id]=attendance

def generate_attendance(id):
    print("\n==============================\n")
    print("\t\tEMPLOYEE ATTENDANCE REPORT\t\t\n")
    print("\n==============================\n")

    for e in emp:
        if e.id==id:
            print("Employee Id :",e["id"])
            print("Employee Name :",e["name"])
            print("Department :",e[dept])
            
while True:
    print("1. Create Employee") 
    print("2. Get Employee Data") 
    print("3. Mark Attendance ") 
    print("4. Generate Attendance Summary")
    print("5. Exit")

    ch=int(input("Enter Your Choice :"))

    match ch: 
        case 1:
            id=int(input("Enter Employee Id :"))
            name=input("Enter Name :")
            dept=input("Enter Department :")            
            create_emp(id,name,dept)
            print("Employee Created Successfully")
            break
            
        case 2:
            get_data()
            break

        case 3:
            id=int(input("Enter Employee Id :"))
            date=input("Enter Date :")
            status=input("Enter Status :")
            mark_attendance(id,date,status)   
            print("Attendance Marked Successfully")
            break
        
        case 4:
            id=int(input("Enter Employee Id :"))
            generate_attendance(id)
            break

        case 5:
            exit(0)
            
        case _:
            print("Invalid Choice")
    
            
        