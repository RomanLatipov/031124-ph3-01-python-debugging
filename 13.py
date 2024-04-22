dogs_list = ['Clifford', 'Scooby Doo', 'Balto']

def print_list_items(list_param:list):
    i = 0
    while i <= len( list_param )-1:
        print(list_param[i])
        i += 1


print_list_items( dogs_list )