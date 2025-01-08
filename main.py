from fastapi import FastAPI

"""
FastAPI application for a simple Hello World API.
"""

app = FastAPI()

@app.get("/")
async def root():
    """
    Root endpoint that returns a Hello World message.
    Returns:
        dict: A dictionary containing a welcome message
    """
    return {"message": "Hello, World!"}
