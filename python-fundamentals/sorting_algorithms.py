

def bubble_sort(lst: list) -> list:
    """ Sorts the list using bubble sort. Time complexity is: O(n) """
    n = len(lst)
    comparison_count = 0
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] < lst[j + 1]:
                comparison_count += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
              
    print(comparison_count)
    print(lst)  
    return lst
    

def insertion_sort(lst: list) -> list:
    """ Sorts the list using insertion sort. Time complexity is: O(n) """
    
    for i in range(1, len(lst)):
        comparison_count = 0
        
        key = lst[i]
        j = i - 1
        
        while j >= 0 and lst[j] > key:
            comparison_count += 1
            lst[j + 1] = lst[j]
            j -= 1
            
        lst[j + 1] = key
        
    print(comparison_count)
    print(lst)
    return lst

def selection_sort(lst: list) -> list:
    """ Sorts the list using selection sort. Time complexity: O(n^2)"""
    n = len(lst)
    count_comparison = 0
    for i in range(n):
        min_idx = i
        
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                count_comparison += 1
                min_idx = j
                
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
        
    print(count_comparison)
    print(lst)
    return lst
    

lst = list(input("Enter values to insert in list: "))

sorted_bubble = bubble_sort(lst)
sorted_insertion = insertion_sort(lst)
sorted_selection = selection_sort(lst)

new_lst = sorted(lst)
if new_lst == sorted_bubble:
    print("Bubble Matched")
    
if new_lst == sorted_insertion:
    print("Insertion Matched")
    
if new_lst == sorted_selection:
    print("Selection Matched")