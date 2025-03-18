profit=0
resources={
    'water':1000,
    'milk':500,
    'coffee':200
}
Menu={
    'latte':{
        'Ingredients':{
            'water':100,
            'milk':50,
            'coffee':10
        },
        'cost':150
},
    'espresso':{
        'Ingredients':{
            'water':120,
            'milk':60,
            'coffee':30
        },
        'cost':200
},
    'cappuccino':{
        'Ingredients':{
            'water':80,
            'milk':100,
            'coffee':40
        },
        'cost':250
}
}
def check_resources(o_ingredients):
    for item in o_ingredients:
        if o_ingredients[item]>resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
def left():
    for quant in resources:
        resources[quant] -= Menu[coffee]['Ingredients'][quant]
def renter():
    coin=True
    while coin:
        print("Please take your cash")
        print("Please Insert coins again")
        rs5 = int(input("How many 5Rs. coins:"))
        rs10 = int(input("How many 10Rs. coins:"))
        rs15 = int(input("How many 15Rs. coins:"))
        total = rs5 * 5 + rs10 * 10 + rs15 * 15
        if total< Menu[coffee]['cost']:
            coin = True
        else:
            coin = False
game=True
while game:
    coffee=input("What would you like to have? (latte/espresso/cappuccino):").lower()
    if coffee=='off':
        game=False
    elif coffee=='report':
        print(f"Water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}gm")
        print(f"Money: Rs{profit}")
    else:
        check=check_resources(Menu[coffee]['Ingredients'])
        left()
        if check is True:
            profit += int(Menu[coffee]['cost'])
            print("Please Insert coins")
            Rs5 = int(input("How many 5Rs. coins:"))
            Rs10 = int(input("How many 10Rs. coins:"))
            Rs15 = int(input("How many 15Rs. coins:"))
            Total = Rs5 * 5 + Rs10 * 10 + Rs15 * 15
            if Total < Menu[coffee]['cost']:
                renter()
            elif Total > Menu[coffee]['cost']:
                print(f"Here is your {Total - Menu[coffee]['cost']} change")
            print(f"Here is your {coffee}")

