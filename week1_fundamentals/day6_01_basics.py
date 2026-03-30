def calculate_stress(E, strain):
    stress = E*strain
    return stress

result = calculate_stress(200e9, 0.002)
print(f"Stress is: {result/1e6} MPa")