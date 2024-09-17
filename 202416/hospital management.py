patients=[]

def patient_add(patient):
    global patients
    patients.append(patient)  

def patient_remove(patient):
    global patients
    try:
        patients.remove(patient)
    except ValueError as err:
        print("no records")    

def menu():
    choice = int(input('''1-add
2-delete                                            
your choice:'''))
    if choice == 1:
        patient1 = input('Enter the patient name:')
        patient_add(patient1)
        print(patients)
    elif choice == 2:
        patient2= input('Enter patient name:')
        patient_remove(patient2)
        print(patients)
def menus():
    choice=menu()
    while choice != 3:
        choice = menu()
    print('App Ended')
   
menus()    