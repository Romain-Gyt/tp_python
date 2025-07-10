class Intervalle:
    def __init__(self, borne_min, borne_max):
        if borne_min > borne_max:
            borne_min, borne_max = borne_max, borne_min
        self.__borne_min = borne_min
        self.__borne_max = borne_max

    def __str__(self):
        return f"[{self.__borne_min} ; {self.__borne_max}]"

    # Getters
    def get_borne_min(self):
        return self.__borne_min

    def get_borne_max(self):
        return self.__borne_max

    # Setters
    def set_borne_min(self, val):
        if val <= self.__borne_max:
            self.__borne_min = val
        else:
            print("Erreur : la borne inférieure ne peut pas dépasser la borne supérieure.")

    def set_borne_max(self, val):
        if val >= self.__borne_min:
            self.__borne_max = val
        else:
            print("Erreur : la borne supérieure ne peut pas être inférieure à la borne inférieure.")


    def __add__(self, other):
        borne_min = self.__borne_min + other.__borne_min
        borne_max = self.__borne_max + other.__borne_max
        return Intervalle(borne_min, borne_max)


    def intersection(self, other):
        new_min = max(self.__borne_min, other.__borne_min)
        new_max = min(self.__borne_max, other.__borne_max)
        if new_min <= new_max:
            return Intervalle(new_min, new_max)
        else:
            return None


    def union(self, other):
        if self.intersection(other) is not None:
            new_min = min(self.__borne_min, other.__borne_min)
            new_max = max(self.__borne_max, other.__borne_max)
            return Intervalle(new_min, new_max)
        else:
            return None