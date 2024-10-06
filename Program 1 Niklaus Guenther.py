#Don't forget to rename this file after copying the template
#for a new program!
"""
Student Name: Niklaus Guenther     
Program Title: Hipster Local Vinyl Records
Description: Program 1   
"""

def main(): #<-- Don't change this line!
    #Write your code below. It must be indented!
    customerName = input("Enter the customer's name: ")
    kilometers = float(input("Enter the distance in kilometers: "))
    recordCost = float(input("Enter the cost of the records: "))

    #delivery rate and tax rate
    deliveryRate = 15.0
    taxRate = 0.14

    #Calculates the delivery cost, the cost with tax, and the total
    deliveryCost = kilometers * deliveryRate
    purchaseCost = recordCost + (recordCost * taxRate)
    totalCost = deliveryCost + purchaseCost

    
    print("Receipt for", customerName)
    print("Delivery Cost: $", (deliveryCost))
    print("Purchase Cost (with tax): $", (purchaseCost))
    print("Total Cost: $", (totalCost))



    #Your code ends on the line above

#Do not change any of the code below!
main()