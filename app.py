from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Change this to a secure key

# Simple in-memory storage for enrolled courses (replace with database later)
enrolled_courses = []

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Simple authentication (replace with real auth)
        if username == 'admin' and password == 'password':
            flash('Login successful!', 'success')
            return redirect(url_for('training'))
        else:
            flash('Invalid credentials', 'error')
    return render_template('login.html')

@app.route('/training', methods=['GET', 'POST'])
def training():
    courses = [
        {'name': 'Gen AI', 'desc': 'Master Generative AI techniques.'},
        {'name': 'Snowflake with Cortex', 'desc': 'Learn Snowflake data warehousing.'},
        {'name': 'Python', 'desc': 'Comprehensive Python programming.'},
        {'name': 'PySpark', 'desc': 'Big data processing with PySpark.'},
        {'name': 'Databricks', 'desc': 'Cloud-based analytics platform.'},
        {'name': 'ML', 'desc': 'Machine Learning fundamentals.'},
        {'name': 'DL', 'desc': 'Deep Learning with neural networks.'},
        {'name': 'AWS DevOps', 'desc': 'DevOps on AWS.'},
        {'name': 'Agentic AI', 'desc': 'Building AI agents.'},
        {'name': 'Chat Bots', 'desc': 'Creating conversational bots.'},
        {'name': 'Chat Assistants', 'desc': 'Advanced chat assistants.'},
        {'name': 'Prompt Engineering', 'desc': 'Crafting effective prompts.'},
        {'name': 'Data Warehouse', 'desc': 'Data warehousing concepts.'}
    ]
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        enrolled_courses.append({'name': name, 'email': email, 'phone': phone, 'course': course})
        flash(f'Enrolled in {course} successfully!', 'success')
        return redirect(url_for('training'))
    return render_template('training.html', courses=courses)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)