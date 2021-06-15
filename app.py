from flask import Flask, render_template

app = Flask(__name__)

dummy_postData = [
    {'title':'Post 1', 'content':'Lorem Ipsum Dolar Sit Amet', 'author': 'Elon Musk'}
   ,{'title':'Post 1', 'content':'Lorem Ipsum Dolar Sit Amet'}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=dummy_postData)

@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return "Hello, " + name + ", your  id is: " + str(id)

@app.route('/onlyget', methods=['GET'])
def get_req():
    return 'You can only GET this webpage.'

if __name__ == "__main__":
    app.run(debug=True)

