import random

def find_it(num,element_list):
    
    for i in range(len(element_list)):
        
        if (element_list[i]==num):
            print(i+1)
            break
        continue

#Initializes a list with values 1 to n in random order and returns it
def initialize_list_of_elements(n):
    list_of_elements=[]
    for i in range(1,n+1):
        list_of_elements.append(i)
    mid=n//2
    for j in range(0,n):
        index1=random.randrange(0,mid)
        index2=random.randrange(mid,n)
        num1=list_of_elements[index1]
        list_of_elements[index1]=list_of_elements[index2]
        list_of_elements[index2]=num1
    return list_of_elements

def play(n):
 
    li=initialize_list_of_elements(n)
    nu=random.randrange(1,n+1)
    find_it(nu,li)

#Pass different values to play() and observe the output
play(100)
