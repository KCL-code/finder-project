
import os
import json

choices=("COMP 1080SEF")
list_of_stduents=["John","Tom","Ken","George","Holly", "Ian", "Jade", "Kyle", "Laura", "Mason", "Nina"]
dictionary = {"COMP 1080SEF":["John","Nina","Mason","Laura","Kyle","Tom","Ken","George","Holly","Ian","Jade"]}

#lobby_contents
lobby=("----------------------Menu----------------------\n1.Get to know your classmates:\n2.Check existing groups:\n3.Advanced groupmates finder:\n")
#lobby_module
def main_menu():
    print(lobby)
    intro=int(input("Select to enter function:(1,2,3)\t"))
    return intro

while True:
    intro=main_menu()
    if intro ==1:
        os.system("cls")
        question=str(input("Which course are you inquiring about?\n(COMP 1080SEF)\n\nTerminal:\t"))
        #lookup_dictionary
        course_found=False
        for key,val in dictionary.items():
            if question == key:
                course_found=True
                os.system("cls")
                print(f"In {question} course, studnet {(val)} are your classmates")
                #Guide_question
                followup_on_profile=input("Do you wanna know more about them or return to Main menu?(continue/quit)\n\nTerminal:\t")
                while True:
                    if followup_on_profile == "continue":
                        intrest_in=input("\nPlease tell me which student you want to know more about him/her?\t(quit to return menu)\n\nTerminal:\t")
                    #Display student_profile
                        with open("student_profile.json","r") as file:
                            student_profile=json.load(file)
                            #ast to convert from tree data to normal data 
                            #student_profiles=ast.literal_eval(data)
                            if intrest_in in student_profile:
                                print(f"\n{intrest_in}'s profile:\n")
                                for attribute, value in student_profile[intrest_in].items():
                                    print(f"{attribute}: {value}")
                            elif intrest_in == "quit":
                                break
                            else:
                                os.system("cls")
                                print("student not found")
                    else:
                        os.system("cls")
                        print("Input error")
                        break
            if not course_found:
                print("course not found")
            

                        

    elif intro==2:
        while True:
            welcome = input("Which course are you enquiring about?\t(quit to return menu)\n(COMP 1080SEF)\nTerminal:\t")
            
            if welcome == "COMP 1080SEF":
                os.system('cls')
                with open('existing_group_in_COMP1080SEF.txt', 'r') as file:
                    content = file.read
                    for i in file:
                        print(i)

            elif welcome == "quit":
                os.system("cls")
                break

            else:
                os.system('cls')
                print("Course not found")
    
    elif intro==3:
        while True:
            #whoru=input("What is student name:\n\nTerminal:\t")
            #contactu=input("What is you phone number:\n\nTerminal:\t")
            leading=input("Which course have you enrolled (COMP 1080SEF)\n\nTerminal:\t")
            filter1=input("What range of GPA you wanna archive?\n(in a range of 2-3 or Above 3)\n\nTerminal:\t")

            if leading=="COMP 1080SEF":
                with open("student_profile.json","r") as access_json:
                    content=json.load(access_json)

                    selected_students = []
                    
                    if filter1 == "Above 3":
                        for name, info in content.items():
                            if "Above 3" in info["GPA_goal"]:
                                selected_students.append((name, info["Phone_number"]))
                                
                    elif filter1 == "in a range of 2-3":
                        for name, info in content.items():
                            if "in a range of 2-3" in info["GPA_goal"]:
                                selected_students.append((name, info["Phone_number"]))

                if selected_students:
                    print("\nStudents with GPA goals:")
                    for name, Phone_number in selected_students:
                        print(f"{name} has a GPA goal {filter1} and their phone number is {Phone_number}")

                    grouped_names = input(str("\nEnter the names of student you want to group with (quit to return menu):\nTerminal:\t"))
                    if grouped_names==quit:
                        break
                    else:
                        os.system("cls")
                        print("Input invaild")
                    grouped_names_list = [name.strip() for name in grouped_names.split(',')]

                
                    for name in grouped_names_list:
                        # Find and print the phone number for each grouped name
                            for student_name, Phone_number in selected_students:
                                if name == student_name:
                                    print("\nHis/her phone numbers are:")
                                    print(f"{name}: {Phone_number}\n")
                                    print("Please make sure he/her is not in any group and submit this grouping request to your professor by email")

            else:
                    os.system("cls")
                    print("Input invaild")
            break
    else:
        print("Your input is invaild")
