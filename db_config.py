from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'wp_user'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'wordplay'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.3'
mysql.init_app(app)
