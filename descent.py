temps_c = [0, 100, 20, 37]
temps_f = [32, 212, 68, 98.6]

w = 1.5
learning_rate = 0.01
def loss(w): 
    total = 0
    for c, f in zip(temps_c, temps_f):
        prediction = c * w + 32
        total = total +abs(prediction - f)
    return total
for step in range(100):
    if loss(w + 0.01) > loss(w):
        w = w - learning_rate
    else:
        w = w + learning_rate
    if loss(w) < 0.0001:
            print("found it:", w)
            break
    print(step, w, loss(w))   



