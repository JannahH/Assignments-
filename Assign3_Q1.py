#ITI1120
#Assinment 2
#Jannah Hossain, 8616189
#Jennifer Vo, 7277323
#Stats function
def count_pos(x):
'''It will read the users input and print out the number of positive numbers '''
'''program function is called count_pos()'''
    
    b = 0
    for i in y :
    # condition on positive integers
        if i > 0:
            b = 1 + b
    print('There are', b ,'positive numbers in your list.')
    return (y)
# input by user
a = input ('Please input a list of numbers separated by commas: ')
# converted into a list)
y = list(eval(a))
count_pos(y)

'''eval(x) helps turn the list into an integer''' 
