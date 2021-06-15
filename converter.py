# Create a file called “converter.py” that requests an hour value, converts it to seconds and returns the result.
myHour = float(input('Input the hour you want to convert: '))
myConversion = myHour * 3600
myHour = str(myHour)

print('The hour(s) has been converted into ' + myHour + ' seconds')
print(myConversion)