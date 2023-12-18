
# Receipts for Lovely Loveseats
# We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.

# In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

# Please note: Projects do not run tests against your code. This experience is more open to your interpretation and gives you the freedom to explore. Remember that all variables must be declared before they are referenced in your code.


# Task 1. Let’s add in our first item, the Lovely Loveseat that is the store’s namesake. Create a variable called lovely_loveseat_description and assign to it the following string:
# "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
# "

# Task 2. Great, now let’s create a price for the loveseat. Create a variable lovely_loveseat_price and set it equal to 254.00

# Task 3. Let’s extend our inventory with another characteristic piece of furniture! Create a variable called stylish_settee_description and assign to it the following string:
# "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."

# Task 4. Now let’s set the price for our Stylish Settee. Create a variable stylish_settee_price and assign it the value of 180.50.

# Task 5. Fantastic, we just need one more item before we’re ready for business. Create a new variable called luxurious_lamp_description and assign it the following:
# "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
# "

# Task 6. Let’s set the price for this item. Create a variable called luxurious_lamp_price and set it equal to 52.15.

# Task 7. In order to be a business, we should also be calculating sales tax. Let’s store that in a variable as well.

# Define the variable sales_tax and set it equal to .088. That’s 8.8%.

# Task 8. Our first customer is making their purchase! Let’s keep a running tally of their expenses by defining a variable called customer_one_total. Since they haven’t purchased anything yet, let’s set that variable equal to 0 for now.

# Task 9. We should also keep a list of the descriptions of things they’re purchasing. Create a variable called customer_one_itemization and set that equal to the empty string "". We’ll tack on the descriptions to this as they make their purchases.

# Task 10. Our customer has decided they are going to purchase our Lovely Loveseat! Add the price to customer_one_total.

# Task 11. Let’s start keeping track of the items our customer purchased. Add the description of the Lovely Loveseat to customer_one_itemization.

# Task 12. Our customer has also decided to purchase the Luxurious Lamp! Let’s add the price to the customer’s total.

# Task 13. Let’s keep the itemization up-to-date and add the description of the Luxurious Lamp to our itemization.

# Task 14. They’re ready to check out! Let’s begin by calculating sales tax. Create a variable called customer_one_tax and set it equal to customer_one_total times sales_tax.

# Task 15. Add the sales tax to the customer’s total cost.

# Task 16. Let’s start printing up their receipt! Begin by printing out the heading for their itemization. Print the phrase "Customer One Items:".

# Task 17. Print customer_one_itemization.

# Task 18. Now add a heading for their total cost: Print out "Customer One Total:"

# Task 19. Now print out their total! Our first customer now has a receipt for the things they purchased.

# Task 20. Congratulations! We created our catalog and served our first customer. We used our knowledge of strings and numbers to create and update variables. We were able to print out an itemized list and a total cost for our customer. Lovely!




lovely_loveseat_description = "Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep Red or white."
lovely_loveseat_price = 254.00


stylish_settee_description = "Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
stylish_settee_price = 180.50

luxurious_lamp_description = "Luxurious Lamp. Glass and irom. 36 inches tall. Brown with dcream shade."
luxurious_lamp_price = 52.15


sales_tax = 0.088

customer_one_total = 0
customer_one_itemization = ""


customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description


customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description


customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer one items:")
print(customer_one_itemization)
print("Customer one Total:")
print(customer_one_total)

print('\n')

customer_two_total = 0
customer_two_itemization = ""

customer_two_total += stylish_settee_price
customer_one_itemization += stylish_settee_description


customer_two_total += luxurious_lamp_price
customer_two_itemization += luxurious_lamp_description

customer_two_tax = customer_two_total * sales_tax
customer_two_total += customer_two_tax

print("Customer two items:")
print(customer_two_itemization)
print("Customer two Total:")
print(customer_two_total)






