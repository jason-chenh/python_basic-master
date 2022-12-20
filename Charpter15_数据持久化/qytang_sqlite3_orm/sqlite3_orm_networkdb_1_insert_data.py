from sqlalchemy.orm import sessionmaker
from sqlite3_orm_create_table import Router, Interface, OSPFProcess, Area, OSPFNetwork, engine

Session = sessionmaker(bind=engine)
session = Session()


# 设备接口信息
csr1_ifs = [{'ifname': "GigabitEthernet1", 'ip': "137.78.5.254", 'mask': "255.255.255.0"},
            {'ifname': "GigabitEthernet2", 'ip': "61.128.1.254", 'mask': "255.255.255.0"},
            {'ifname': "Loopback0", 'ip': "1.1.1.1", 'mask': "255.255.255.255"}]

csr2_ifs = [{'ifname': "GigabitEthernet1", 'ip': "61.128.1.1", 'mask': "255.255.255.0"},
            {'ifname': "GigabitEthernet2", 'ip': "202.100.1.1", 'mask': "255.255.255.0"},
            {'ifname': "Loopback0", 'ip': "2.2.2.2", 'mask': "255.255.255.255"}]

# 设备OSPF信息
csr1_ospf = {"process_id": 1,
             "router_id": "1.1.1.1",
             "areas": [{'area_id': 0, 'networks': [{'ip': "137.78.5.0", 'wildmask': "0.0.0.255"},
                                                   {'ip': "61.128.1.0", 'wildmask': "0.0.0.255"},
                                                   {'ip': "1.1.1.1", 'wildmask': "0.0.0.0"}]}]}

csr2_ospf = {"process_id": 1,
             "router_id": "2.2.2.2",
             "areas": [{'area_id': 0, 'networks': [{'ip': "61.128.1.0", 'wildmask': "0.0.0.255"},
                                                   {'ip': "202.100.1.0", 'wildmask': "0.0.0.255"},
                                                   {'ip': "2.2.2.2", 'wildmask': "0.0.0.0"}]}]}

# 汇总后数据
all_network_data = [{'ip': "192.168.1.1", 'routername': 'CSR1', 'interfaces': csr1_ifs, 'ospf': csr1_ospf},
                    {'ip': "192.168.1.2", 'routername': 'CSR2', 'interfaces': csr2_ifs, 'ospf': csr2_ospf}]

# 把之前的内容删除
session.query(Router).delete()


for device in all_network_data:
    # 添加Router
    router_device = Router(routername=device['routername'], ip=device['ip'])
    session.add(router_device)

    # 添加Interface
    for ifs in device['interfaces']:
        new_if = Interface(router=router_device, interface_name=ifs['ifname'], ip=ifs['ip'], mask=ifs['mask'])
        session.add(new_if)

    # 添加OSPFProcess
    router_device_process = OSPFProcess(router=router_device,
                                        processid=device["ospf"]["process_id"],
                                        routerid=device["ospf"]["router_id"])

    # 添加Area
    for device_area in device["ospf"]["areas"]:
        router_device_area = Area(ospf_process=router_device_process, area_id=device_area["area_id"])
        session.add(router_device_area)

        # 添加Area下的每一个OSPFNetwork
        for net in device_area["networks"]:
            new_net = OSPFNetwork(area=router_device_area, network=net['ip'], wildmask=net['wildmask'])
            session.add(new_net)

session.commit()
