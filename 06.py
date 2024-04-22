cats_list = ["Octavia", "Ursula"]

def name_cats():
    for cat in cats_list:
        print(f"Meow my name is {cat}")
    return cats_list

print( name_cats() )