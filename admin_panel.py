import os

app.run(
    host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
        )
        
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