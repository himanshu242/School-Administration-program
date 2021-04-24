import csv

def write_into_csv(info_list):
    with open('student_info.csv','w+', newline='') as csv_file:
        writer =csv.writer('csv_file')
        writer.writerow(["Name," "Age", "Contact Number ", "Email id"])
     
        writer.writerow(info_list)


if__name__=='__main__':
    condition = True
    student_num = 1

    while(condition):
        student_info= input('Enter student information for student#{} in the following Format (Name age Contact_number Email_id): '.format(student_num))
        
        #split
        student_info_list = student_info.split(' ')
        
        print("\nThe entered Information is -\nName: {}\nAge: {}\nContact_number: {}/nEmail Id: {} "
                .format(student_info_list[0],student_info_list[1], student_info_list[2], student_info_list[3]))

        choice_check = input("Is The Entered Information Correct? (yes/ no): ")
        
        if choice_check =="yes":
            write_into_csv(student_info_list)

        write_into_csv(student_info_list) 

        condition_check = input("Enter (yes/no) if you want to enter other student informaion ")
        
        if condition_check =="yess":
            condition = True
            student_num = student_num + 1
        elif condition_check =="no":
            condition = False
        elif choice_check =="no":
            print('\nPlease re-enter the values!')
