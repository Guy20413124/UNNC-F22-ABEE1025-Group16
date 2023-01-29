from os.path import exists
from tkinter import  messagebox
class explain:
    @classmethod
    def make_explain(cls):
        if exists("help.txt"):
            pass
        else:  # this is what you type in to the text
            f = open("help.txt", 'x+')
            f.write("+++++++++++++++++++The program function and the sample input below+++++++++++++++++++\n")
            f.write("1.O invertible matrix,matters need attention:\n")
            f.write("O invertible matrix only need to input a matrix, the input sample\n")
            f.write("1 2 3\n")
            f.write("1 2 3\n")
            f.write("1 2 3\n")
            f.write("Pay attention to the adjacent two Numbers separated by a space\n")
            f.write("2.Matrix of the dot product, need to enter two matrix,\n")
            f.write(" input matrix method as well as the middle with the capital of the 'X', input sample：\n")
            f.write("1 2 3\n")
            f.write("1 2 3\n")
            f.write("1 2 3\n")
            f.write("X\n")
            f.write("1 2 3\n")
            f.write("1 2 3\n")
            f.write("1 2 3\n")
            f.write("3.Multiple solutions of a type, in the process, you just need to the unknown coefficient (signed) equals sign and add and subtract Numbers do not need to write, output sample：\n")
            f.write("If you want to askX+Y=0,3X+2Y=9,so the input\n")
            f.write("1 1 0\n")
            f.write("3 2 9\n")
            f.write("Adjacent Numbers separated by a space\n")
            f.write("4.Transposed matrix\n")
            f.write("The input and invertible matrix input is the same\n")
            f.write("5.For matrix and matrix the dot product of the same knowledge could become a '+' to 'X'\n")
            f.write("6.Matrix multiplication'\n")
            f.write("    2 as input and function\n")
            f.write("7.The square of matrix'\n")
            f.write("    1 as input and function\n")
            f.write("8.Strives for the eigenvalues of the matrix'\n")
            f.write("    1 as input and function\n")
            f.write("9.Strives for the featurevector of the matrix'\n")
            f.write("    1 as input and function\n")
            messagebox.showinfo(title="help", message="In the same directory is written documents“help.txt”,Please check in the document")
