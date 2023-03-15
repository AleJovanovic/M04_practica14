#A -Aleksandra Jovanovic

import json
from Integrant_A.Car import Car
from Integrant_A.user import user



#crear una llista per cada classe creada 

cars = [

    Car("Lamborghini","10000 km/h","XFGBH300","2010"),
    Car("Mercedes","200 km/h","MERC22","2000")

]

users = [
    
    user("Aleksandra Jovanovic","23","7484398437C","Gran Via, 46, 3o 2a,Barcelona","ajovanov22@gmail.com","española"),
    user("Oriol Roca","32","37283727B","Ciutat Vella,38,1o 3a,Barcelona","oroca@gmail.com","española")

]


#convertir les llistes creades a diccionaris JSON

cars_list=[A_cars.to_dict() for A_cars in cars]

users_list=[A_users.to_dict() for A_users in users]

#envolvemos las listas dentro de un objeto contenedor

data = {"users":users_list, "cars":cars_list}


#guardar l'objecte contenedor a un  arxiu

with open("json_API/a.json",'w') as file:
    json.dump(data,file)




#B -Maria Palomeque

import json
import Cat
import university


#crear una llista per cada classe creada 

cats = [
    Cat("Luna","f","2","persa","Barcelona","España"),
    Cat("Nina","f","1","egipcio","Madrid","España")
] 

universitys = [
    university("Barcelona","Barcelona","Industria","Economia","Empresa" ),
    university("Madrid","Madrid","Diputacion","Biologia","Bioquimica")
]


#convertir les llistes creades a diccionaris JSON

cats_list = [c.to_disct() for c in cats]

universitys_list = [u.to_dict() for u in universitys]


#envolvemos las listas dentro de un objeto contenedor

data = {"cats":cats_list, "universitys":universitys_list}


#guardar l'objecte contenedor a un  arxiu

with open("json_API.json/cats.json",'w') as file:
    json.dump(data, file)

