import sys

def genrandom(hetustart, gender):
	for x in range(2,899):
		if x%2 == 0 and gender == "f":
			id = '{:03}'.format(x)
			print(hetustart+id+hashgen(hetustart[0:6]+id))
		elif x%2 == 0 and gender == "m":
			pass
		elif x%2 == 1 and gender == "m":
			id = '{:03}'.format(x)
			print(hetustart+id+hashgen(hetustart[0:6]+id))
		else:
			pass
		
def hashgen(genhetu):
	hashlist = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","H","J","K","L","M","N","P","R","S","T","U","V","W","X","Y"]
	hash = int(genhetu)%31
	return hashlist[hash]

def main():
	try:
		birthday = sys.argv[1]
		if len(birthday) != 8:
			print("Usage: python ssn.py ddmmyyyy m/f")
			sys.exit(0)
		elif not birthday.isdigit():
			print("Usage: python ssn.py ddmmyyyy m/f")
			sys.exit(0)
		elif int(birthday[0:2]) > 31:
			print("Invalid date value. Must be ddmmyyyy.")
			sys.exit(0)
		elif int(birthday[2:4]) > 12:
			print("Invalid date value. Must be ddmmyyyy.")
			sys.exit(0)
	except IndexError:
		print("Usage: python ssn.py ddmmyyyy m/f")
		sys.exit(0)
	try:
		gender = str(sys.argv[2])
		if not (gender == "m" or gender == "f"):
			print("Please enter a valid gender (m or f)")
			sys.exit(0)
	except IndexError:
		print("You must specify a gender (m or f)")
		sys.exit(0)
	try:
		if int(birthday[4:6]) == 18:
			hetustart = birthday[0:4]+birthday[6:8]+"+"
		elif int(birthday[4:6]) == 19:
			hetustart = birthday[0:4]+birthday[6:8]+"-"
		elif int(birthday[4:6]) == 20:
			hetustart = birthday[0:4]+birthday[6:8]+"A"
		else:
			print("Invalid year. Supported years are 1800-2099.")
			sys.exit(0)
	except ValueError:
		print("Invalid date value. Must be ddmmyyyy.")
		sys.exit(0)
	try:	
		genrandom(hetustart,gender)
	except UnboundLocalError:
		print("Invalid date value. Must be ddmmyyyy.")
		sys.exit(0)
	

	
if __name__ == '__main__':
	main()
	



