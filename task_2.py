import numpy as np

print("Input length, average speeds, part of road start, part of road end")
lengths = np.array(list(map(float, input("length: ").split())))
speeds = np.array(list(map(float, input("speeds: ").split())))
k = int(input('part of road start: '))
p = int(input('part of road end: '))
if len(lengths) != len(speeds):
    print("Amount of lengths doesn't equal amount of speeds")
else:
    l = lengths[k-1:p]    
    v = speeds[k-1:p]
    s = l.sum()
    t = np.sum(l / v)  
    v_avg = s / t
    print(f"S = {s:.0f} км, T = {t:.2f} час, V = {v_avg:.2f} км/ч")