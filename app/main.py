import asyncio


async def fetch_data():
    asyncio.sleep(1)
    return {"data": "sample data"}


def process_data(data):
    return data["data"].upper()
