import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mode", help="Conversion mode", type=str)
parser.add_argument("-v", "--value", help="The value to be converted", type=float)


conversiondict = {
    "mb2gb": lambda v : v * 0.001, 
    "gb2mb": lambda v : v * 1000.0,
}

def main():
    args = parser.parse_args()

    assert args.mode != None, "No conversion mode provided"
    assert args.mode in conversiondict, "The conversion mode doesn't exist" 
    assert args.value != None, "No value given"
    
    print("Converted value: ", conversiondict[args.mode](args.value))


if __name__ == '__main__':
    main()


