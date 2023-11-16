import random
import time
from colorama import Fore



def random_list(size:int,max:int)->list:
    list=[]
    for i in range(0,size):
        list.append(random.randint(0,max))
    return list

def insertion_sort(list:list)->list:
    helper=0

    for j in range(1,len(list)):
        helper=list[j]
        for p in range(0,j):
            if list[p]>list[j]:
                o=j
                while o>p:
                    list[o]=list[o-1]
                    o-=1
                list[p]=helper
                break
    return list

def bubble_sort(list:list)->list:
    helper=0
    for i in range(0,len(list)):
        for i in range(0,len(list)-1):
            if list[i]>list[i+1]:
                helper=list[i]
                list[i]=list[i+1]
                list[i+1]=helper
    return list

def bubble_sort_flagged(list:list):
    notSorted=True
    while notSorted:
        notSorted=False
        for i in range(0,len(list)-1):
            if list[i]>list[i+1]:
                notSorted=True
                helper=list[i]
                list[i]=list[i+1]
                list[i+1]=helper    
    return list

def merge_sort(list:list)->list:
    midpoint=int(len(list)/2)
    left=list[0:midpoint]
    right=list[midpoint:]
    if len(left)>1:
        left=merge_sort(left)
    if len(right)>1:
        right=merge_sort(right)
    return _merge(left, right)

#Helper function for merge_sort
def _merge(a:list,b:list)->list:
    merged=[]
    left=0
    right=0
    while left<len(a) and right<len(b):
        if a[left]<b[right]:
            merged.append(a[left])
            left+=1
            continue
        else:
            merged.append(b[right])
            right+=1
            continue
    if left<len(a):
        merged+=a[left:]
    if right<len(b):
        merged+=b[right:]
    return merged


### My own experiments
def my_experimental_deuces_sort(list:list)->list:
    list_of_lists=[]
    counter=0
    doubles=0
    lenlist=len(list)
    while counter<lenlist:
        list_of_lists.append(_flip(list[counter:counter+2]))
        doubles+=1
        counter+=2
    if len(list)%2==1:
        list_of_lists.append(list[doubles*2:])
    sorted=[list_of_lists[0][0],list_of_lists[0][1]]
    lenlist_of_list=len(list_of_lists)
    for i in range(1,lenlist_of_list):
        sorted=_add_list_of_two(sorted, list_of_lists[i])
    return sorted


def my_experimental_deuces_sort2(list:list)->list:
    list_of_lists=[]
    counter=0
    doubles=0
    lenlist=len(list)
    while counter<lenlist:
        list_of_lists.append(_flip(list[counter:counter+2]))
        doubles+=1
        counter+=2
    if len(list)%2==1:
        list_of_lists.append(list[doubles*2:])
    sorted=_add_list_of_two(list_of_lists[0], list_of_lists[1])
    lenlist_of_list=len(list_of_lists)
    index=1
    counter=2
    while 2**index<=lenlist_of_list/2:
        for i in range(2**index,2**index*2):
            sorted=_add_list_of_two(sorted, list_of_lists[i])
        index+=1
    return sorted

def _flip(list:list)->list:
    bigger=0
    if len(list)==1:return list
    if list[0]>list[1]:
        bigger=list[0]
        list[0]=list[1]
        list[1]=bigger
    return list

def _add_list_of_two(list:list, list_of_two:list)->list:
    index=0
    index2=0
    sorted=[]
    lenlist=len(list)
    threshold=len(list_of_two)
    while index<lenlist and index2<threshold:
        if list[index]<list_of_two[index2]:
            sorted.append(list[index])
            index+=1
        else:
            sorted.append(list_of_two[index2])
            index2+=1
        if index2==threshold:
            sorted+=list[index:]
            break
        if index==lenlist:
            sorted+=list_of_two[index2:]
    return sorted

def my_magnitude_merge_sort(list:list)->list:
    midpoint=int(len(list)/2)
    left=list[0:midpoint]
    right=list[midpoint:]
    if len(left)>2:
        left=merge_sort(left)
    if len(right)>2:
        right=merge_sort(right)
    return _merge(left, right)

### end of my experiments

#Wrapper function for running the algorithms
def test_wrapper(list_size, max_integer,algorithm,print_results=True):
    lista=random_list(list_size,max_integer)
    print()
    print(Fore.LIGHTYELLOW_EX,f"Running {algorithm.__name__} with input size {list_size}...")
    start_time=time.time_ns()
    if print_results:
        print(Fore.LIGHTYELLOW_EX,"List before sorting:")
        print(Fore.RED, lista)
    lista=algorithm(lista)
    if print_results:
        print(Fore.LIGHTYELLOW_EX,"List after sorting:")
        print(Fore.GREEN,lista)
    end_time=time.time_ns()
    timer(start_time,end_time)



#Prints the duration in a relevant time unit
def timer(start_time,end_time)->str:
    duration=end_time-start_time
    if duration<1000:
        print(Fore.MAGENTA, "Finished in",duration,"ns")
    elif duration/1000<1000:
        print(Fore.MAGENTA,"Finished in",duration/1000 ,"µs")
    elif duration/1000000<1000:
        print(Fore.MAGENTA,"Finished in",duration/1000000,"ms")
    else:
        print(Fore.MAGENTA,"Finished in",duration/1000000000,"s")    

def counting_sort(list:list[int]):
    c=[0]*(max(list)+1)
    b=[0]*len(list)
    for i in range(len(list)):
        c[list[i]]+=1
    #print("Occurences of indexes in list:",c)
    for i in range(1,len(c)):
        c[i]+=c[i-1]
    #print("Cumulative occurences in list:",c)
    for i in range(len(c)):
        c[i]-=1
    #print("0-index corrected vector c:",c)
    for i in range(len(list)-1,-1,-1):
        b[c[list[i]]]=list[i]
        c[list[i]]-=1
    for i in range(len(list)):
        list[i]=b[i]

### Execution area. Includes example code. Alter for your conveniece ###

# The size of the list to be sorted
input_size=200000
# The maximum value of any given integer in the list
maximum_value_of_random_integer_in_list=10000

## Executions
<<<<<<< HEAD
"""test_wrapper(input_size,maximum_value_of_random_integer_in_list,bubble_sort, False)
test_wrapper(input_size,maximum_value_of_random_integer_in_list,bubble_sort_flagged, False)"""
#test_wrapper(input_size,maximum_value_of_random_integer_in_list,insertion_sort, False)
test_wrapper(input_size,maximum_value_of_random_integer_in_list,merge_sort, False)
#test_wrapper(input_size,maximum_value_of_random_integer_in_list,my_experimental_deuces_sort, False) #No good O(n^2)
#test_wrapper(input_size,maximum_value_of_random_integer_in_list,my_experimental_deuces_sort2, False) #No good O(n^2)
test_wrapper(input_size,maximum_value_of_random_integer_in_list,my_magnitude_merge_sort, False)
print("Ended")
=======
#test_wrapper(input_size,maximum_value_of_random_integer_in_list,bubble_sort, False)
#test_wrapper(input_size,maximum_value_of_random_integer_in_list,bubble_sort_flagged, False)
#test_wrapper(input_size,maximum_value_of_random_integer_in_list,insertion_sort, False)
test_wrapper(input_size,maximum_value_of_random_integer_in_list,merge_sort, False)
test_wrapper(input_size,maximum_value_of_random_integer_in_list, counting_sort, False)
>>>>>>> 156b3b4ab31462d3391652092f4e4e62a7808989

