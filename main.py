#coding=gbk
from tkinter import  Tk,Menu,Text
from MatrixCalculation import MatrixCalculation as mc
from Explain import explain
def main():
    '''
    Create the GUI window, guides the user input and option,
    and then call the corresponding calculation method to calculate and display the results
    :return:
    '''
    GUIwindow=Tk()   #Create the GUI window

    GUIwindow.title("Matrix Calculator")

    GUIwindow.geometry("800x450+500+250")

    GUIwindow.minsize(300,400)#The minimum Settings window

    textwindow1=Text(GUIwindow,width=180,height=11,font=('Calibri 12  italic'))#Create a text box
    textwindow2=Text(GUIwindow,width=180,height=20,font=('Calibri 12  italic'))#Create a second text boxes

    textwindow1.grid(row=0,column=0)#Place text box


    textwindow1.insert(0.0, "Please click on the 'help' to view the use of the simple matrix processor\nyour input should conform to the sample in the documentation to get the answer")#在第一个文本框中插入字符串


    textwindow2.grid(row=20,column=0)
    window_menu_all=Menu(GUIwindow)#Create a total menu


    window_menu1=Menu(window_menu_all,tearoff=0)#Create the main menu

    window_menu1.add_command(label="1.O invertible matrix",command=lambda : mc.Invertible_matrix(textwindow1,textwindow2))#Create a deputy menu

    window_menu1.add_command(label ='2.Matrix is the dot product',command=lambda : mc.Martix_dot(textwindow1,textwindow2))
    window_menu1.add_command(label ='3.Multiple results of a type o matrix',command=lambda : mc.Polynomial(textwindow1,textwindow2))
    window_menu1.add_command(label ='4.Transpose matrix',command=lambda : mc.T(textwindow1,textwindow2))
    window_menu1.add_command(label ='5.Matrix addition',command=lambda : mc.plus(textwindow1,textwindow2))
    window_menu1.add_command(label ='6.Matrix multiplication',command=lambda : mc.multiplication(textwindow1,textwindow2))
    window_menu1.add_command(label ='7.The square of matrix',command=lambda : mc.square(textwindow1,textwindow2))
    window_menu1.add_command(label ='8.Eigenvalue',command=lambda : mc.eigenvalue(textwindow1,textwindow2))
    window_menu1.add_command(label ='9.Featurevector',command=lambda : mc.featurevector(textwindow1,textwindow2))


    window_menu_all.add_cascade(label="formula mode",menu=window_menu1,font=('Calibri 12 '))#Create a deputy menu

    window_menu2=Menu(window_menu_all,tearoff=0)#Create the main menu
    window_menu2.add_command(label="Input considerations",command=lambda : explain.make_explain())#Create a deputy menu
    window_menu_all.add_cascade(label='help',menu=window_menu2,font=('Calibri 12 '))#Total menu display
    GUIwindow.config(menu=window_menu_all)#According to the main menu
    GUIwindow.mainloop()
if __name__ == '__main__':
    main()
