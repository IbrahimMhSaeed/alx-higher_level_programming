
def add(x, y):
    """Add function"""
    return x + y

def sub(x, y):
    """Sub function"""
    return x - y

def mul(x, y):
    """Mul function"""
    return x * y

def div(x, y):
    """Div function"""
    if y == 0:
        raise ValueError("Can't divide by zero")
    else:
        return x / y
