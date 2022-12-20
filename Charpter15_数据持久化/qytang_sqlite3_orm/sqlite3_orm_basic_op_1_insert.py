from sqlalchemy.orm import sessionmaker
from sqlite3_orm_create_table import User, engine


Session = sessionmaker(bind=engine)
session = Session()

# 插入一个条目
user1 = User(username='qinke',
             password='cisco',
             email='collinsctk@qytang.com')
session.add(user1)
session.commit()

user2 = User(username='tina',
             password='cisco',
             realname='qyttina',
             email='tina@qytang.com')
session.add(user2)
session.commit()

# 一次性插入多个条目
# session.add_all([user1, user2])
# session.commit()
