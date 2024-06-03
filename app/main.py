import asyncio
import time


async def fetch_data():
    asyncio.sleep(1)
    return {"data": "sample data"}


def process_data(data):
    return data["data"].upper()


for count in range(10):
    print(process_data({"data": "sample data"}), count)
    count += 1
    time.sleep(1)
