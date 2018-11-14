import os
from app import app

os.system("rm -f mirai.db; sqlite3 mirai.db < create.sql")
app.run(host="0.0.0.0")
