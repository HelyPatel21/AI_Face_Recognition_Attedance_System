import firebase_admin
from firebase_admin import credentials
from firebase_admin import db


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{"databaseURL":"your databaseURL"})

ref = db.reference('Students')

data = {
    "102863":
        {
            'Name':"Ratan TATA",
            'Field':'architecture and engineering ',
            'standing':'A',
            'Starting_year':'2016',
            'Attendances':8,
            'Year': 4,
            'last_attendance_time': '2019-09-25 00:54:35'
        },
    "123456":
        {
            'Name':"Kriti Senon",
            'Field':'IT',
            'standing':'B',
            'Starting_year':'2015',
            'Attendances':8,
            'Year': 4,
            'last_attendance_time': '2018-07-25 00:35:30'
        },
    "237916":
        {
            'Name':"Mark Zuckerberg",
            'Field':'computer science',
            'standing':'B',
            'Starting_year':'2013',
            'Attendances':9,
            'Year': 4,
            'last_attendance_time': '2016-06-20 08:12:35'
        },
    "567890":
        {
            'Name':"Sundar  Pichai",
            'Field':'metallurgy engineering',
            'standing':'A',
            'Starting_year':'2010',
            'Attendances':9,
            'Year': 4,
            'last_attendance_time': '2014-05-25 09:54:35'
        },
    "761351":
        {
            'Name':"Mukesh  Ambani",
            'Field':'Chemical Engineering',
            'standing':'A',
            'Starting_year':'2015',
            'Attendances':8,
            'Year': 4,
            'last_attendance_time': '2018-09-21 10:30:35'
        },
    "852741":
        {
            'Name':"Emly Blunt",
            'Field':'drama studies',
            'standing':'C',
            'Starting_year':'2016',
            'Attendances':8,
            'Year': 3,
            'last_attendance_time': '2019-03-25 08:50:35'
        },
    "963852":
        {
            'Name':"Elon  Musk",
            'Field':' physics and economics',
            'standing':'B',
            'Starting_year':'2011',
            'Attendances':6,
            'Year': 4,
            'last_attendance_time': '2014-09-09 09:54:35'
        }
}


for key,value in data.items():
    ref.child(key).set(value)