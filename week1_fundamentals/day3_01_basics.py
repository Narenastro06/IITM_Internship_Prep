E = 200e9
yield_stress = 250e6
force = 60000
area = 0.00001

stress = force/area
print(f"Stress = {stress/1e6:.2f} MPa")
if stress > yield_stress:
    print("FAILURE")
elif stress > 0.8*yield_stress:
    print("WARNING")
else:
    print('SAFE')