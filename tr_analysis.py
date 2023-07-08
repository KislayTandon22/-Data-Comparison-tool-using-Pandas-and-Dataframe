# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 09:09:06 2020

@author: hp
"""

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
    



def analysis_data():
    
    df = pd.read_csv('f:\passenger2.csv',names=['Rtno','Area_Covered','Capacity','Noofstudents','Distance','Charges','Transporter'],skiprows=1)
    while(True):
        print(analysis_menu)
        ch=int(input("Enter choice" ))
        if ch==1:
            df.plot('Noofstudents','Capacity',color='b',linestyle='-',linewidth=2,marker='o',markersize=8)
            plt.ylabel('Capacity in a Bus',fontsize=12)
            plt.xlabel('No of Students',fontsize=12)
            plt.title('No of Students / Capacity in Bus',fontsize=14)
            plt.grid(True)
            plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
            plt.show()
            
        elif ch==2:
            df.plot.bar('Noofstudents','Capacity',color='g',edgecolor='r')
            plt.ylabel('Capacity in a Bus',fontsize=12)
            plt.xlabel('No of Students',fontsize=12)
            plt.title('No of Students / Capacity in Bus',fontsize=14)
            plt.show()
            
        elif ch==3:
            df.plot.bar('Area_Covered','Capacity',color='g',edgecolor='r')
            plt.ylabel('Capacity in a Bus',fontsize=12)
            plt.xlabel('Area Covered',fontsize=12)
            plt.title('Area Covered / Capacity in Bus',fontsize=14)
            plt.show()   
            
        elif ch==4:
            plt.pie(df.Noofstudents, labels=df.Area_Covered,autopct='%.1f%%')
            plt.show()
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
    