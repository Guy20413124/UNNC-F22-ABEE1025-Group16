from tkinter import END

import numpy as np
from numpy.linalg import inv,solve
from numpy import zeros,array,dot
class MatrixCalculation:
    @classmethod
    def Invertible_matrix(cls,textwindow1,textwindow2):
        '''
        O invertible matrix
        Text box input two window object, it will output the result in the text box 2
        :param textwindow1:The input window object
        :param textwindow2:The output window object
        :return:
        '''
        result = None
        string1 = textwindow1.get(0.0, END)
        '''
        Extracted from the input matrix
        '''
        Matrix_val = []
        string_list = string1.split('\n')
        for sl in string_list:
            sl2 = sl.split()
            if len(sl2)!=0:
                sl3 = []
                for i in range(len(sl2)):
                    sl3.append(float(sl2[i]))
                Matrix_val.append(sl3)
        Matrix_arr = np.array(Matrix_val)
        print(Matrix_arr)
        textwindow2.delete(0.0, END)
        try:
            result= inv(Matrix_arr)
            textwindow2.insert(0.0, result)
        except:
            textwindow2.insert(0.0, "Input is wrong, please read the instructions and enter again")
    @classmethod
    def Martix_dot(cls,textwindow1,textwindow2):
        '''
        The dot product for matrix
        Text box input two window object, it will output the result in the text box 2
        :param textwindow1:The input window object
        :param textwindow2:The output window object

        :return:
        '''
        result = None
        string1 = textwindow1.get(0.0, END)
        '''
        Extracted from the input matrix
        '''
        try:


            Matrix_val1 = []
            Matrix_val2 = []

            matrix_list = string1.split('X')

            string_list1 = matrix_list[0].split('\n')
            string_list2 = matrix_list[1].split('\n')
            for sl in string_list1:
                sl2 = sl.split()
                if len(sl2)!=0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val1.append(sl3)
            for sl in string_list2:
                sl2 = sl.split()
                if len(sl2)!=0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val2.append(sl3)
            len_row = len(Matrix_val1)
            len_col = len(Matrix_val1[0])
            print(Matrix_val1)
            print(Matrix_val2)
            Matrix_val3 = []
            for i in range(len_row):
                Mv3 = []
                for j in range(len_col):
                    Mv3.append(0)
                Matrix_val3.append(Mv3)
            for i in range(len_row):
                for j in range(len_col):
                    Matrix_val3[i][j] = Matrix_val1[i][j]*Matrix_val2[i][j]

            '''
            Join the answer
            '''
            textwindow2.delete(0.0, END)
            result = np.array(Matrix_val3)
            textwindow2.insert(0.0, result)
        except:
            textwindow2.insert(0.0, "Input is wrong, please read the instructions and enter again")
    @classmethod
    def Polynomial(cls,textwindow1,textwindow2):
        '''
        For multivariate the results of a type
        :param textwindow1:The input window object
        :param textwindow2:The output window object
        :return:
        '''

        try:
            result = None
            string1 = textwindow1.get(0.0, END)
            '''
                    Extracted from the input matrix
                    '''
            Matrix_val = []
            string_list = string1.split('\n')
            for sl in string_list:
                sl2 = sl.split()
                if len(sl2) != 0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val.append(sl3)
            A = zeros((len(Matrix_val), len(Matrix_val[0]) - 1))
            len_row = len(Matrix_val)
            len_col = len(Matrix_val[0])
            for i in range(len_row):
                for j in range(len_col-1):
                    A[i][j] = int(Matrix_val[i][j])
            B = []
            for x in range(len_row):
                B.append(int(Matrix_val[x][len(Matrix_val[0]) - 1]))
            print(A)
            print(B)
            result = solve(A,B)
            textwindow2.delete(0.0, END)
            textwindow2.insert(0.0, result)
        except:
            textwindow2.insert(0.0, "Input is wrong, please read the instructions and enter again")
    @classmethod
    def T(cls,textwindow1,textwindow2):
        '''
        O matrix transpose
        :param textwindow1:The input window object
        :param textwindow2:The output window object
        :return:
        '''
        result = None
        string1 = textwindow1.get(0.0, END)
        '''
                            Extracted from the input matrix
        '''
        Matrix_val = []
        string_list = string1.split('\n')
        for sl in string_list:
            sl2 = sl.split()
            if len(sl2) != 0:
                sl3 = []
                for i in range(len(sl2)):
                    sl3.append(float(sl2[i]))
                Matrix_val.append(sl3)
        Matrix_arr = np.array(Matrix_val)
        result = Matrix_arr.T

        textwindow2.delete(0.0, END)
        try:
            textwindow2.insert(0.0, result)
        except:
            textwindow2.insert(0.0, "Input is wrong, please read the instructions and enter again")
    @classmethod
    def plus(cls,textwindow1,textwindow2):
        '''
        Adding matrices
        Two matrices of addition
        :param textwindow1:The input window object
        :param textwindow2:The output window object
        :return:
        '''
        result = None
        string1 = textwindow1.get(0.0, END)
        '''
        Extracted from the input matrix
        '''
        try:

            Matrix_val1 = []
            Matrix_val2 = []

            matrix_list = string1.split('+')

            string_list1 = matrix_list[0].split('\n')
            string_list2 = matrix_list[1].split('\n')
            for sl in string_list1:
                sl2 = sl.split()
                if len(sl2) != 0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val1.append(sl3)
            for sl in string_list2:
                sl2 = sl.split()
                if len(sl2) != 0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val2.append(sl3)
            len_row = len(Matrix_val1)
            len_col = len(Matrix_val1[0])
            print(Matrix_val1)
            print(Matrix_val2)
            Matrix_val3 = []
            for i in range(len_row):
                Mv3 = []
                for j in range(len_col):
                    Mv3.append(0)
                Matrix_val3.append(Mv3)
            for i in range(len_row):
                for j in range(len_col):
                    Matrix_val3[i][j] = Matrix_val1[i][j] + Matrix_val2[i][j]

            '''
            Join the answer
            '''
            textwindow2.delete(0.0, END)
            result = np.array(Matrix_val3)
            textwindow2.insert(0.0, result)
        except:
            textwindow2.insert(0.0, "Input is wrong, please read the instructions and enter again")

    @classmethod
    def subtract(cls, textwindow1, textwindow2):
        '''
        Matrix by subtracting
        The subtraction of two matrix
        :param textwindow1:The input window object
        :param textwindow2:The output window object
        :return:
        '''
        result = None
        string1 = textwindow1.get(0.0, END)
        '''
        Extracted from the input matrix
        '''
        try:

            Matrix_val1 = []
            Matrix_val2 = []

            matrix_list = string1.split('-')

            string_list1 = matrix_list[0].split('\n')
            string_list2 = matrix_list[1].split('\n')
            for sl in string_list1:
                sl2 = sl.split()
                if len(sl2) != 0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val1.append(sl3)
            for sl in string_list2:
                sl2 = sl.split()
                if len(sl2) != 0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val2.append(sl3)
            len_row = len(Matrix_val1)
            len_col = len(Matrix_val1[0])
            print(Matrix_val1)
            print(Matrix_val2)
            Matrix_val3 = []
            for i in range(len_row):
                Mv3 = []
                for j in range(len_col):
                    Mv3.append(0)
                Matrix_val3.append(Mv3)
            for i in range(len_row):
                for j in range(len_col):
                    Matrix_val3[i][j] = Matrix_val1[i][j] - Matrix_val2[i][j]

            '''
            Join the answer
            '''
            textwindow2.delete(0.0, END)
            result = np.array(Matrix_val3)
            textwindow2.insert(0.0, result)
        except:
            textwindow2.insert(0.0, "Input is wrong, please read the instructions and enter again")

    @classmethod
    def multiplication(cls, textwindow1, textwindow2):
        '''
        Matrix multiplication
        Two matrix multiplication
        :param textwindow1:The input window object
        :param textwindow2:The output window object
        :return:
        '''
        result = None
        string1 = textwindow1.get(0.0, END)
        '''
                        Extracted from the input matrix
                        '''
        try:

            Matrix_val1 = []
            Matrix_val2 = []

            matrix_list = string1.split('X')

            string_list1 = matrix_list[0].split('\n')
            string_list2 = matrix_list[1].split('\n')
            for sl in string_list1:
                sl2 = sl.split()
                if len(sl2) != 0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val1.append(sl3)
            for sl in string_list2:
                sl2 = sl.split()
                if len(sl2) != 0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val2.append(sl3)
            len_row1 = len(Matrix_val1)
            len_col1 = len(Matrix_val1[0])
            len_row2 = len(Matrix_val2)
            len_col2 = len(Matrix_val2[0])
            if len_col1 != len_row2:
                raise AssertionError
            Matrix_val3 = []
            for i in range(len_row1):
                t = []
                for j in range(len_col2):
                    t.append(0)
                Matrix_val3.append(t)
            for i in range(len_row1):
                for j in range(len_col2):
                    for k in range(len_col1):
                        temp = Matrix_val1[i][k] * Matrix_val2[k][j]
                        Matrix_val3[i][j] += temp
            '''
            Join the answer
            '''
            textwindow2.delete(0.0, END)
            result = np.array(Matrix_val3)
            textwindow2.insert(0.0, result)
        except:
            textwindow2.insert(0.0, "Input is wrong, please read the instructions and enter again")


    @classmethod
    def square(cls, textwindow1, textwindow2):
        '''
        The square of matrix
        :param textwindow1:The input window object
        :param textwindow2:The output window object
        :return:
        '''
        result = None
        string1 = textwindow1.get(0.0, END)
        '''
                Extracted from the input matrix
                '''
        try:

            Matrix_val1 = []

            matrix_list = string1.split('X')

            string_list1 = matrix_list[0].split('\n')
            for sl in string_list1:
                sl2 = sl.split()
                if len(sl2) != 0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val1.append(sl3)
            len_row1 = len(Matrix_val1)
            len_col1 = len(Matrix_val1[0])
            if len_col1 != len_row1:
                raise AssertionError
            Matrix_val3 = []
            for i in range(len_row1):
                t = []
                for j in range(len_col1):
                    t.append(0)
                Matrix_val3.append(t)
            for i in range(len_row1):
                for j in range(len_col1):
                    for k in range(len_col1):
                        temp = Matrix_val1[i][k] * Matrix_val1[k][j]
                        Matrix_val3[i][j] += temp
            '''
            Join the answer
            '''
            textwindow2.delete(0.0, END)
            result = np.array(Matrix_val3)
            textwindow2.insert(0.0, result)
        except:
            textwindow2.insert(0.0, "Input is wrong, please read the instructions and enter again")

    @classmethod
    def eigenvalue(cls, textwindow1, textwindow2):
        '''
        Strives for the eigenvalues of the matrix
        :param textwindow1:The input window object
        :param textwindow2:The output window object
        :return:
        '''
        textwindow2.delete(0.0, END)
        try:
            result = None
            string1 = textwindow1.get(0.0, END)
            '''
            Extracted from the input matrix
            '''
            Matrix_val = []
            string_list = string1.split('\n')
            for sl in string_list:
                sl2 = sl.split()
                if len(sl2) != 0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val.append(sl3)
            Matrix_arr = np.array(Matrix_val)
            eigenvalue, featurevector = np.linalg.eig(Matrix_arr)
            result = eigenvalue

            textwindow2.insert(0.0, result)
        except:
            textwindow2.insert(0.0, "Input is wrong, please read the instructions and enter again")
    def featurevector(cls, textwindow1, textwindow2):
        '''
        Strives for the eigenvector of the matrix
        :param textwindow1:The input window object
        :param textwindow2:The output window object
        :return:
        '''
        textwindow2.delete(0.0, END)
        try:
            result = None
            string1 = textwindow1.get(0.0, END)
            '''
            Extracted from the input matrix
            '''
            Matrix_val = []
            string_list = string1.split('\n')
            for sl in string_list:
                sl2 = sl.split()
                if len(sl2) != 0:
                    sl3 = []
                    for i in range(len(sl2)):
                        sl3.append(float(sl2[i]))
                    Matrix_val.append(sl3)
            Matrix_arr = np.array(Matrix_val)
            eigenvalue, featurevector = np.linalg.eig(Matrix_arr)
            result = featurevector
            textwindow2.insert(0.0, result)
        except:
            textwindow2.insert(0.0, "Input is wrong, please read the instructions and enter again")



