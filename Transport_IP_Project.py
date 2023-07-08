
import matplotlib.pyplot as plt
import csv
import pandas as pd
import os

main_menu='''\n\n Main Menu-------:
0 To add performance record of quarter jan 2020-march 2020 
1 To change perfromance record of quarter jan 2020-march 2020 
2 To display quaterly performance district  
3 To analysis quaternary perfromance
4 To delete performance record 
5 To update performance record
6. Exit'''

display_menu='''     ----Display DATA MENU----
1: All Data 
2: bottom five performance(avg) in quarter jan2020- march 2020
3: top five performance in quarter jan2020- march 2020
4: specific performance of a district
5: facility type performance of different districts
6: Display Selected Columns 
--  Return to Main Menu'''

analysis_menu='''     ----Analysis DATA MENU----
1: Line Chart(performance min(AVG))
2: Bar Chart (perfromance max (avg) v/s facility type)
3: Bar chart (facility vs no of facilities )
4: Pie Chart (facility vs no of facilities) "))
--- Return to Main Menu'''


def display_data():
    
    df=pd.read_csv('D:\ip project\hmis-deliveries_conducted_at_facility-2019-20-raj-Jan_to_Mar.csv',names=['District','Facility_Type','Total_No._of_Facilities #','No._of_facilities_reporting_nil_performance *','Performance-Overall_Average **','Performance-Maximum','Performance-Minimum'
],skiprows=1)
    while(True):
        print(display_menu)
        ch=int(input("Enter Choice "))
        if ch==1:
            print(df)
        elif ch==2:
            print(df.sort_values(by=['Performance-Overall_Average **']).head(5))
        elif ch==3:
            print(df.sort_values(by=['Performance-Overall_Average **']).tail(5))
        elif ch==4:
            n=input('\nEnter name of district -> ')
            df1=df[df.District==n]
            if df1.empty:
                print('\n........No such city record is present..........\n')
            else:
                print(df1)
            print()
        elif ch==5:
            print('\nAvailable facility  ->   ',df.Facility_Type.unique())
            Tr=input('\nEnter Facility_Type -> ')
            df1=df[df.Facility_Type==Tr]
            if df1.empty:
                print('\nNo such Facility_Type available in -> ',Tr)
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


def input_data():
    
    
    with open('D:\ip project\hmis-deliveries_conducted_at_facility-2019-20-raj-Jan_to_Mar.csv', mode='w') as pass_file:
        pass_writer = csv.writer(pass_file, delimiter=',')
        n=int(input("how many records : "))
        for i in range(n):
            rno=input("Enter District :")
            ac=input("Facility_Type :")
            cap=int(input("Total_No._of Facilities #"))
            ns=int(input("No._of_facilities_reporting_nil_performance *"))
            dis=int(input("Performance-Overall_Average **"))
            ch=int(input("Performance-Maximum"))
            tr=int(input("Performance-Minimum"))
            aa=[rno,ac,cap,ns,dis,ch,tr]
            pass_writer.writerow(aa)
    
    df= pd.read_csv('D:\ip project\hmis-deliveries_conducted_at_facility-2019-20-raj-Jan_to_Mar.csv',names=['District','Facility_Type','Total_No._of Facilities #','No._of_facilities_reporting_nil_performance *','Performance-Overall_Average **','Performance-Maximum','Performance-Minimum'])
    print(df)
    

def append_data():
     
    with open('D:\ip project\hmis-deliveries_conducted_at_facility-2019-20-raj-Jan_to_Mar.csv', mode='a') as pass_file:
        pass_writer = csv.writer(pass_file, delimiter=',')
        rno=input("Enter District :")
        ac=input("Facility_Type :")
        cap=int(input("Total_No._of Facilities #"))
        ns=int(input("No._of_facilities_reporting_nil_performance *"))
        dis=int(input("Performance-Overall_Average **"))
        ch=int(input("Performance-Maximum"))
        tr=int(input("Performance-Minimum"))
        aa=[rno,ac,cap,ns,dis,ch,tr]
        pass_writer.writerow(aa)
    
    df = pd.read_csv('D:\ip project\hmis-deliveries_conducted_at_facility-2019-20-raj-Jan_to_Mar.csv',header=None)
    print(df)


def analysis_data():
    
    df = pd.read_csv('D:\ip project\PTI.csv',names=['facility','performmance_AVG','no_of_facilities','performance_max(AVG)','performance_min(avg)']
,skiprows=1)
    while(True):
        print(analysis_menu)
        ch=int(input("Enter choice" ))
        if ch==1:
            
            df.plot('facility','performance_min(avg)',color='k',linestyle='-',linewidth=2,marker='o',markersize=8)
            plt.ylabel('performance ',fontsize=12)
            plt.xlabel('facility',fontsize=12)
            plt.title('performmance min (avg) / facility',fontsize=14)
            plt.grid(True)
            plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
            plt.show()
            
        elif ch==2:
            df.plot.bar('facility','performmance_AVG',color='g',edgecolor='r')
            plt.ylabel('Perfromance avg',fontsize=12)
            plt.xlabel('Facility',fontsize=12)
            plt.title('Facility wise avg performnace',fontsize=14)
            plt.show()
            
        elif ch==3:
            df.plot.bar('facility','no_of_facilities',color='g',edgecolor='r')
            plt.ylabel('No of facilities',fontsize=12)
            plt.xlabel('facility',fontsize=12)
            plt.title('No of particular facility',fontsize=14)
            plt.show()   
            
        elif ch==4:
            plt.pie(df.no_of_facilities, labels=df.facility,autopct='%.1f%%')
            plt.show()
        else:
            break



def remove_data():
    df = pd.read_csv('D:\ip project\hmis-deliveries_conducted_at_facility-2019-20-raj-Jan_to_Mar.csv',names=['District','Facility_Type','Total_No._of Facilities #','No._of_facilities_reporting_nil_performance *','Performance-Overall_Average **','Performance-Maximum','Performance-Minimum'],skiprows=1)
    print(df)
    n=input('Enter the row index number for deletion ->  ')
    df.drop(n,inplace=True)
    print(df)
    print('\n------------Record deleted from Data Frame---------------')
    ch=input("Wnat to change in CSV file")
    if ch in 'yY':
        df.to_csv(r"D:\ip project\new_pass2.csv",index=False,sep=',')
        print('\nData Written in [new_pass.csv] file.........\n\n')
        
    os.remove("D:\ip project\hmis-deliveries_conducted_at_facility-2019-20-raj-Jan_to_Mar.csv")
    os.rename(r"D:\ip project\new_pass2.csv",r"D:\ip project\hmis-deliveries_conducted_at_facility-2019-20-raj-Jan_to_Mar.csv")
    

def update_data():
        
    df = pd.read_csv('D:\ip project\hmis-deliveries_conducted_at_facility-2019-20-raj-Jan_to_Mar.csv',names=['District','Facility_Type','Total_No._of Facilities #','No._of_facilities_reporting_nil_performance *','Performance-Overall_Average **','Performance-Maximum','Performance-Minimum'])
    print(df)
    rno=input('Enter district(it should be of same index) ->  ')
    pno=input('Enter Facility_Type(it should be of same index) ->  ')
    ns1=int(input('Enter new performance("Total_No._of Facilities ")( ->  '))
    ns2=int(input('Enter new (No._of_facilities_reporting_nil_performance *)( ->  '))
    ns3=int(input('Enter new (Performance-Overall_Average **)( ->  '))
    ns4=int(input('Enter new (Performance-Maximum)( ->  '))
    ns5=int(input('Enter new (Performance-Minimum)( ->  '))
    df.loc[df['District'] == rno,df['Facility_Type'] == pno, 'Total_No._of Facilities #','No._of_facilities_reporting_nil_performance *','Performance-Overall_Average **','Performance-Maximum','Performance-Minimum'] = ns1,ns2,ns3,ns4,ns5
    print(df)
    ch=input("Wnat to change in CSV file")
    if ch in 'yY':
      df.to_csv(r"D:\ip project\new_pass2.csv",index=False,sep=',')
    print('\nData Written in [new_pass.csv] file.........\n\n')
            
    os.remove("D:\ip project\hmis-deliveries_conducted_at_facility-2019-20-raj-Jan_to_Mar.csv")
    os.rename(r"D:\ip project\new_pass2.csv",r"D:\ip project\hmis-deliveries_conducted_at_facility-2019-20-raj-Jan_to_Mar.csv")    
    print('\n------------Record Modified---------------')
        
    
    
    

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

