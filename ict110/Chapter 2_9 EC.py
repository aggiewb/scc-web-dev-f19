#Chapter 2:9 Convert Fahrenheit to Celsius
#Aggie Wheeler Bateman
#A program that converts Fahrenheit to Celsius

def main():
    
    print("Hi user! My name is Sage, and I am a friendly program that converts Fahrenheit to Celsius.")
    fahrenheit = eval(input("Please enter the Fahrenheit temperture that you would like converted to Celsius: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print("The temperature of", fahrenheit, "Fahrenheit is", celsius, "Celsius.")

main()
    
    
