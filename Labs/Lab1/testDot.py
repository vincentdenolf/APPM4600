"""
 This program is a warm up for coding. You get used to the coding 
format and practice some coding skills. 
"""

############################################# 
"""
Copyright (C) 2025  Adrianna M. Gillman

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
############################################# 

#import packages
import numpy as np
import numpy.linalg as la
import math

def driver():

     n = 100
     x = np.linspace(0,np.pi,n)

# this is a function handle.  You can use it to define 
# functions instead of using a subroutine like you 
# have to in a true low level language.     
     f = lambda x: x**2 + 4*x + 2*np.exp(x)
     g = lambda x: 6*x**3 + 2*np.sin(x)

     y = f(x)
     w = g(x)

# evaluate the dot product of y and w     
     dp = dotProduct(y,w,n)

# print the output
     print('the dot product is : ', dp)

# test
# define matrix and vector to multiply
     A = np.ndarray([2,3],[5,6])
     v = np.array([2,3])

# find matrix product of A and v
     mp = matrixVectorProduct(A,v,n)
     return
     
def dotProduct(x,y,n):
#   Computes the dot product of the n x 1 vectors x and y
     dp = 0.
     for j in range(n):
        dp = dp + x[j]*y[j]

     return dp  
# this is for testing commits!
def matrixVectorProduct(A,x,n):
# computes the product of an n x n matrix and the n x 1 vector x
     mp = 0
     for i in range(n):
          for j in range(n):
               mp = mp + A[i,j]*x[j]

     return mp
driver()               


# this code was never finished