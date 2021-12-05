dict_a = {
	"A":"a",
	"B":"b",
	"C":[{"F":"f","G":"g", "H":"h","I":"i"},{"F":"f","G":"g", "H":"h","I":"i"},{"F":"f","G":"g", "H":"h","I":"i"}],
	"D":"d",
	"E":"e"
	}

dict_b = {
	"A":"a",
	"B":"b",
	"D":"d",
	"E":"e"
	}

dict_c = {
	"A":"a",
	"B":"b",
	"C":[{"F":"f","G":"g", "H":"h","I":"i"},{"F":"f","G":"g", "H":"h","I":"i"},{"F":"f","G":"g", "H":"h","I":"i"}],
	"D":"d",
	"E":"e"
	}

def dictTest(dict):
    if "C" in dict:
        aliases = dict.get("C")
        for alias in aliases:
            print(alias["I"])
                
            

    
    else:
        print("Not in Dictonary")
        main()

def main():
    x= input("Choose a Dictonary. a, b or c ")
    if x == "a":
        dictTest(dict_a)
    elif x == "b":
        dictTest(dict_b)
    elif x == "c":
        dictTest(dict_c)
    else:
        print("Wrong")
        main()

if __name__ == '__main__':
    main()
