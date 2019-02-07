#File contains the city name and temp in degree celcius.
#Convert the tempearture to farenheit and update in the same file.
	
import fileinput
for line in fileinput.input("temp.txt", inplace=True):
	city, temp = line.strip().split()
	temp = int(temp) + 32
	print("{} {}".format(city, str(temp)))