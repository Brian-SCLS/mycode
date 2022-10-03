#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   print() - display data to std out"""

# below is a function containing our code
def main():

    # wordbank list.
    wordbank= ["indentation", "spaces"] 
    
    print("wordbank before:",wordbank)

    # students list.
    tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

    wordbank.append(4)
    print("wordbank after:", wordbank)


    num = input("\nPlease enter a number between 0 and 18: ")
    int_num = int(num)
    if int_num < 0 or int_num > 18:
        print("Error! Number must be between 0 and 18. Number set to 5.")
        int_num = 5

    print("int_num:",int_num)

    student_name = tlgstudents[int_num]
    print("\n" + student_name + " always uses " + str(wordbank[2]) + " " + wordbank[1] + " to indent.")

# this calls main
main()

