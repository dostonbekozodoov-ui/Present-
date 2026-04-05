from flask import Flask, render_template
app = Flask(__name__)

@app.route('/admin')
def admin_dashboard():
    # Sample data for user management (this should connect to a database)
    users = [
        {"id": 1, "name": "User One", "email": "user1@example.com"},
        {"id": 2, "name": "User Two", "email": "user2@example.com"},
        # More user data here
    ]
    
    return render_template('admin_dashboard.html', users=users)

if __name__ == '__main__':
    app.run(debug=True)