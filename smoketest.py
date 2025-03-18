from fastapi import FastAPI, HTTPException
# import tensorflow as tf
# from models import Grid
# from conway import iterate_grid
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

print("success")