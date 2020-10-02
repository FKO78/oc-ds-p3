import os 

# To generate a new secret key:
# >>> import random, string
# >>> "".join([random.choice(string.printable) for _ in range(24)])
SECRET_KEY = "1bdbeeb07ac5163c68bd205eb0d11dec"

FB_APP_ID = 2640045952990513

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db') 

SOURCE_FILE = 'OC_DS_P3.pkl' 
#SOURCE_FILE_2 = 'OC_DS_P3_2.pkl' 
NB_RECOS = 5