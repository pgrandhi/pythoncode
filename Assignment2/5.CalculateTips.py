#Prompt the use to enter subtotal and gratuity rate
subtotal,gratuityrate = map(float, input("Enter the subtotal and a gratuity rate:").split(","))

def calculateTips(subtotal,gratuityrate):   
    gratuity = subtotal * (gratuityrate/100
    total = subtotal + gratuity
    print("The gratuity is ", round(gratuity,2), " the total is ", round(total,2))

calculateTips(subtotal,gratuityrate)
