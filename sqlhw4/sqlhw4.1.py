import sql_func
from sql_func import connect_db, read_query
# 4
db_name:str= "sqlhw4.db"
conn,cursor=sql_func.connect_db(db_name)
all_courses=sql_func.read_query(cursor,"SELECT * FROM courses")
for item in all_courses:
    print(item)

# 5
course_topic:str=input("enter a course topic:")
course_hours:int=int(input("enter course length:"))
sql_func.update_query(cursor,conn,"INSERT INTO courses (topic, hours) VALUES (?, ?)",(course_topic,course_hours))
