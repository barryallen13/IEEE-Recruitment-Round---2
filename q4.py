class binary_to_roman:
    def bin_to_rom(self, binary_no) :
        string = str(binary_no)
        lst1 = list(string)
        integer = 0
        for i in range((len(lst1)-1),-1,-1):
            integer += int(lst1[i]) * (2**((len(lst1)-1) - i))
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        n=0
        roman_number = ''
        while integer>0 :
            for k in range(integer//values[n]) :
                roman_number +=symbols[n]
                integer -= values[n]
            n+=1
        return roman_number

binary = int(input("Please input your binary number : "))
print(binary_to_roman().bin_to_rom(binary))
            
        
