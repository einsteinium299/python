print('Convert Fahrenheit to Celsius')
temp = input("What is the temperature in Fahrenheit? ")
cel = 0
try:
    fahr = float(temp)
except:
    print("That's not a number")
    quit()
cel = (fahr - 32.0) * 5.0 / 9.0
print("The temperature in Celsius is " + str(cel))
