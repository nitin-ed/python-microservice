import jwt, datetime, os
from flask import Flask, request, jsonify
from flask_mysqldb import MySQL

# Initialize Flask App
server = Flask(__name__)

# Initialize MySQL Connection
mysql = MySQL(server)

# Database Config from Env
server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_USER")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_PASSWORD")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_DB")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_PORT")


# Route for Login
@server.route("/users", methods=["POST"])
def get_all_users():
    try:
        cur = mysql.connection.cursor()

        cur.execute("SELECT * FROM Users")

        results = cur.fetchall()

        users = [{"id": row[0], "email": row[1]} for row in results]

        cur.close()

        return jsonify(users), 200
    
    except Exception as e:
        return str(e), 500
        
    

# Route for JWT validation
@server.route("/validate", methods=["POST"])





# Entry Point
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
