import sys
from math import sqrt

class Trojuhelnik:
    def __init__(self, Bod1, Bod2, Bod3):
        self.b1 = Bod1
        self.b2 = Bod2
        self.b3 = Bod3
        self.str_a = sqrt(pow(self.b2[0] - self.b1[0], 2) + pow(self.b2[1] - self.b1[1], 2))
        self.str_b = sqrt(pow(self.b3[0] - self.b2[0], 2) + pow(self.b3[1] - self.b2[1], 2))
        self.str_c = sqrt(pow(self.b1[0] - self.b3[0], 2) + pow(self.b1[1] - self.b3[1], 2))
        self.obvod = self.str_c + self.str_a + self.str_b
        self.obsah = sqrt(self.obvod/2*(self.obvod/2 - self.str_a)*(self.obvod/2 - self.str_b)*(self.obvod/2 - self.str_c))

    def sestrojitelny(self):
        if self.str_a + self.str_b > self.str_c and self.str_b + self.str_c > self.str_a and self.str_c + self.str_a > self.str_b :
            return True
        else:
            return False
    def pravouhly(self):
        if pow(self.str_a,2) + pow(self.str_b,2) == pow(self.str_c,2) or pow(self.str_b,2) + pow(self.str_c,2) == pow(self.str_a,2) or pow(self.str_c,2) + pow(self.str_a,2) == pow(self.str_b,2):
            return True
        else:
            return False

try:
    vstup = sys.argv
    vstup.remove("trojuhelnik.py")
    vstup = list(map(int, vstup))

    t1 = Trojuhelnik([vstup[0],vstup[1]], [vstup[2],vstup[3]], [vstup[4],vstup[5]])
    print(f"Strana A: {t1.str_a}, Strana B: {t1.str_b}, Strana C: {t1.str_c}")
    if t1.sestrojitelny():
        print(f"Trojúhelník je sestrojitelný a jeho obvod je {t1.obvod} a obsah {t1.obsah}")
    else:
        print("Trojúhelník není sestrojitelný")
    if t1.pravouhly():
        print("Trojúhelník je pravoúhlý")
    else:
        print("Trojúhelník není pravoúhlý")
except ValueError:
    print("Please insert 6 arguments that reporesent coordinates of 3 points.")