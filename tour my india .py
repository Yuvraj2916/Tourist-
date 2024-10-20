import csv
import time
import emoji

a='''\U0001F64F  Namaste  \U0001F64F'''
b='''WE WILL ASSIST YOU FOR YOUR TRIP \U0001F60A'''
print(' ')
print(a.center(110))
print(b.center(110))

#The CSV file where travel records will be stored
CSV_FILE = "travel_recs.csv"
#The CSV file where invoice will be generated
CSV_F="travel_inv.csv"

'''def create_csv_f():
    with open(CSV_F, "w", newline="") as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow(["Name", "Age", "Hotel Amount","Transport Amount","Total Amount"])
        writer.writerows(data2)'''
    
def add_travel_record1(name, age, destination, departure_date, return_date):
    with open(CSV_FILE, "a", newline="") as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerow([name, age, destination, departure_date, return_date])
        
def add_travel_record2(name, age, hotel_amount, transport_amount, total_amount):
    with open(CSV_F, "a", newline="") as f:
        writer = csv.writer(f,delimiter=',')
        writer.writerow([name, age, hotel_amount, transport_amount, total_amount])




#BOOKING FUNC
def dest():
    print('\t \t PLEASE SELECT DESTINATION')
    print()
    print("\t \t 1. SHIMLA\n")
    print("\t \t 2. MANALI\n")
    print('\t \t 3. OOTY\n')
    print('\t \t 4. DARJEELING\n')
    print("\t \t 5. JAIPUR\n")
    ch_dest=int(input("--->>"))
    if ch_dest==1:
        destination="Shimla"
    elif ch_dest==2:
        destination="Manali"     
    elif ch_dest==3:
        destination="Ooty"      
    elif ch_dest==4:
        destination="Darjeeling"  
    elif ch_dest==5:
        destination="Jaipur"
        

    
def package():
    print("_"*107)
    print('\t \t PLEASE SELECT DESIRED PACKAGE')
    print("_"*107)
    print()
    print("\t \t Please note the following packages\n"
          "\t \t are in accordance to per person per night")
    print()
    print('\t \t 1. Rs3,500 per person, 3 activites,CP')
    print("\t \t  It includes breakfast along with room")
    print()
    print("\t \t 2. Rs5,000 per person, 3 activities, MAP")
    print("\t \t  Room with Breakfast and One Major Meal")
    print()
    print("\t \t 3. Rs6,000 per person, 5 activites, MAP")
    print("\t \t  Room with Breakfast and One Major Meal")
    print()
    print('\t \t 4. Rs7,000 per person, 8 activities, EP')
    print ("\t \t It is room only,with no meals")
    print()
    ch_pack=int(input("enter the code no--->>"))
    global pack_cost
    if ch_pack==1:
        pack_cost= 3500
    elif ch_pack==2:
        pack_cost= 5000
    elif ch_pack==3:
        pack_cost=6000
    elif ch_pack==4:
        pack_cost=7000
    global nights
    nights=int(input('ENTER NO. OF NIGHTS YOU WANT TO STAY:'))

def passengers():
    data1=[]
    global num
    global age
    num=int(input("ENTER NO. OF PASSENGERS:"))
    destination=input("Enter your destination:")
    i=1
    departure_date = input("ENTER DEPARTURE DATE(DD-MM-YYYY):")
    return_date = input("ENTER RETURN DATE(DD-MM-YYYY):")
    while i<=num:
        name=input("ENTER NAME OF PASSENGER:")
        age=int(input("ENTER AGE OF PASSENGER:"))
        gender=input('ENTER GENDER OF PASSENGER:')
        add_travel_record1=[name, age, destination, departure_date, return_date]
        data1.append(add_travel_record1)
        i+=1
    with open(CSV_FILE, "w", newline="") as file:
        writer = csv.writer(file,delimiter=',')
        writer.writerow(["Name", "Age", "Destination", "Departure Date", "Return Date"])
        writer.writerows(data1)
        
def route():
    print("\t START JOURNEY FROM:")
    print("\t 1. DELHI")
    print("\t 2. BENGALURU")
    print("\t 3. MUMBAI")
    print("\t 4. HYDERABAD")
    print("\t 5. CHENNAI")
    ch_route=int(input("enter the code no--->>"))
    global route_cost
    if ch_route==1:
        route_cost=4500
    elif ch_route==2:
        route_cost=9500
    elif ch_route==3: 
        route_cost=9000
    elif ch_route==4:
        route_cost=5000
    elif ch_route==5:
        route_cost=7000
    time.sleep(2)
    print("done!")
    time.sleep(1)
    
def invoice():
    print('''\t     PAYMENT       ")
    -----------------------
         MODE OF PAYMENT   
      1- Credit/Debit Card
      2- Paytm/PhonePe
      3- Using UPI
      4- Cash''')
    pay=int(input("Enter the code no.--->>"))
    print("PROCEED(Y/N)")
    data2=[]
    dec=input("--->>")
    if dec in "Yy":
        name=input("ENTER NAME OF PAYEE:")
        nom=int(input("ENTER PHONE NO.:"))
        hotelamount=pack_cost*nights
        totalamount=pack_cost*nights+routecost
        routecost=route_cost
        print("-----------------------")
        print("     TOUR MY INDIA       ")
        print('-----------------------')
        print("          BILL         ")
        print('NAME:',name, "\t\n Phone number:",nom)
        print("HOTEL AMOUNT= Rs",hotelamount)
        print("TRANSPORT AMOUNT= Rs",routecost)
        print("TOTAL AMOUNT= Rs",totalamount)
        print("-----------------------")
        print("-----------------------")
        print("      THANK YOU \U0001F604      ")
        print("------------------------")
        print("BOOKING DONE SUCCESSFULLY")
        print("HAPPY JOURNEY!")
        row=[name,age,hotelamount,routecost,totalamount]
        data2.append(row)
        with open(CSV_F, "w", newline="") as f:
            writer = csv.writer(f,delimiter=',')
            writer.writerow(["Name", "Age", "Hotel Amount","Transport Amount","Total Amount"])
            writer.writerows(data2)
        
        

def view_travel_records():
    # Display all travel records from the CSV file
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("Name: ", row[0])
            print("Age:",row[1])
            print("Destination: ", row[2])
            print("Departure Date: ", row[3])
            print("Return Date: ", row[4])
            print("--------------------------")

def search_travel_records(name):
    # Search for travel records by traveler's name
    found = False
    with open(CSV_FILE, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0].lower() == name.lower():
                print("Name: ", row[0])
                print("Age:",row[1])
                print("Destination: ", row[2])
                print("Departure Date: ", row[3])
                print("Return Date: ", row[4])
                found = True

    if not found:
        print("No records found for", name)




#MAIN MENU
        
import time
print("_"*107)
a=" \U0001F31F TOUR MY INDIA \U0001F31F"
b=a.center(107)
print(b)
print("_"*107)
print()
time.sleep(2)
print("_"*107)
c="Welcome to TOUR MY INDIA!"
d=c.center(107)
print(d)
print()
time.sleep(1)
e="Where the journey begins"
f=e.center(107)
print(f)
print("_"*107)
print()
time.sleep(2)
dest()
package()
passengers()

'''create_csv_f()'''

print("Please Wait.....")
time.sleep(2)
print("_"*107)
hb= "HOTEL BOOKED"
hc=hb.center(107)
print(hc)
print("_"*107)
print()
    
while True:
    print("1. BOOK FLIGHT TICKECTS\n")
    time.sleep(1)
    print("2. BOOK TRAIN TICKETS\n")
    time.sleep(1)
    print("3. INVOICE\n")
    time.sleep(1)
    print("4. View All Travel Records\n")
    time.sleep(1)
    print("5. Search for Travel Records\n")
    time.sleep(1)
    print("6. EXIT\n")
    ch=int(input("ENTER CHOICE NO.-->"))
    if ch==1:
        route()
    elif ch==2:
        route()
    elif ch==3:
        invoice()
    elif ch==4:
        view_travel_records()
    elif ch==5:
        name = input("Enter traveler's name to search: ")
        search_travel_records(name)
    elif ch==6:
        break
    else:
        print('PLEASE ENTER VALID OPTION')



              

    
