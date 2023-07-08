# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 08:41:16 2020

@author: hp
"""

import matplotlib.pyplot as plt
import csv
import pandas as pd
import os

main_menu='''\n\n Main Menu-------:
0 To write data
1 To append
2 To display data
3 To analysis data
4 To delete
5 To update
6. Exit'''

display_menu='''     ----Display DATA MENU----
1: All Data 
2: First Five Records
3: Last Five Record
4: Specific Routeno Record
5: Unique Transporters
6: Display Selected Columns 
--  Return to Main Menu'''

analysis_menu='''     ----Analysis DATA MENU----
1: Line Chart(Capacity/No of students)
2: Bar Chart (Capacity/No of students)
3: Bar Chart (Area Covered / Capacity)
4: Pie Chart (Area Covered / No of Studenst) "))
--- Return to Main Menu'''
def display_data():
    
    df=pd.read_csv('f:\passenger2.csv',names=['Rtno','Area_Covered','Capacity','Noofstudents','Distance','Charges','Transporter'],skiprows=1)
    while(True):
        print(display_menu)
        ch=int(input("Enter Choice "))
        if ch==1:
            print(df)
        elif ch==2:
            print(df.head(5))
        elif ch==3:
            print(df.tail(5))
        elif ch==4:
            n=int(input('\nEnter Route number for search -> '))
            df1=df[df.Rtno==n]
            if df1.empty:
                print('\n........No such Route Available..........\n')
            else:
                print(df1)
            print()
        elif ch==5:
            print('\nAvailable Transporters  ->   ',df.Transporter.unique())
            Tr=input('\nEnter Transporter Name -> ')
            df1=df[df.Transporter==Tr]
            if df1.empty:
                print('\nNo such Transporter available in -> ',Tr)
            else:
                print(df1)
            print()
        elif ch==6:
            print('\nList of Columns are')
            for x in df.columns:
                print(x,end=', ')
            clist=[]
            while True:
                c=input('\nEnter column name -> ')
                clist.append(c)
                ch=input('Want to give more column name-> ')
                if ch in 'nN':
                    break
            print('Details of Selected columns data')
            print(df[clist])
            print()
        else:
            break
    
while(True):
    print(main_menu)
    choice=int(input("Enter choice: "))
    if choice==0:
        input_data()
    elif choice==1:
        append_data() 
    elif choice==2:
        display_data()
    elif choice==3:
        analysis_data()
    elif choice==4:
        remove_data()
    elif choice==5:
        update_data()
    elif choice==6:
        print("Ending Project")
        break