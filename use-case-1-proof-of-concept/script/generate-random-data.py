import random
import datetime

# ------------ VISITORS GENERATE --------------
def generate_visitors(num_visitors):
    names = ["Alice","Charlie","Foxtrot","David","Frank","Dani","Emma","Grace",
             "Hannah","Emily","Pablo","Tracy","George","Sheldon","Brandon","Tony","Quinn"]
    tickets = ["Standard","VIP","Child","Senior"]
    visitor_data = []

    for i in range(num_visitors):
        name=random.choice(names)
        age = random.randint(5,65)
        ticket_type = random.choice(tickets)
        ticket_price = 50 if ticket_type == "VIP" else 20 if ticket_type == "Standard" else 10
        visit_date = datetime.date.today() - datetime.timedelta(days=random.randint(0,30))

        visitor_data.append(f"INSERT INTO visitors (name,age,ticket_type,ticket_price,visit_date) "
                            f"VALUES ('{name}',{age},'{ticket_type}',{ticket_price},'{visit_date}');")

    return visitor_data
# ----------- ATTRACTION GENERATE--------------
def generate_attractions():
    attraction_names = ["Roller Coaster","Haunted House", "Ferris Wheel", "Bumper Cars",
                        "Funhouse","Pendelum Ride"]
    status = ["Open","Closed","Under Maintenance"]
    attraction_data = []

    for i in range (1,6):
        name = attraction_names[i-1]
        status = random.choice(status)
        capacity = random.randint(10,50)

        attraction_data.append(f"INSERT INTO attractions (name,status,capacity) "
                               f"VALUES ('{name}','{status}',{capacity});")
    return attraction_data

# ---------------- VISIT GENERATE ----------------
def generate_visits(num_visitors,num_attractions):
    visit_data = []

    for i in range(num_visitors * 2):
        visitor_id = random.randint(1,num_visitors)
        attraction_id = random.randint(1,num_attractions)
        visit_date = datetime.date.today() - datetime.timedelta(days = random.randint(0,30))

        visit_data.append(f"INSERT INTO visits (visitor_id, attraction_id, visit_date)"
                          f"VALUES ({visitor_id},{attraction_id}, '{visit_date}');")
    return visit_data

# ---------------- TRANSACTION GENERATE ----------------
def generate_financial_transactions(num_visitors,business_climate):
    transaction_data = []
    for visitor_id in range (1,num_visitors + 1):
        amount = random.uniform(20,100) if business_climate == "positive" else (
            random.uniform(5,50))
        transaction_date =  datetime.date.today() - datetime.timedelta(days = random.randint(0,30))

        transaction_data.append(f"INSERT INTO financial_transactions (visitor_id, "
                                f"transaction_type,amount,transaction_date)"
                                f"VALUES({visitor_id},'ticket purchase',{amount:.2f}, '{transaction_date}');")
    return transaction_data

#------------------ FOOD SALE GENERATION ---------------
def generate_food_sales(num_sales,business_climate):
    food_items = ["Burger","Pizza","Ice Cream","Soda","Water","Duner","Grill","Juice","Hot Dog"]
    food_data = []

    for i in range(num_sales):
        visitor_id = random.randint(1,100)
        food_item = random.choice(food_items)
        quantity = random.randint(1,4)
        price = random.uniform(5,15) if business_climate == "positive" \
            else random.uniform(3,10)
        sale_date = datetime.date.today() - datetime.timedelta(days = random.randint(0,30))

        food_data.append(f"INSERT INTO food_sales (visitor_id, food_item, quantity, price, sale_date)"
                         f"VALUES ({visitor_id}, '{food_item}',{quantity},{price:.2f},'{sale_date}');")
    return food_data

#--------------- user input -------------
business_climate = input("Enter business climate (Positive or Negative): ").strip().lower()
num_visitors = 100 if business_climate == "positive" else 30
num_sales = 200 if business_climate == "positive" else 50

#-------------- generate insert statements -------------
insert_statements = []
insert_statements.extend(generate_visitors(num_visitors))
insert_statements.extend(generate_attractions())
insert_statements.extend(generate_visits(num_visitors,6))
insert_statements.extend(generate_financial_transactions(num_visitors,business_climate))
insert_statements.extend(generate_food_sales(num_sales,business_climate))

# ----------- Save to File ---------------
with open ("insert_data.sql","w") as f:
    for statement in insert_statements:
        f.write(statement + "\n")

print(f"SQL Insert statements generated! See in the insert_data.sql file.")
