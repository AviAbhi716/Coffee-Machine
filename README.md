# Coffee-Machine

This Python program simulates a Coffee Machine that allows users to order different types of coffee while managing available resources and payments.

Features:

✔️ Coffee Menu: Offers three types of coffee – Latte, Espresso, and Cappuccino, each with specific ingredient requirements and costs.

✔️ Resource Management: Tracks the available quantities of water, milk, and coffee.

✔️ Payment System: Accepts Rs. 5, Rs. 10, and Rs. 15 coins, calculates the total amount, and returns change if needed.

✔️ Reports: Displays the remaining ingredients and total profit.

✔️ Machine Control:

    1. Type "report" to check remaining resources.
    
    2. Type "off" to turn off the machine.
    
✔️ Refilling & Error Handling: Notifies when ingredients are insufficient and asks for re-insertion of coins if payment is insufficient.

How It Works:

1. The user selects a coffee type (Latte, Espresso, or Cappuccino).
2. The program checks if there are enough ingredients to make the coffee.
3. The user inserts coins to pay for the coffee.
4. If the payment is less than required, the user is prompted to insert more coins.
5. If the payment is more than required, the program returns the change.
6. The coffee is served, and the resources are updated accordingly.
7. The process repeats until the user decides to turn off the machine.
   
This program is a fun and interactive way to understand resource management, condition checking, and user input handling in Python! ☕🔄
