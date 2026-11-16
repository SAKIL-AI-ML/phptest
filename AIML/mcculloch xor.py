def mp_neuron(x1,x2,w1,w2,threshold):
    net=x1*w1+x2*w2
    if net>=threshold:
        return 1
    else:
        return 0
def xor(x1,x2):
    h1=mp_neuron(x1,x2,1,1,1)
    h2=mp_neuron(x1,x2,-1,-1,-1)
    result=mp_neuron(h1,h2,1,1,2)
    return result
for x1 in (0,1):
    for x2 in (0,1):
        print(x1,x2,xor(x1,x2))