#ITI1120
#Assinment 2
#Jannah Hossain, 8616189
#Jennifer Vo, 7277323
#Stats function
'''It will read the users input and print out the number of numbers input'''
'''program function is called two_length_run()'''
def two_length_run():
    a = input('Input a list of numbers:')
    b =0
    for i in range(0,len(a)+1):
        if a[i] == a[i+1]:
            b = b+1
        elif i == len(a): 
            print (b)
    return b



    
two_length_run()

'''collections.Counter counts the number of numbers'''
''' keys seperates the values'''
'''len helps turn the string into a number'''
