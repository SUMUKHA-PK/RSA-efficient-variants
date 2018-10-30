def multiplicative_inverse(e, phi):
    #Function to find multiplicative inverse modulo of a number.
    # Function parameters:
    #  e : Number of which multiplicative inverse is needed
    #  phi : This is the factor modulo of which the inverse is computed
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    # The inverse is found through one single iteration where the possibility of the number being the required number is computed
    while e > 0:
        temp1 = temp_phi/e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2
        
        x = x2- temp1* x1
        y = d - temp1 * y1
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    return d + phi