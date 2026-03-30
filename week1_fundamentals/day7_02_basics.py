material = {
    "steel" : {"E": 200e9, "yield_stress": 250e6, "density": 7850},
    "aluminium" : {"E": 69e9, "yield_stress": 270e9, "density": 2700},
    "titanium" : {"E": 116e9, "yield_stress": 880e6, "density": 4500}
}
material["copper"] = {"E": 110e9, "yield_stress": 210e6, "density": 8960}
print(material)
print(material["steel"]["E"])
print(material["aluminium"]["density"])
print(material["copper"])