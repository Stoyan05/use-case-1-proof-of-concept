from flask import Flask, jsonify, request
import snowflake.connector
import db

app = Flask(__name__)


@app.route("/attractions", methods=['GET'])
def get_all_attractions():
    return db.db_query("SELECT * FROM attractions")

@app.route("/attractions/<int:attraction_id>",methods=['GET'])
def get_attraction_by_id(attraction_id):
    query = "SELECT * FROM attractions WHERE attraction_id = %s"
    result = db.db_query(query,(attraction_id,))

    if not result:
        return jsonify({"error": "Attraction not found"}), 404

    return jsonify(result[0])


@app.route("/employees",methods=['GET'])
def get_all_employees():
    results = db.db_query("SELECT * FROM employees")

    employees = []
    for row in results:
        employee= {
            "employee_id": row[0],
            "name" : row[1],
            "role": row[2],
            "salary": row[3],
            "shift_start": str(row[4]),
            "shift_end": str(row[5])
        }
        employees.append(employee)

    return jsonify(employees)

@app.route("/employees/<int:employee_id>",methods=['GET'])
def get_employee_by_id(employee_id):
    query = "SELECT * FROM employees WHERE employee_id = %s"
    result = db.db_query(query,(employee_id,))


    employee = {
        "employee_id": result[0][0],
        "name":result[0][1],
        "role": result[0][2],
        "salary": result[0][3],
        "shift_start": str(result[0][4]),
        "shift_end": str(result[0][5])
    }

    if not result:
        return jsonify({"error": "Employee not found"}), 404

    return jsonify(employee)

@app.route("/sales", methods=['GET'])
def get_all_sales():
    return db.db_query("SELECT * FROM sales")


@app.route("/sales/<int:sale_id>",methods=['GET'])
def get_sale_by_id(sale_id):
    query = "SELECT * FROM sales WHERE sale_id = %s"
    result = db.db_query(query,(sale_id,))

    if not result:
        return jsonify({"error": "Sale not found"}), 404

    return jsonify(result[0])


@app.route("/tickets", methods=['GET'])
def get_all_tickets():
    return db.db_query("SELECT * FROM tickets")

@app.route("/tickets/<int:ticket_id>",methods=['GET'])
def get_ticket_by_id(ticket_id):
    query = "SELECT * FROM tickets WHERE ticket_id = %s"
    result = db.db_query(query,(ticket_id,))

    if not result:
        return jsonify({"error": "Ticket not found"}), 404

    return jsonify(result[0])

@app.route("/tickets", methods=['POST'])
def create_ticket():
    request_data = request.get_json()
    highest_id_query = db.db_get_highest_id("SELECT MAX(ticket_id) FROM tickets")
    ticket_type = request_data["ticket_type"]
    ticket_price = request_data["ticket_price"]

    db.db_insert(f"INSERT INTO tickets(ticket_id,ticket_type,ticket_price) VALUES({highest_id_query[0][0] + 1},'{ticket_type}', {ticket_price})")
    return {"result" : "successfully created new task"}


@app.route("/events",methods=['GET'])
def get_all_events():
    result = db.db_query("SELECT * FROM events")

    events = []

    for row in result:
        event = {
            "event_id": row[0],
            "name" : row[1],
            "description": row[2],
            "date" : row[3],
            "start_time": str(row[4]),
            "end_time": str(row[5]),
            "location": row[6],
            "ticket_price": row[7],
            "capacity": row[8],
            "status": row[9]
        }
        events.append(event)

    return jsonify(events)

@app.route("/events/<int:event_id>",methods=['GET'])
def get_event_by_id(event_id):
    query = "SELECT * FROM events WHERE event_id = %s"
    result = db.db_query(query,(event_id,))

    if not result:
        return jsonify({"error": "Event not found"}), 404

    event = {
        "event_id": result[0][0],
        "name": result[0][1],
        "description": result[0][2],
        "date": result[0][3],
        "start_time": str(result[0][4]),
        "end_time": str(result[0][5]),
        "location": result[0][6],
        "ticket_price": result[0][7],
        "capacity": result[0][8],
        "status": result[0][9]
    }
    return jsonify(event)


@app.route("/visitors", methods=['GET'])
def get_all_visitors():
    result = db.db_query("SELECT * FROM visitors")

    visitors = []
    for row in result:
        visitor = {
            "visitor_id" : row[0],
            "name" : row[1],
            "age" : row[2],
            "ticket_type": row[3],
            "ticket_price": row[4],
            "visit_date" : row[5],
            "ticket_id" : row[6],
        }
        visitors.append(visitor)

    return jsonify(visitors)


@app.route("/visitors/<int:visitor_id>",methods=['GET'])
def get_visitor_by_id(visitor_id):
    query = "SELECT * FROM visitors WHERE visitor_id = %s"
    result = db.db_query(query,(visitor_id,))
    if not result:
        return jsonify({"error": "Visitor not found"}), 404

    visitor = {
        "visitor_id": result[0][0],
        "name": result[0][1],
        "age": result[0][2],
        "ticket_type": result[0][3],
        "ticket_price": result[0][4],
        "visit_date": result[0][5],
        "ticket_id": result[0][6],
    }
    

    return jsonify(visitor)


@app.route("/financial", methods=['GET'])
def get_all_financial():
    result = db.db_query("SELECT * FROM financial_transactions")

    transactions = []
    for row in result:
        transaction = {
            "transaction_id": row[0],
            "visitor_id": row[1],
            "transaction_type" : row[2],
            "amount": row[3],
            "transaction_date": row[4],
        }
        transactions.append(transaction)

    return jsonify(transactions)

@app.route("/financial/<int:transaction_id>",methods=['GET'])
def get_financial_by_id(transaction_id):
    query = "SELECT * FROM financial_transactions WHERE transaction_id = %s"
    result = db.db_query(query,(transaction_id,))

    if not result:
        return jsonify({"error": "Financial not found"}), 404
    transaction = {
        "transaction_id": result[0][0],
        "visitor_id": result[0][1],
        "transaction_type": result[0][2],
        "amount": result[0][3],
        "transaction_date": result[0][4]
    }
    return jsonify(transaction)

if __name__ == "__main__":
    app.run()
