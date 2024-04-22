numbers_list = [1, 2]

def average_numbers_in_list(num_list:list):
    # number_list is empty
    return sum(num_list) / len(num_list)

avg = average_numbers_in_list( numbers_list )

print( avg )