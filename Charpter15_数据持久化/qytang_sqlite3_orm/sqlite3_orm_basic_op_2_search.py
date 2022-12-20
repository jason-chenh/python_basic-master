from sqlalchemy.orm import sessionmaker
from sqlite3_orm_create_table import User, engine
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

Session = sessionmaker(bind=engine)
session = Session()

# 使用filter_by 过滤特定条件 [Python风格,功能有限]
users = session.query(User).filter_by(username='qinke')
for user in users:
    print(user)

# one()类似于Django的 get()
user1 = session.query(User).filter_by(username='qinke').one()
print(user1.username)

# 抑制找不到的错误
try:
    user1 = session.query(User).filter_by(username='test').one()
except NoResultFound:
    print('没有找到对象!')

# 抑制找到多个的错误
try:
    user1 = session.query(User).filter_by(password='cisco').one()
except MultipleResultsFound:
    print('找到多个对象!')


# 使用filter 过滤特定条件[SQL风格,但是需要通过 类名.属性名 的方式来过滤, 功能强大]
user1 = session.query(User).filter(User.username == 'qinke').one()
print(user1.password)

# sql的like, 可以实现正则表达式的匹配
user1 = session.query(User).filter(User.username.like('qin%')).one()
print(user1.email)

# 使用逗号分隔默认为AND条件
user1 = session.query(User).filter(User.username.like('qin%'), User.email == 'collinsctk@qytang.com').one()
print(user1)

from sqlalchemy import or_
# 使用or_来实现OR条件
user1 = session.query(User).filter(or_(User.username.like('qin%'), User.email == 'ender@qytang.com')).one()
print(user1)