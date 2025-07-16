import asyncio

async def say_hello():
    print('Hello')
    await asyncio.sleep(2)
    print('World')

#asyncio.run(say_hello())

async def fetch_data(url, delay):
    print(f'Загрузка данных из {url}...')
    await asyncio.sleep(delay=delay)
    print(f'Данные из запроса {url} получены')

async def main():
    task1 = asyncio.create_task(fetch_data("https://api.example.com/data1", 2))
    task2 = asyncio.create_task(fetch_data("https://api.example.com/data1", 1))

    await say_hello()
    await task1
    await task2


asyncio.run(main())