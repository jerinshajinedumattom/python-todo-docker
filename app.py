from flask import Flask, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def home():
    return '''
    <h2>Todo App</h2>
    <form method="POST" action="/add">
        <input name="task">
        <button>Add</button>
    </form>
    <ul>
        {}
    </ul>
    '''.format(''.join(f"<li>{t}</li>" for t in tasks))

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)