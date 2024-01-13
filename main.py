import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mode", help="Conversion mode", type=str)
parser.add_argument("-v", "--value", help="The value to be converted", type=float)


conversiondict = {
    "mb2gb": lambda v : v * 0.001, 
}

def main():
    args = parser.parse_args()

    # Checks if the arguments are valid
    if args.mode == None:
        print("No conversion mode provided")
    elif not args.mode in conversiondict:
        print("Conversion mode doesn't exist")
    elif args.value == None:
        print("No value provided")

if __name__ == '__main__':
    main()





