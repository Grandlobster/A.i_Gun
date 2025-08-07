def mirror_value(val, start, end):
    midpoint = (start + end) / 2
    mirror_val = midpoint - (val - midpoint)
    return mirror_val

# Example usage
start = 0
end = 180
val = 56
mirror_val = mirror_value(val, start, end)
print("Mirror value of", val, "is", mirror_val)
