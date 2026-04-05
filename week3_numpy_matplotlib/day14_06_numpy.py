import numpy as np
stress = np.array([100, 200, 300, 400, 500]) #MPa
# np.where — finds values that meet a condition
failed = np.where(stress>250)
print(f"Failed at indices: {failed}")
print(f"Failed stress values: {stress[failed]}")