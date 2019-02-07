import json

def json_parser(ip):
	with open("input.json") as fh:
		d1 = json.load(fh)
		
		for i in range(len(d1["clients"])):
			for j in range(len(d1["clients"][i]["value"])):
				if(ip == d1["clients"][i]["value"][j]["ip"]):
					return(d1["clients"][i]["name"], d1["clients"][i]["value"][j]["username"], d1["clients"][i]["value"][j]["password"])

def main():
	s = input("Enter ip address to search: ")
	print(json_parser(s))
	
if __name__ == "__main__":
	main()