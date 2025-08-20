students={}
while True:
    print('/n--- Student Management System ---')
    print('1.add student')
    print('2.add/update grade')
    print('3.calculate average grade')
    print('4.display all students')
    print('5.search for student')
    print('6.update student info')
    print('7.exit')
    
    ch=int(input("enter your choice: "))
    if ch == 1:
        roll = int(input("enter  roll number: "))
        if roll in students:
            print('students roll number already exists')
        name = input("enter a name: ")
        if name in students:
            print('student name already exists')
        else:
           students[roll] = {"name": name,"grades" : []}
           students[name] = {"roll" :roll,'grades':[]}
           print('student added successfully')
           
    elif ch == 2:
        roll = int(input("enter a roll number:"))
        if roll in students:
            try:
                grade = float(input("enter grade to add:"))
                students[roll]["grades"].append(grade)
                print("grade added")
            except ValueError:
                print("invalid grade format")
        else:
            print("student not found")
            
    elif ch == 3:
        roll = int(input("enter a roll number:"))
        if roll in students:
            grades=students[roll]["grades"]
            if grades:
                avg=sum(grades)/len(grades)
                print("average for students:",avg)
            else:
                print("no grades available")
        else:
            print("student not found")
    
    elif ch == 4:
        if not students:
            print("no students available")
        else:
            print("\nall students:")
            for roll,info in students.items():
               grades=info["grades"]
               avg=sum(grades)/len(grades) if grades else 0
               print(f"Roll: {roll}, Name: {info.get('name', 'Unknown')}, Grades: {grades}, Average: {avg}")
               
    elif ch == 5:
        roll=int(input("enter a roll number:"))
        if roll in students:
            info=students[roll]
            print(f" Roll: {roll}, Name: {info['name']}, Grades: {info['grades']}")
        else:
            print("student not found")
            
    elif ch == 6:
        roll=int(input("enter a roll number to update:"))
        if roll in students:
            new_name=input("enter a new name:")
            students[roll]["name"]=new_name
            print("student info updated")
        else:
            print("student not found")
            
    elif ch ==7:
        print("existing program...")
        break
    else:
        print("invalid ch.try again")
















        



    
