from flask import Flask, render_template
app = Flask(__name__)

JOBS = [{'id':1,
         'job':'Backend Engineer',
         'location': 'Lagos, Nigeria',
         'salary':'$100,000'
        },
        {
          'id':2,
         'job':'Frontend Engineer',
         'location': 'Delhi, India',
         'salary':'$70,000'
        },
        {
          'id':3,
           'job':'DevOps',
           'location': 'California, USA',
           'salary':'$120,000'
        },
        {
          'id':4,
           'job':'ML Engineer',
           'location': 'Abuja, Nigeria',
           'salary':'$150,000'
        },
        {
          'id':5,
           'job':'Software Developer',
           'location': 'Cross River, Nigeria',
           'salary':'$170,000'
        }

  ]

@app.route('/')
def hello_world():
  return render_template('home.html', jobs=JOBS)
if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  