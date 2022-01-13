
def pow(base, exponent):
    if exponent == 0:
        return(1)
    elif exponent > 0:
        base1 = base
        while exponent > 1:
            base1 = base1 * base
            exponent -= 1
        return(base1)
    else:
        return(1/pow(base, exponent * -1))

