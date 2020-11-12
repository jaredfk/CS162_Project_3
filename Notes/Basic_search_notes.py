'''Project 5 notes and helpful code'''
# This algorithm is innefecient because it most go over every element individually.
# Big - O value is high, as the number of elements increases, number of operation increases. 

def search(a_list: list, target_value: int) -> bool:
    '''Search list for target value, return true if exists otherwise false
    Linear search, or time is related to elements. '''
    for element in a_list:
        if element == target_value:
            return True
    
    return False

def binary_search_helper(a_list: list, low: int, high: int, target_value: int) -> bool:
    '''Do binary search and return whether target value is in list or not '''
    if low > high:
        return False
    
    #else we have more space to check
    mid = (low + high) // 2
    mid_value = a_list[mid]


    if mid_value == target_value:
        return True
    elif mid_value < target_value:
        return binary_search_helper(a_list, mid + 1, high, target_value)
    else: #mid_value > target_value
        return binary_search_helper(a_list, low, mid -1, target_value)

def binary_search(a_list: list, target_value):
    return binary_search_helper(a_list, 0, len(a_list), target_value)



def main():
    '''Ask for and search for a value in a list'''
    list_values = input('Please enter a list of integer values seperated by spaces: ').split()
    list_values = list(map(int, list_values))
    target_value = int(input("Enter a integer to be searched for in the previously entered list: "))
    print(f'{target_value} is in the list {list_values}: {binary_search(list_values, target_value)}')

if __name__ == '__main__':
    main()