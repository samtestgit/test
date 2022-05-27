import mysql.connector
from tabulate import tabulate
flag=1
flag1=1

def sql_path(i):
    global myresult



    mydb = mysql.connector.connect(
        host="testadmin.c9niue7olmv5.ap-south-1.rds.amazonaws.com",
        user="testadmin",
        passwd="testadmin123",
        database="information_schema"
    )

#NEw code to chek
#if it is working
#or not


    mycursor = mydb.cursor()
    mycursor.execute("select * from collations where ID= '%s'", [i])
    myresult = mycursor.fetchall()
    print("new:",tabulate(myresult, tablefmt='psql'))
    print("my:",myresult)


#File Handeling
#open in put file
var = open("E:\Python\input.txt",'r')
var2 = open("E:\Python\summary.txt", 'a')
var1 = open("E:\Python\output.txt", 'a')
#print(var.readlines())

#x =''
for i in var.readlines():
    print("i:",i)

    i=int(i)
    sql_path(i)
    print("myresult:", myresult)
    #myresult =str(myresult)
    for x in myresult:
        print("x:",x)
        if x == "":
        #var2 = open("E:\Python\summary.txt", 'a')
            #var2.writelines(x)
            var2.writelines(tabulate(myresult,headers=['desc','value','num','ques','ques1','num1'], tablefmt='mysql'))
            #var2.close()
        else:
        #var1 = open("E:\Python\output.txt", 'a')
            #var1.writelines(x)
            var1.writelines(tabulate(myresult, tablefmt='mysql'))
            #var1.close()


#print(mydb)
#pr_list=[]
#file("E:\Python\input.txt",pr_list)
#Close inout file
var.close()
var1.close()
var2.close()





