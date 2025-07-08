# créez une fonction qui prend en paramètres un **kwargs
# et qui renvoi la concaténation de toutes les clés valeur
# exemple function(je="suis", un="kwarg") doit renvoyer "jesuisunkwarg"
# exemple function(la="jolie", maison="dans", la="prairie") doit renvoyer "lajoliemaisondanslaprairie"
from unittest import result


def return_key_value(**attributes):
    result = ""
    for key, value in attributes.items():
        result += str(key) + str(value)
    return result

print(return_key_value(je="suis", un="kwarg"))
