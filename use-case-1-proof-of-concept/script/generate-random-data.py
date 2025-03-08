import random
import datetime

# ------------ VISITORS GENERATE --------------
def generate_visitors(num_visitors):
    names = ["Alice","Charlie","Foxtrot","David","Frank","Dani","Emma","Grace",
             "Hannah","Emily","Pablo","Tracy","George","Sheldon","Brandon","Tony","Quinn"]
    tickets = ["Standard","VIP","Child","Senior"]
    visitor_data = []
    visitor_ids = []

    for i in range(num_visitors):
        name=random.choice(names)
        age = random.randint(5,65)
        ticket_type = random.choice(tickets)
        ticket_price = 50 if ticket_type == "VIP" else 20 if ticket_type == "Standard" else 10
        visit_date = datetime.date.today() - datetime.timedelta(days=random.randint(0,30))
        visitor_id = i + 1
        visitor_ids.append(visitor_id)

        visitor_data.append(f"INSERT INTO visitors (visitor_id,name,age,ticket_type,ticket_price,visit_date) "
                            f"VALUES ({visitor_id},'{name}',{age},'{ticket_type}',{ticket_price},'{visit_date}');")


    return visitor_data,visitor_ids
# ---------------- EMPLOYEE GENERATE--------------
def generate_employees(num_employees):
    names = ["John","Sarah","Jared","Emily","Jack","Lisa","Misa","Peter","Ivan","Maria",
             "Chris","Martin","Barbara","Katie","Jennifer","Eve","Vili","Brandon"]
    roles = ["Manager","Technician","Cashier","Ride Operator"]
    role_salary = {
        "Manager": random.randint(5000, 7000),
        "Technician": random.randint(3000, 5000),
        "Cashier": random.randint(2000, 3000),
        "Ride Operator": random.randint(2500, 3500)
    }
    employee_data = []
    ride_operators_ids = []
    employee_ids = []

    for i in range(num_employees):
        name = random.choice(names)
        role = random.choice(roles)
        salary = role_salary[role]
        start_hour = random.randint(6,14)
        shift_start = f"{start_hour:02}:00:00"
        shift_end = f"{(start_hour + 8) % 24:02}:00:00"
        employee_id = i + 1
        employee_ids.append(employee_id)
        if role == "Ride Operator":
            ride_operators_ids.append(i + 1)
        employee_data.append(f"INSERT INTO employees(employee_id,name,role,salary,shift_start,shift_end)"
                             f"VALUES({employee_id},'{name}','{role}',{salary},'{shift_start}','{shift_end}');")
    return employee_data,ride_operators_ids
# ----------- ATTRACTION GENERATE--------------
def generate_attractions(ride_operators_ids):
    attraction_names = ["Roller Coaster","Haunted House", "Ferris Wheel", "Bumper Cars",
                        "Funhouse","Pendelum Ride"]
    statuses = ["Open","Closed","Under Maintenance"]
    attraction_data = []
    attraction_ids = []
    for i in range (1,7):
        name = attraction_names[i-1]
        status = random.choice(statuses)
        capacity = random.randint(10,50)
        employee_id = random.choice(ride_operators_ids) if ride_operators_ids else "NULL"

        attraction_id = i
        attraction_ids.append(attraction_id)
        attraction_data.append(f"INSERT INTO attractions (attraction_id,name,status,capacity,employee_id) "
                               f"VALUES ({attraction_id},'{name}','{status}',{capacity},{employee_id});")
    return attraction_data,attraction_ids


# ---------------- VISIT GENERATE ----------------
def generate_visits(num_visitors,num_attractions,visitor_ids,attraction_ids):
    visit_data = []

    for i in range(num_visitors * 2):
        visitor_id = random.choice(visitor_ids)
        attraction_id = random.choice(attraction_ids)
        visit_date = datetime.date.today() - datetime.timedelta(days = random.randint(0,30))

        visit_data.append(f"INSERT INTO visits (visitor_id, attraction_id, visit_date)"
                          f"VALUES ({visitor_id},{attraction_id}, '{visit_date}');")
    return visit_data

# ---------------- TRANSACTION GENERATE ----------------
def generate_financial_transactions(num_visitors,business_climate,visitor_ids):
    transaction_data = []
    for visitor_id in visitor_ids:
        amount = random.uniform(20,100) if business_climate == "positive" else (
            random.uniform(5,50))
        transaction_date =  datetime.date.today() - datetime.timedelta(days = random.randint(0,30))

        transaction_data.append(f"INSERT INTO financial_transactions (visitor_id, "
                                f"transaction_type,amount,transaction_date)"
                                f"VALUES({visitor_id},'ticket purchase',{amount:.2f}, '{transaction_date}');")
    return transaction_data

#------------------ FOOD SALE GENERATION ---------------
def generate_food_sales(num_sales,business_climate,visitor_ids):
    food_items = ["Burger","Pizza","Ice Cream","Soda","Water","Duner","Grill","Juice","Hot Dog"]
    food_data = []

    for i in range(num_sales):
        visitor_id = random.choice(visitor_ids)
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
num_employees = 50
num_sales = 200 if business_climate == "positive" else 50

#-------------- generate insert statements -------------
insert_statements = []
visitor_data, visitor_ids = generate_visitors(num_visitors)
insert_statements.extend(visitor_data)

employee_data, ride_operator_ids = generate_employees(num_employees)
insert_statements.extend(employee_data)

attraction_data, attraction_ids = generate_attractions(ride_operator_ids)
insert_statements.extend(attraction_data)

insert_statements.extend(generate_visits(num_visitors, 6, visitor_ids, attraction_ids))

insert_statements.extend(generate_financial_transactions(num_visitors, business_climate, visitor_ids))
insert_statements.extend(generate_food_sales(num_sales, business_climate, visitor_ids))

# ----------- Save to File ---------------
with open ("insert_data.sql","w") as f:
    for statement in insert_statements:
        f.write(statement + "\n")

print(f"SQL Insert statements generated! See in the insert_data.sql file.")
