from sqlalchemy.orm import sessionmaker
from sqlalchemy_sqlite3_create_table import Router, Interface, engine

Session = sessionmaker(bind=engine)
session = Session()

print(session.query(Router).filter(Router.routername.like('%CSR%')).all())  # 大小敏感
print(session.query(Router).filter(Router.routername.ilike('%csr%')).all())  # 大小不敏感

# join联合查询
filter_result = session.query(Router).join(Interface).filter(Interface.interface_name == 'GigabitEthernet1',
                                                             Router.routername.ilike('%csr%'),
                                                             Interface.ip == '137.78.5.254').one()
print(filter_result)

# 直接查询路由器CSR1的所有接口
for interface in filter_result.interface:
    # 向下查询
    print(interface.interface_name)
    print(interface.ip)
    # 向上反向查询
    print(interface.router.ospf_process.routerid)

# one to one 直接得到ospf_process
print(filter_result.ospf_process.routerid)


# 打印CSR1下的所有区域下的所有网络
for area in filter_result.ospf_process.area:
    for network in area.ospf_network:
        print(network)


if __name__ == '__main__':
    pass