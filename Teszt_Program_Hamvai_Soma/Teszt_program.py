# Author: Soma Hamvai
# Jelentkezés a "Python fejlesztő" pozícióra a OdooTech Zrt. vállalatnál.
# 1. függvény

import os
import json

class Auto:
    def __init__(self, id, type, ajtok_szama, marka):
        self.id = id
        self.type = type
        self.ajtok_szama = ajtok_szama
        self.marka = marka

class Bicikli:
    def __init__(self, id, type, terhelhetoseg, marka):
        self.id = id
        self.type = type
        self.terhelhetoseg = terhelhetoseg
        self.marka = marka

def load_data(directory):
    vehicles = []

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.dat'):
                with open(os.path.join(root, file), 'r') as f:
                    data = json.load(f)
                    id = os.path.splitext(file)[0]

                    if data['type'] == 'auto':
                        vehicle = Auto(id, data['type'], data['ajtok_szama'], data['marka'])
                    elif data['type'] == 'bicikli':
                        vehicle = Bicikli(id, data['type'], data['terhelhetoseg'], data['marka'])
                    else:
                        print(f"Ismeretlen típusú közlekedési eszköz: {data['type']}")
                        continue

                    vehicles.append(vehicle)
                    print(f"{vehicle.id} betöltve.")

    return vehicles

# 2. függvény
def print_vehicles(vehicles):
    for vehicle in vehicles:
        if vehicle.type == 'auto':
            print(f"ID: {vehicle.id}, Típus: {vehicle.type}, Ajtók száma: {vehicle.ajtok_szama}, Márka: {vehicle.marka}")
        elif vehicle.type == 'bicikli':
            print(f"ID: {vehicle.id}, Típus: {vehicle.type}, Terhelhetőség: {vehicle.terhelhetoseg}, Márka: {vehicle.marka}")

vehicles = load_data('C:/Users/Hamvai/Desktop/Teszt_Program_Hamvai_Soma/data')
print_vehicles(vehicles)