from datetime import datetime, timezone
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import config
import httpx


app = FastAPI()

async def fetch_cat_fact() -> str:
    """Fetch a random cat fact from Cat Facts API with error handling."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(config.CAT_FACT_API)
            response.raise_for_status()
            data = response.json()
            return data.get("fact", "Cats are mysterious creatures!")  # fallback
    except Exception:
        return "Could not fetch a cat fact at this time."


@app.get("/me")
async def get_profile():
    fact = await fetch_cat_fact()
    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")

    payload = {
        "status": "success",
        "user": {
            "email": config.EMAIL,
            "name": config.NAME,
            "stack": config.STACK
        },
        "timestamp": timestamp,
        "fact": fact
    }
    return JSONResponse(content=payload, status_code=status.HTTP_200_OK)