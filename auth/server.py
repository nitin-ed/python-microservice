import jwt, datetime, os
from flask import Flask, request
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
@server.route("/login", methods=["POST"])
def login():
     # Get the Authorization header from the request
    auth = request.authorization
    if not auth:
        return "Missing Credentials", 401

    # Check db for username and password
    cur = mysql.connection.cursor()
    res = cur.execute(
        "SELECT email, password FROM user WHERE email=%s", (auth.username,)
    )

    # User Found
    if res > 0:
        user_row = cur.fetchone()
        email = user_row[0]
        password = user_row[1]

        # Check Creds with db

        if auth.username != email and auth.password != password:
            return "Invalid Credentials", 401
        else:
            return createJWT(auth.username, os.environ.get("JWT_SECRET"), True)
        
    else:
        return "Invalid Credentials", 401

# Route for JWT validation
@server.route("./validate", method=["POST"])
def validate():
    encoded_jwt = request.headers["Authorization"]

    if not encoded_jwt:
        return "Missing Credentials", 401

    encoded_jwt = encoded_jwt.split(" ")[1]

    try:
        decoded = jwt.decode(
            encoded_jwt,
            os.environ.get("JWT_SECRET"),
            algorithm=["HS256"]
        )
    except:
        return "Not Authorized", 403

    return decoded, 200

# Function to create a JWT token
def createJWT(username, secret, authz):
    return jwt.encode(
        {
            "username":username,
            "exp": datetime.datetime.now(datetime.timezone.utc)
            + datetime.timedelta(days=1),
            "iat": datetime.datetime.now(datetime.timezone.utc),
            "admin": authz
        },
        secret,
        algorithm="HS256",
    )

# Entry Point
if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000)
