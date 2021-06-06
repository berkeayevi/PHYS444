# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 13:10:22 2021

@author: BerkeAyevi
"""


def zero_vector(x):#Creates 0 vector in given length returns as v
    v = []#Empty array
    for i in range(x):
        v.append(0.0)#add 0.0
    return v

def maxvalues(matrix):#Takes the matrix and finds it's max values on each row
    length = len(matrix)
    maxvector = zero_vector(length)
    for i in range(length):
        maxval= 0.0
        for j in range(length):
            val = abs(matrix[i][j])
            if (val> maxval):
                maxval = val
        maxvector[i]= maxval

    return maxvector
def Forward_Elimination(matrix1,matrix2,index,opnum,length): #Forward Elimination method

    for i in range(opnum+1,length):#step by step calculation taken form the slayts pg no:20-21
        mul = (matrix1[index[i]][opnum])/ matrix1[index[opnum]][opnum]
        for j in range(opnum,length):
            matrix1[index[i]][j] -= mul* matrix1[index[opnum]][j]
        matrix2[index[i]] -= mul* matrix2[index[opnum]]

    return matrix1,matrix2

def Backward_Substition(matrix,solution,index,x,length): #Backwawrd Substition method

    x[length-1]= solution[index[length-1]]/matrix[index[length-1]][length-1] # Frist Element
    for i in range(length-2,-1,-1):#step by step calculation taken form the slayts pg no:22
        tot = 0.0
        for j in range(i+1,length):
            tot += x[j]*matrix[index[i]][j]
        x[i]= (solution[index[i]]-tot)/ matrix[index[i]][i]

    return x

def gaussian(matrix,solution):#main function takes 2 matrices
    length =(len(matrix))# takes length of the matrix
    index = list(range(length))# creates a vector starting from 0 to length-1
    scale = maxvalues(matrix)#creates scale vector from max row elements of matrix
    x = zero_vector(length)# creates 0 matrix given lentgh

    for n in range(length-1):                   #Do it until xn-1 eliminated
        maxval = 0.0
        for i in range(n, length):
            ratios= (abs(matrix[index[i]][n])) / float(scale[index[i]])#Calculation taken form the slayts pg 33
            if ratios > maxval:
                maxval= ratios
                temp= i
        temp1 = index[n]
        index[n] = index[temp]
        index[temp] = temp1

        matrix, solution = Forward_Elimination(matrix,solution,index,n,length)

    x = Backward_Substition(matrix,solution,index,x,length)

    return x



matrix = [
    [53,48,71],
    [94,58,86],
    [25,35,45],
    ]




solution =[30,90,55]
a = gaussian(matrix,solution)


print(a)