def picalc(f_diameter, f_circlelength, i_round=11):#f_diameter Durchmesser/f_circlelength Umfang
    return round((f_circlelength/f_diameter), i_round)

def main():
    f_diameter = float(input("Bitte geben Sie den Durchmesser ein: "))
    f_circlelength = float(input("Bitte geben Sie den Umfang ein: "))

    print(picalc(f_diameter, f_circlelength))
    
if __name__ == "__main__":
    main()