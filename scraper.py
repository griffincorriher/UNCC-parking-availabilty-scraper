#import libraries
from datetime import date, datetime, time
import time
import mysql.connector as mysql
from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession
import re

def scrape():
    #Scrape website
    global allInfoList
    global info1
    global info2
    global info3
    global info4
    global info5
    global info6
    global info7
    global info8
    global info9
    global info10    
    max = 100
    
    session = HTMLSession()
    resp = session.get("https://parkingavailability.uncc.edu/")
    resp.html.render()
    soup = BeautifulSoup(resp.html.html, "lxml")
    resp.html.render(timeout=20)
    
    #Get required info
    allInfo = soup.find_all("mat-list-item")
    allInfoList = [tag.text for tag in allInfo]

    #Clean up info
    for parkingDecks in allInfoList:
        parkingDecks = parkingDecks.replace('\n',' ').replace('place','').replace('star_border','')
        #print(parkingDecks)

    info1 = allInfoList[0].split("\n")
    info2 = allInfoList[1].split("\n")
    info3 = allInfoList[2].split("\n")
    info4 = allInfoList[3].split("\n")
    info5 = allInfoList[4].split("\n")
    info6 = allInfoList[5].split("\n")
    info7 = allInfoList[6].split("\n")
    info8 = allInfoList[7].split("\n")
    info9 = allInfoList[8].split("\n")
    info10 = allInfoList[9].split("\n")


        
def database():
    now = datetime.now()
    time = now.strftime('%H:%M:%S')
    date = now.strftime('%Y-%m-%d')
    day = now.strftime('%A')
    db = mysql.connect(
        host = "localhost",
        user = "root",
        passwd = "Letter69!",
        database = "parkinginformation"
    )
    #print(db)
    cursor = db.cursor()
    
    sql = "INSERT INTO parking (date, day, time, name, cap) VALUES (%s, %s, %s, %s, %s)"
    query = "SELECT * FROM parking"
    dropDB = "DROP DATABASE parkinginformation2"
    createDB = "CREATE DATABASE parkinginformation"
    dropTable = "DROP TABLE parking"
    createTable = "CREATE TABLE parking (ID int PRIMARY KEY AUTO_INCREMENT, date VARCHAR(100), day VARCHAR(10), time VARCHAR(50), name VARCHAR(100), cap smallint UNSIGNED)"
    showTable = "DESCRIBE parking"
    deleteQuery = "DELETE FROM parking"
    val = [
        (date, day, time, info1[2].replace('star_border','').replace(' ',''), 100-int(info1[1].replace('%',''))),
        (date, day, time, info2[2].replace('star_border','').replace(' ',''), 100-int(info2[1].replace('%',''))),
        (date, day, time, info3[2].replace('star_border','').replace(' ',''), 100-int(info3[1].replace('%',''))),
        (date, day, time, info4[2].replace('star_border','').replace(' ',''), 100-int(info4[1].replace('%',''))),
        (date, day, time, info5[2].replace('star_border','').replace(' ',''), 100-int(info5[1].replace('%',''))),
        (date, day, time, info6[2].replace('star_border','').replace(' ',''), 100-int(info6[1].replace('%',''))),
        (date, day, time, info7[2].replace('star_border','').replace(' ',''), 100-int(info7[1].replace('%',''))),
        (date, day, time, info8[2].replace('star_border','').replace(' ',''), 100-int(info8[1].replace('%',''))),
        (date, day, time, info9[2].replace('star_border','').replace(' ',''), 100-int(info9[1].replace('%',''))),
        (date, day, time, info10[2].replace('star_border','').replace(' ',''), 100-int(info10[1].replace('%','')))
    ]

    #cursor.execute(createTable)
    
    cursor.executemany(sql,val)
    db.commit()
    #print(cursor.rowcount, "record(s) inserted.")
    #db.close()

    #cursor.execute(query)
    #result = cursor.fetchall()
    #for i in result:
    #    print(i)

def parkingdeck(allInfoList):
    print("Parking deck options")
    print("1. Cone Deck Faculty/Staff\n2. Cone Deck Visitor\n3. CRI Deck\n4. East Deck 1\n5. East Deck 2/3\n6. North Deck\n7. South Village Deck\n8. Union Deck Lower\n9. Union Deck Upper\n10. West Deck")

    deck = int(input("What parking deck? "))
    while deck not in [1,2,3,4,5,6,7,8,9,10]:
        print("Not a valid number, please try again")
        deck = int(input("What parking deck? "))
    if deck == 1:
        info1 = allInfoList[0].split("\n")
        print(info1[2].replace('star_border',''),":",info[1])
    elif deck == 2:
        info2 = allInfoList[1].split("\n")
        print(info2[2].replace('star_border',''),":",info[1])
    elif deck == 3:        
        info3 = allInfoList[2].split("\n")
        print(info3[2].replace('star_border',''),":",info[1])
    elif deck == 4:
        info4 = allInfoList[3].split("\n")
        print(info4[2].replace('star_border',''),":",info[1])
    elif deck == 5:
        info5 = allInfoList[4].split("\n")
        print(info5[2].replace('star_border',''),":",info[1])
    elif deck == 6:
        info6 = allInfoList[5].split("\n")
        print(info6[2].replace('star_border',''),":",info[1])
    elif deck == 7:
        info7 = allInfoList[6].split("\n")
        print(info7[2].replace('star_border',''),":",info[1])
    elif deck == 8:
        info8 = allInfoList[7].split("\n")
        print(info8[2].replace('star_border',''),":",info[1])
    elif deck == 9:
        info9 = allInfoList[8].split("\n")
        print(info9[2].replace('star_border',''),":",info[1])
    elif deck == 10:
        info10 = allInfoList[9].split("\n")
        print(info10[2].replace('star_border',''),":",info[1])
    else:
        info11 = allInfoList[10].split("\n")
        print(info11[2].replace('star_border',''),":",info[1])




scrape()       
database()
#parkingdeck(allInfoList)
