from sqlalchemy.orm import sessionmaker
from sqlite3_orm_create_table import Router, CPUUsage, Interface, engine

Session = sessionmaker(bind=engine)
session = Session()

# 删除所有cpu_usage记录
# session.query(CPUUsage).delete()

# 删除所有router
session.query(Router).delete()

session.commit()
