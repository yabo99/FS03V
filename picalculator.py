from math import pi

def picalc(i_round=11): 
    return round(pi, i_round)

def main():

    print(picalc())
    
if __name__ == "__main__":
    main()