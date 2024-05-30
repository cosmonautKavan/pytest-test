import pytest
import asyncio
from app.main import fetch_data, process_data

@pytest.mark.asyncio
async def test_fetch_data():
    data = await fetch_data()
    assert data == {"data": "sample data"}
    
def test_process_data():
    result = process_data({"data": "sample data"})
    assert result == "SAMPLE DATA"