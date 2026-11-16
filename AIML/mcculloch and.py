def mp_neuron(x1,x2,w1,w2,threshold):
    net=x1*w1+x2*w2
    if net>=threshold:
        return 1
    else:
        return 0
print("output")
for x1 in (0,1):
    for x2 in (0,1):
       output = mp_neuron(x1,x2,1,1,2)
       print(f"Input: ({x1}, {x2}), Output: {output}")