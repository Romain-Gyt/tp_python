from Poo.Intervalle import Intervalle

if __name__ == "__main__":
    a = Intervalle(2, 5)
    b = Intervalle(3, 6)
    print("a :", a)
    print("b :", b)

    c = a + b
    print("a + b =", c)

    inter = a.intersection(b)
    print("Intersection de a et b :", inter)

    union = a.union(b)
    print("Union de a et b :", union)


    a.set_borne_min(1)
    a.set_borne_max(7)
    print("a modifié :", a)

    a.set_borne_min(8)