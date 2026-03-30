# Problem 61: Write a function called factor_of_safety
# Takes: yield_stress, applied_stress_start, increase
# While FOS > 1.5, keep increasing applied stress
# Formula: FOS = yield_stress / applied_stress
# Return final applied_stress and FOS
# Call it: factor_of_safety(250e6, 50e6, 10e6)
# Print: "Applied Stress: X MPa - FOS: X"

def factor_of_safety(yield_stress, applied_stress_start, increase):
    FOS = yield_stress / applied_stress_start
    while FOS > 1.5:
        applied_stress_start = applied_stress_start + increase
        FOS = yield_stress / applied_stress_start
    return applied_stress_start, FOS
applied_stress_start, FOS =factor_of_safety(250e6, 50e6, 10e6)
print(f"Applied Stress: {applied_stress_start/1e6} MPa - FOS: {FOS}")

