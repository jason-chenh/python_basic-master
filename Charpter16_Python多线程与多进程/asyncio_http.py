import requests
import asyncio
import os
import threading

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


async def pressure_test(host, task_id):
    print(f'ID: {task_id} Started')
    print(os.getpid(), threading.currentThread().ident)
    # awaitable loop.run_in_executor(executor, func, *args)
    # requests.get 这个位置是函数
    # host 是参数
    result = await loop.run_in_executor(None, requests.get, host)
    print(f'ID: {task_id} Stopped')
    return result.status_code


def pressure_test_main(conns, url):
    tasks = []

    for i in range(conns):
        task = loop.create_task(pressure_test(url, i))
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))

    result_list = []
    for i in tasks:
        result_list.append(i.result())

    return result_list


if __name__ == '__main__':
    print(pressure_test_main(5, 'http://www.baidu.com'))
