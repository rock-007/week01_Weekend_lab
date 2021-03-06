def get_pet_shop_name(all_pet_shop):
    return all_pet_shop["name"] 

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, cash_value):
    
   pet_shop["admin"]["total_cash"] += cash_value
   

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop,additional_sold):
    pet_shop["admin"]["pets_sold"] += additional_sold

def get_stock_count(pet_shop):
   return len(pet_shop['pets'])

def get_pets_by_breed(pet_shop,value):
    breed_list=[]
    for each_pet in pet_shop["pets"]:
        
        if(each_pet["breed"]==value):
            breed_list.append(each_pet)
        
    return breed_list

def find_pet_by_name(pet_shop,display_name):
    
    for each_pet in pet_shop["pets"]:
        
        if(each_pet["name"]==display_name):
            return each_pet
        
            

def remove_pet_by_name(pet_shop, remove_name):
    for each_pet in pet_shop["pets"]:
        if (each_pet["name"] == remove_name):
            pet_shop["pets"].remove(each_pet)

def add_pet_to_stock(pet_shop, new_pet):
    
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(customer,remove_value):
    customer["cash"]= customer["cash"]-remove_value
    return customer

def get_customer_pet_count(customer):
    return len(customer["pets"])

def add_pet_to_customer(customer, new_pet):
    return customer["pets"].append(new_pet)
    
def customer_can_afford_pet(customer, new_pet):
    if(customer["cash"]>=new_pet["price"]):
        return True
    else:
        return False
        
def sell_pet_to_customer(pet_shop,pet,customer):
    for each_pet in pet_shop["pets"]:
        if(pet !=None and each_pet["name"]==pet["name"] and customer["cash"]>=each_pet["price"]):
            customer["pets"].append(pet)

            remove_customer_cash(customer,pet["price"])
            add_or_remove_cash(pet_shop, pet["price"])
            increase_pets_sold(pet_shop,1)


        



  













