from conv import Converter
import argparse

converter = Converter()

parser = argparse.ArgumentParser()

parser.add_argument("-m", "--mode", help="Conversion mode", type=str)
parser.add_argument("-v", "--value", help="The value to be converted", type=str)


def main():
    args = parser.parse_args()

    assert args.mode != None, "No conversion mode provided"
    assert converter.conversion_exists(args.mode), "The conversion mode doesn't exist" 
    assert args.value != None, "No value given"
    
    print(converter.convert(args.value, args.mode))



if __name__ == '__main__':
    main()
