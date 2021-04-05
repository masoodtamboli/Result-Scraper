import requests
from bs4 import BeautifulSoup
import csv

def cm1i(start1, end1):
    seat = ""
    total = "" 
    remarks = "" 
    percentage = "" 
    subjects = ['ENGLISH','BASIC SCIENCE','BASIC MATHEMATICS','FUNDAMENTALS OF ICT','ENGINEERING GRAPHICS','WORKSHOP PRACTICE']
    marks = []
    short_sub = ['ENG','BSC','BMA','ICT','EGE','WPC']
    headers = ["seat no"]
    start = start1
    end = end1
    #for headers
    for subject in short_sub:
        if subject=="ENG" or subject=="BSC":
            headers.append(subject+"(TH)")
            headers.append(subject+"(PR)")	
        else:
            headers.append(subject+"(PR)")

    final_header = headers + ['total marks','percentage','remarks']
    with open("H:\\GP\\VI sem\\Python Projrct\\1st.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(final_header)

    for seat_number in range(start,end):
        URL = "http://msbte.org.in/SHTFNL20BTERESLIVE/SHTFNL20BTERESLIVE/SeatNumber/17/"+str(seat_number)+"Marksheet.html"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content,'html.parser')
        #seat-no
        seat = soup.find('td',text="SEAT NO.").find_next('td').text
        marks.append(seat)
        #for getting marks
        for subject in subjects:
            var=soup.find('td',text=subject)
            for i in range(36):
                if subject=="ENGLISH" or subject=="BASIC SCIENCE":
                    if(i==7):
                        marks.append(var.text)
                    if(i==25):
                        marks.append(var.text)
                    var = var.find_next('td')
                else:
                    if(i==7):
                        marks.append(var.text)
                    var = var.find_next('td')

        #for getting total,percentage,remarks
        total = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[2].text
        percentage = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[1].text
        remarks = soup.find_all('table')[2].find_all('tr')[2].find_all('td')[1].text
        
        marks.append(total)
        marks.append(percentage)
        marks.append(remarks)
        #add to the excel sheet
        with open("C:\\Users\\Hacker\\Desktop\\1st.csv", 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(marks)
        del marks[:]

def cm3i(start1, end1):
    seat = ""
    total = "" 
    remarks = "" 
    percentage = "" 
    subjects = ['OBJECT ORIENTED PROGRAMMING USING C++', 'DATA STRUCTURE USING C', 'COMPUTER GRAPHICS', 'DATABASE MANAGEMENT SYSTEM', 'DIGITAL TECHNIQUES']
    marks = []
    short_sub = ['OOP','DSU','CGR','DBMS','DT']
    headers = ["seat no"]
    start = start1
    end = end1
    #for headers
    for subject in short_sub:
        headers.append(subject+"(TH)")
        headers.append(subject+"(PR)")

    final_header = headers + ['total marks','percentage','remarks']
    with open("H:\\GP\\VI sem\\Python Projrct\\2nd.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(final_header)

    for seat_number in range(start,end):
        URL = "http://msbte.org.in/SHTFNL20BTERESLIVE/SHTFNL20BTERESLIVE/SeatNumber/17/"+str(seat_number)+"Marksheet.html"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content,'html.parser')
        #seat-no
        seat = soup.find('td',text="SEAT NO.").find_next('td').text
        marks.append(seat)
        #for getting marks
        for subject in subjects:
            var=soup.find('td',text=subject)
            for i in range(36):
                if(i==7):
                    marks.append(var.text)
                if(i==25):
                    marks.append(var.text)
                var = var.find_next('td')

        #for getting total,percentage,remarks
        total = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[2].text
        percentage = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[1].text
        remarks = soup.find_all('table')[2].find_all('tr')[2].find_all('td')[1].text
        
        marks.append(total)
        marks.append(percentage)
        marks.append(remarks)
        #add to the excel sheet
        with open("C:\\Users\\Hacker\\Desktop\\2nd.csv", 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(marks)
        del marks[:]

def cm5i(start1, end1):
    seat = ""
    total = "" 
    remarks = "" 
    percentage = "" 
    subjects = ['ENVIRONMENTAL STUDIES','OPERATING SYSTEMS','ADVANCED JAVA PROGRAMMING','SOFTWARE TESTING','CLIENT SIDE SCRIPTING LANGUAGE','INDUSTRIAL TRAINING','CAPSTONE PROJECT PLANNING']
    marks = []
    short_sub = ['EST','OSY','AJP','STE','CSS','ITR','CPP']
    headers = ["seat no"]
    start = start1
    end = end1
       #for headers
    for subject in short_sub:
        if subject=="OSY" or subject=="AJP" or subject=="STE" or subject=="CSS":
            headers.append(subject+"(TH)")
            headers.append(subject+"(PR)")
        else:
            headers.append(subject+"(PR)")

    final_header = headers + ['total marks','percentage','remarks']
    with open("H:\\GP\\VI sem\\Python Projrct\\3rd.csv", 'w', newline='') as f:
        w = csv.writer(f)
        w.writerow(final_header)

    for seat_number in range(start,end):
        URL = "http://msbte.org.in/SHTFNL20BTERESLIVE/SHTFNL20BTERESLIVE/SeatNumber/17/"+str(seat_number)+"Marksheet.html"
        r = requests.get(URL)
        soup = BeautifulSoup(r.content,'html.parser')
        #seat-no
        seat = soup.find('td',text="SEAT NO.").find_next('td').text
        marks.append(seat)
        #for getting marks
        for subject in subjects:
            var=soup.find('td',text=subject)
            for i in range(36):
                if subject=="OPERATING SYSTEMS" or subject=="ADVANCED JAVA PROGRAMMING" or subject=="SOFTWARE TESTING" or subject=="CLIENT SIDE SCRIPTING LANGUAGE":
                    if(i==7):
                        marks.append(var.text)
                    if(i==25):
                        marks.append(var.text)
                    var = var.find_next('td')
                else:
                    if(i==7):
                        marks.append(var.text)
                    var = var.find_next('td')

        #for getting total,percentage,remarks
        total = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[2].text
        percentage = soup.find_all('table')[2].find_all('tr')[1].find_all('td')[1].text
        remarks = soup.find_all('table')[2].find_all('tr')[2].find_all('td')[1].text
        
        marks.append(total)
        marks.append(percentage)
        marks.append(remarks)
        #add to the excel sheet
        with open("C:\\Users\\Hacker\\Desktop\\3rd.csv", 'a', newline='') as f:
            w = csv.writer(f)
            w.writerow(marks)
        del marks[:]

print("\n================MSBTE RESULT DOWNLOADER===============")
print("\n  Select Semester")
print("  1. CM1I")
print("  2. CM2I")
print("  3. CM3I")
print("  4. CM4I")
print("  5. CM5I")
print("  6. CM6I")
semester = int(input("\n >"))
print("  You have selected Smester :",semester)
if semester==1:
    start = int(input("  Enter start seat number : "))
    end = int(input("  Enter End seat number : "))
    print("  Results for CM1I are being fetched this takes a moment...")
    cm1i(start,end)
if semester==2:
    print("  No reults availabe for CM2I")
if semester==3:
    start = int(input("  Enter start seat number : "))
    end = int(input("  Enter End seat number : "))
    print("  Results for CM3I are being fetched this takes a moment...")
    cm3i(start,end)
if semester==4:
    print("  No reults availabe for CM4I")
if semester==5:
    start = int(input("  Enter start seat number : "))
    end = int(input("  Enter End seat number : "))
    print("  Results for CM5I are being fetched this takes a moment...")
    cm5i(start,end)
if semester==6:
    print("  No reults availabe for CM6I")
print("  Fetching is done check out your CSV file")
