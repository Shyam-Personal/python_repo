#File contains the city name and temp in degree celcius.
#Convert the tempearture to farenheit and update in the same file.


def main():
	try:
		import fileinput
		for line in fileinput.input("Input_files/temp.txt", inplace=True):
			city, temp = line.strip().split()
			temp = int(temp) + 32
			print("{} {}".format(city, str(temp)))

	except Exception as e:
		print("Exception while executing program. Error details: {}".format(str(e)))


if __name__ == "__main__":
	main()
