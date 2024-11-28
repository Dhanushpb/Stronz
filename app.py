from flask import Flask,render_template

cen=Flask(__name__)

JOBS = [
    {
        'id':1,
        'title':'Data Analsyt',
        'location':'Bengaluru',
        'Salary':'Rs.15,00,000'
    },
    {
        'id':2,
        'title':'Data Scientist',
        'location':'Hyderabad',
        'Salary':'Rs.24,00,000'
    },
    {
        'id':3,
        'title':'Frontend Engineer',
        'location':'California ',
        'Salary':'$120,000 '
    },
    {
        'id':4,
        'title':'Web Developer',
        'location':'Remote',
        'Salary':'Rs.15,00,000'
    }
]

@cen.route("/")
def homepage():
    return render_template('home.html',jobs=JOBS,company_name='Stronz Ltd')