from flask import Flask, render_template
app = Flask(__name__)

JOBS = [
  {
    'id': 1 ,
    'title' : 'Data Analyst',
    'location' : 'Islamabad, Pakistan' ,
    'salary' : 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title' : 'Software Engineer',
    'location' : 'Islamabad, Pakistan' ,
    'salary' : 'Rs. 15,00,000'
  },
{
    'id': 3,
    'title' : 'Backend Engineer',
    'location' : 'Islamabad, Pakistan' ,
    'salary' : 'Rs. 9,00,000'
  },
{
    'id': 4,
    'title' : 'Frontend Engineer',
    'location' : 'Islamabad, Pakistan' ,
    'salary' : 'Rs. 8,00,000'
  }
]
@app.route("/")
def hello_world():
  return render_template("home.html" ,
                         jobs=JOBS , project_name='The Khd Project' )

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)



