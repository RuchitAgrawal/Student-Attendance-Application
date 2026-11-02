from flask import Flask, request, render_template_string

app = Flask(__name__)

LOGIN_PAGE = """
<!DOCTYPE html>
<html>
<head><title>Student Login</title></head>
<body>
  <h2>Student Attendance Login</h2>
  <form method="POST" action="/login">
    <label>Username:</label><br>
    <input type="text" id="username" name="username" placeholder="Enter username"><br><br>
    <label>Password:</label><br>
    <input type="password" id="password" name="password" placeholder="Enter password"><br><br>
    <button type="submit" id="login-btn">Login</button>
  </form>
  {% if error %}
  <p id="error-msg" style="color:red;">{{ error }}</p>
  {% endif %}
  {% if success %}
  <p id="success-msg" style="color:green;">{{ success }}</p>
  {% endif %}
</body>
</html>
"""

VALID_USERS = {"student1": "pass123", "admin": "admin123"}


@app.route("/", methods=["GET"])
def index():
    return render_template_string(LOGIN_PAGE)


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("username", "")
    password = request.form.get("password", "")
    if VALID_USERS.get(username) == password:
        return render_template_string(LOGIN_PAGE, success="Login successful! Welcome, " + username)
    return render_template_string(LOGIN_PAGE, error="Invalid credentials. Please try again.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
