""" Author: Hasan Skaiky
 Date: 03/03/2019  """

import csv
import sys

name = "@auther: Hasan Skaiky"


filename = "Quttinirpaaq_NP_Tundra_Plant_Phenology_2016-2017_data_1.csv"
datast_array = []
new_mylist = []

var = 1 #used for while loop

''' menu for user selection '''
menu =  "\nPlease select one of the follwoing: \n" \
        "1.Reload the data from the dataset, replacing the in-memory data\n" \
        "2.Display all the records held in the simple data structure\n" \
        "3.Create a new record and store it in the simple data structure\n" \
        "4.Select, display and edit a record held in the simple data structure\n" \
        "5.Delete a record from the simple data structure\n" \
        "0.EXIT\n\n "



''' prints auther name '''
print # prints emptyline
print name
print # prints emptyline

'''exception handling for opening file'''

try:
    with open(filename, 'r') as filehandle: #opens file
        datast_array = [current_place.rstrip() for current_place in filehandle.readlines()]
        print (datast_array[0]) #print titles
        print (datast_array[1]) #print data
        print
        '''loops for 10 records'''
        for x in range(2, 12): #loop < 10
            new_mylist.append(datast_array[x]) # save first 10 records to array
        print ('\n'.join(map(str, new_mylist))) # print the first 10 records of the new array
        print
        print name  #keep name visible on the screen when scrolling

    ''' loops through the menu'''
    while var ==1:
        try:
            '''get input from user'''
            user_selection = input(menu)
            type(user_selection)
            '''handles if users select option 1'''
            if user_selection == 1:
                for i in new_mylist: #clears list
                    new_mylist[:] = []
                    ''' reloads data into the list '''
                for x in range(2, 12): #loop < 10
                    new_mylist.append(datast_array[x]) # save first 10 records to array
                print name

            elif user_selection == 2:
                print ('\n'.join(map(str, new_mylist))) # print the first 10 records of the new array
            elif user_selection == 3:
                create_new_record = raw_input("please insert the new record you want to create\n")# do something
                type(create_new_record)
                new_mylist.append(create_new_record)
                print "New Record has been added\n"
                print name
            elif user_selection == 4:
                edit_record = input("Select the index of the record you want to edit\n") # do something
                type(edit_record)
                print new_mylist[edit_record]
                edit_record_str = raw_input("Please enter the replacement\n") # do something
                type(edit_record_str)
                new_mylist[edit_record] = edit_record_str
                print " Record has been edited and replaced"

            elif user_selection == 5:
                delete_record = input("Select the index of the record you want to delete\n") # do something
                type(delete_record)
                new_mylist.remove(new_mylist[delete_record])
                print "Record has been deleted\n"
                print ('\n'.join(map(str, new_mylist)))
                print name

            elif user_selection == 0:
                break
        except: #handles exceptions for incorrect options
            print "You haven't selected anything, please select from the Menu"


except IOError: #handles error for file open
    print 'Problem with File',filename

finally: #close file and exit

    filehandle.close()
    print "Exiting..."
