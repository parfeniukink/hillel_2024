import httpx
import random
import string
from typing import Callable

import requests
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

create_random_string: Callable[[int], str] = lambda size: "".join(
    [random.choice(string.ascii_letters) for _ in range(size)]
)


@app.get("/generate-article")
async def get_information():
    """This endpoint returns the random information"""

    return {
        "title": create_random_string(size=10),
        "description": create_random_string(size=20),
    }


@app.get("/fetch-market")
async def get_current_market_state():
    """Response example:
       {
        "Realtime Currency Exchange Rate": {
            "1. From_Currency Code": "UAH",
            "2. From_Currency Name": "Ukrainian Hryvnia",
            "3. To_Currency Code": "USD",
            "4. To_Currency Name": "United States Dollar",
            "5. Exchange Rate": "0.02610000",
            "6. Last Refreshed": "2024-03-07 17:45:47",
            "7. Time Zone": "UTC",
            "8. Bid Price": "0.02609000",
            "9. Ask Price": "0.02610000"
        }
    }
    """
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=UAH&to_currency=USD&apikey=V2V43QAQ8RILGBOW"

    async with httpx.AsyncClient() as client:
        
        response: httpx.Response = await client.get(url)
    # await asyncio.sleep(5)
    rate: str = response.json()["Realtime Currency Exchange Rate"][
        "5. Exchange Rate"
    ]

    return {"rate": rate}
