from math import radians, cos, sin, asin, sqrt
import random


class Main:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.ordre = list(range(len(x)))
        self.miniter = 20
        self.bordre = []

    def longueur(self, ordre):
        i = ordre[-1]
        x0, y0 = self.x[i], self.y[i]
        d = 0
        for o in ordre:
            x1, y1 = self.x[o], self.y[o]
            d += (x0-x1)**2 + (y0-y1)**2
            x0, y0 = x1, y1
        return d

    def permutation(self):
        d = self.longueur(self.ordre)
        d0 = d+1
        it = 1
        while d < d0:
            it += 1
            d0 = d
            # on part de 1 et plus de 0, on est sûr que le premier noeud ne bouge pas
            for i in range(1, len(self.ordre)-1):
                for j in range(i+2, len(self.ordre) + 1):  # correction !
                    r = self.ordre[i:j].copy()
                    r.reverse()
                    ordre2 = self.ordre[:i] + r + self.ordre[j:]
                    t = self.longueur(ordre2)
                    if t < d:
                        d = t
                        self.ordre = ordre2
        return self.ordre

    def n_permutation(self):
        ordre = list(range(len(self.x)))
        bordre = ordre.copy()
        d0 = self.longueur(ordre)
        for i in range(0, 20):
            # print("iteration", i, "d=", d0)
            random.shuffle(ordre)
            ordre = self.permutation_rnd()
            d = self.longueur(ordre)
            if d < d0:
                d0 = d
                bordre = ordre.copy()
        return (bordre, 1818)

    def permutation_rnd(self):
        d = self.longueur(self.ordre)
        d0 = d+1
        it = 1
        while d < d0 or it < self.miniter:
            it += 1
            d0 = d
            for i in range(1, len(self.ordre)-1):
                for j in range(i+2, len(self.ordre) + 1):
                    k = random.randint(1, len(self.ordre)-1)
                    l = random.randint(k+1, len(self.ordre))
                    r = self.ordre[k:l].copy()
                    r.reverse()
                    ordre2 = self.ordre[:k] + r + self.ordre[l:]
                    t = self.longueur(ordre2)
                    if t < d:
                        d = t
                        self.ordre = ordre2
        return self.ordre


"""
[
    {
      lat: 0.8459165322899798,
      lng: -179.9835205078125
    },
    {
      lat: -0.269164049012702,
      lng: -179.4012451171875
    },
    {
      lat: -0.15380840901698828,
      lng: 178.6981201171875
    }
  ]
"""

testt = Main([0.8459165322899798, -0.269164049012702, -0.15380840901698828],
             [-179.9835205078125, -179.4012451171875, 178.6981201171875])
print(testt.n_permutation())
