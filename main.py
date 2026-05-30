
# მონ. ბაზის იმიტაციაა, ეს მექნება იქამდე სანამ ნამდვილ მონაცეთა ბაზას არ შევქმნი

bank_db = {
    # ანგარიში 1
    "GE01001": {
        "name": "Gio",
        "balance": 2500.0,
        "history": [1200, -200]
    },

    # ანგარიში 2
    "GE01002": {
        "name": "Anna",
        "balance": 5000.0,
        "history": [5000]
    }
}

def checkUser():
    angarishis_nomeri = input("შეიყვანე ანგარიშის ნომერი: ").strip().upper()


    
    if angarishis_nomeri in bank_db:
        momxm_saxeli =  bank_db[angarishis_nomeri]["name"]
        momxm_angarishi = bank_db[angarishis_nomeri]["balance"]
        print(f"{momxm_saxeli} - {momxm_angarishi}")     
    else:
        print("ანგარიში ვერ მოიძებნა!")    

  

checkUser()


# ოპერაცების შემსრულებელი

def updateBalance(account_number):
    operation = input("აირჩიეთ ოპერაცია (1 - შეტანა, 2 - გატანა): ").strip()
    

    if operation == "1":
        tanxa = float(input("რა თანხის შეტანა გსურთ? ")) 
        
        bank_db[account_number]["balance"] += tanxa  
        bank_db[account_number]["history"].append(tanxa) 
        print(f"თანხა შეტანილია! ახალი ბალანსი: {bank_db[account_number]['balance']} ლარი.")
        
   
    elif operation == "2":
        tanxa = float(input("რა თანხის გატანა გსურთ? "))
        
      
        if tanxa <= bank_db[account_number]["balance"]:
            bank_db[account_number]["balance"] -= tanxa  
            bank_db[account_number]["history"].append(-tanxa) 
            print(f"თანხა გატანილია! ახალი ბალანსი: {bank_db[account_number]['balance']} ლარი.")
        else:
            print("ტრანზაქცია უარყოფილია: არასაკმარისი ბალანსი!")
    else:
        print("არასწორი ოპერაცია!")


updateBalance("GE01001")
        
        