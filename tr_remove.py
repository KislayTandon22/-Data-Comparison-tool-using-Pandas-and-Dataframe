# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:18:12 2020

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
    







def remove_data():
    df = pd.read_csv('f:\passenger2.csv',names=['Rtno','Area_Covered','Capacity','Noofstudents','Distance','Charges','Transporter'])
    print(df)
    n=int(input('Enter the row index number for deletion ->  '))
    df.drop(n,inplace=True)
    print(df)
    print('\n------------Record deleted from Data Frame---------------')
    ch=input("Wnat to change in CSV file")
    if ch in 'yY':
        df.to_csv(r"C:\WORKSHOP\new_pass2.csv",index=False,sep=',')
        print('\nData Written in [new_pass.csv] file.........\n\n')
        
    os.remove("f:\passenger2.csv")
    os.rename(r"c:\\workshop\new_pass2.csv",r"f:\passenger2.csv")




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
    
    