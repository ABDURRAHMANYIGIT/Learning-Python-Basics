# -*- coding: utf-8 -*-

import sqlite3

def selectOperasyonlari():
    connection= sqlite3.connect("chinook.db")
    
    #cursor = connection.execute("""select FirstName , LastName from 
    #                            customers where city = 'Berlin'""")
    #
    #for row in cursor:
    #    print("First Name ="+ row[0])
    #    print("Last Name ="+ row[1])
    #    print("*******************")
        
        
    #cursor = connection.execute("""select city,count(*) from Customers 
    #                            group by city having count(*)>1 order by count(*) desc""")
    #
    #for row in cursor:
    #    print("City ="+ row[0])
    #    print("Count  ="+ str(row[1]))
    #    print("*******************")
        
    cursor = connection.execute("""select FirstName , LastName from 
                                customers where FirstName like 'a%'""")
    
    for row in cursor:
        print("First Name ="+ row[0])
        print("Last Name ="+ row[1])
        print("*******************")
    connection.close()
    
def insertOperasyonlari():
    connection= sqlite3.connect("chinook.db")
    
    connection.execute("""insert into customers 
                       (firstName,lastName,city,email) 
                       values ('Apo','Yiğit','Adana','apodurrahman.imran.yigit@outlook.com')""")
    connection.commit()
    connection.close()
    
#insertOperasyonlari()

def updateCustomer():
    connection= sqlite3.connect("chinook.db")
    
    connection.execute("""update customers set city = 'İstanbul' where city = 'Adana' """)
    connection.commit()
    connection.close()
    
updateCustomer()

def deleteCustomer():
    connection= sqlite3.connect("chinook.db")
    
    connection.execute("""delete from customers where customerid =66""")
    connection.commit()
    connection.close()
    
deleteCustomer()
    
    
    
    
    
    
    
    

