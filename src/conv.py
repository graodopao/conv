class Converter:
    __conversiondict = {}

    def __init__(self) -> None:            
        self.__conversiondict = {
            # Data
            "bin2dec": self.__bin2dec,

            "mb2gb": lambda v : float(v) * 0.001, 
            "gb2mb": lambda v : float(v) * 1000.0,
            
            # Time
            "min2sec": lambda v : float(v) * 60.0,
            "min2hour": lambda v : float(v) / 60.0,
        }
    
    def conversion_exists(self, name) -> bool:
        return name in self.__conversiondict
    
    def convert(self, value, mode) -> any:
        assert self.conversion_exists(mode), "Conversion mode " + mode + " doesn't exist."
        return self.__conversiondict[mode](value)

    # --- Conversion methods ---
    @staticmethod
    def __bin2dec(binary_str: str) -> int:
        count = 0
        sum = 0
        # Loops through the sring and calculates the binary numbers into decimal
        for letter_index in range(len(binary_str) - 1, -1, -1):
            # Error checking
            char = binary_str[letter_index]
            assert char in ['0', '1'], "String doesn't represent a binary number (found char '" + char + "')."
            
            digit = int(binary_str[letter_index])
            if (digit != 0):
                sum += digit * pow(2, (count))

            count += 1
        
        return sum
            

            
