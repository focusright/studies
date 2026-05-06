import sys
import numpy as np
from fractions import Fraction

def get_args():
    arg_length = len(sys.argv)
    v  = np.array(eval(sys.argv[1]))
    basis = []
    print("\nv = " + str(v))
    basis_count = 0
    for arg in sys.argv[2:]:
        b = eval(arg)
        b = np.array(b)
        basis.append(b)
        basis_count += 1
        print("b" + str(basis_count) + " = " + str(b))
    num_of_elements = len(v)
    num_of_basis = len(basis)
    if num_of_elements != num_of_basis:
        print('\nUsage: python change-basis.py {v} {b1} {b2} ...')
        print('sMake sure there are no spaces in the arrays.')
        print('The dimensions of the arrays must match the number of basis vectors.')
        print('Example: python change-basis.py [5,-1] [1,1] [1,-1]')
        print('Example: python change-basis.py [10,-5] [3,4] [4,-3]')
        print('Example: python change-basis.py [2,2] [-3,1] [1,3]')
        print('Example: python change-basis.py [1,1,1] [2,1,0] [1,-2,-1] [-1,2,-5]')
        print('Example: python change-basis.py [1,1,2,3] [1,0,0,0] [0,2,-1,0] [0,1,2,0] [0,0,0,3]')
        exit(1)

    return v, basis

def change_basis(v, basis):
    scalars = []
    for b in basis:
        v_dot_b = v.dot(b)
        b_mag_squared = b.dot(b)
        s = v_dot_b / b_mag_squared
        scalars.append(s)
    print("Result as decimals: " + str(scalars))
    print("Result as fractions: [", end="", flush=True) 
    for s in scalars:
        print(str(Fraction(s).limit_denominator()) + ", ", end="", flush=True)
    print("]")

if __name__ == "__main__":
    v, basis = get_args()
    change_basis(v, basis)
