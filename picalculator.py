from math import sqrt, pi

def picalc(n_corners, s_length):#n_corners n Anzahl Ecken/ s_length Seitenlänge
    for index in range(1, 31):
        pi_approach = 0.5*n_corners*s_length
        print(round(pi_approach, 11))
        s_length = sqrt(2-sqrt(4-s_length*s_length))
        n_corners = 2*n_corners