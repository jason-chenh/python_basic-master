# https://www.cnblogs.com/lsdb/p/9835894.html

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Text, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
import datetime

tzutc_8 = datetime.timezone(datetime.timedelta(hours=8))  # 设置时区为东八区

# echo=Ture----echo默认为False，表示不打印执行的SQL语句等较详细的执行信息，改为Ture表示让其打印。

# check_same_thread=False----sqlite默认建立的对象只能让建立该对象的线程使用，
# 而sqlalchemy是多线程的所以我们需要指定check_same_thread=False来让建立的对象任意线程都可使用。

# 否则不时就会报错：sqlalchemy.exc.ProgrammingError: (sqlite3.ProgrammingError) SQLite objects created in a thread can
# only be used in that same thread. The object was created in thread id 35608 and this is thread id 34024.
# [SQL: 'SELECT users.id AS users_id, users.name AS users_name, users.fullname AS users_fullname,
# users.password AS users_password \nFROM users \nWHERE users.name = ?\n LIMIT ? OFFSET ?']
# [parameters: [{}]] (Background on this error at: http://sqlalche.me/e/f405)

engine = create_engine('sqlite:///sqlalchemy_sqlite3.db?check_same_thread=False',
                       echo=False
                       )

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    realname = Column(String(64), nullable=True)
    # realname = Column(String(64), nullable=False, server_default='乾颐堂')
    email = Column(String(64), nullable=False, index=True)

    def __repr__(self):
        return f"{self.__class__.__name__}(username: {self.username} | email: {self.email})"


class Router(Base):
    __tablename__ = 'router'

    id = Column(Integer, primary_key=True)
    routername = Column(String(64), nullable=False, index=True)
    ip = Column(String(64), nullable=False, index=True)
    interface = relationship('Interface')
    ospf_process = relationship('OSPFProcess', uselist=False)  # uselist=False表示onetoone
    cpu_usage = relationship('CPUUsage')

    def __repr__(self):
        return f"{self.__class__.__name__}({self.routername})"


class Interface(Base):
    __tablename__ = 'interface'

    id = Column(Integer, primary_key=True)
    router_id = Column(Integer, ForeignKey("router.id", ondelete='CASCADE'), nullable=False)
    interface_name = Column(String(64), nullable=False)
    ip = Column(String(64), nullable=False)
    mask = Column(String(64), nullable=False)
    router = relationship('Router')

    def __repr__(self):
        return f"{self.__class__.__name__}(Router: {self.router.routername} "\
               f"| Interface_name: {self.interface_name} " \
               f"| IP: {self.ip} / {self.mask})"


class OSPFProcess(Base):
    __tablename__ = 'ospf_process'

    id = Column(Integer, primary_key=True)
    router_id = Column(Integer, ForeignKey("router.id", ondelete='CASCADE'), nullable=False)
    processid = Column(Integer, nullable=False)
    routerid = Column(String(64), nullable=False)
    router = relationship('Router')
    area = relationship('Area')

    def __repr__(self):
        return f"{self.__class__.__name__}(Router: {self.router.routername} " \
               f"| Process: {self.processid})"


class Area(Base):
    __tablename__ = 'area'

    id = Column(Integer, primary_key=True)
    ospfprocess_id = Column(Integer, ForeignKey("ospf_process.id", ondelete='CASCADE'), nullable=False)
    area_id = Column(Integer, nullable=False)
    ospfprocess = relationship('OSPFProcess')
    ospf_network = relationship('OSPFNetwork')

    def __repr__(self):
        return f"{self.__class__.__name__}(Router: {self.ospfprocess.router.routername} " \
               f"| Process: {self.ospfprocess.processid} " \
               f"| Area: {self.area_id})"


class OSPFNetwork(Base):
    __tablename__ = 'ospf_network'

    id = Column(Integer, primary_key=True)
    area_id = Column(Integer, ForeignKey("area.id", ondelete='CASCADE'), nullable=False)
    network = Column(String(64), nullable=False)
    wildmask = Column(String(64), nullable=False)
    area = relationship('Area')

    def __repr__(self):
        return f"{self.__class__.__name__}(Router: {self.area.ospfprocess.router.routername} " \
               f"| Process: {self.area.ospfprocess.processid} " \
               f"| Area: {self.area.area_id} " \
               f"| Network: {self.network}/{self.wildmask})"


class CPUUsage(Base):
    __tablename__ = 'cpu_usage'

    id = Column(Integer, primary_key=True)
    router_id = Column(Integer, ForeignKey("router.id", ondelete='CASCADE'), nullable=False)
    cpu_useage_percent = Column(Integer, nullable=False)
    cpu_useage_datetime = Column(DateTime(timezone='Asia/Chongqing'), default=datetime.datetime.now)
    router = relationship('Router')

    def __repr__(self):
        return f"{self.__class__.__name__}(Router: {self.router.routername} " \
               f"| Datetime: {self.cpu_useage_datetime} " \
               f"| Percent: {self.cpu_useage_percent})"


if __name__ == '__main__':
    # checkfirst=True，表示创建表前先检查该表是否存在，如同名表已存在则不再创建。其实默认就是True
    Base.metadata.create_all(engine, checkfirst=True)

