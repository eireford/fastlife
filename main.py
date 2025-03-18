from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import tensorflow as tf
from models import Grid
from conway import iterate_grid
app = FastAPI()

# Comment out or remove the following lines to disable CORS

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/")
async def root():
    return {"message": "Hello World"}

@app.get("/tensorflow")
async def run_tensorflow_operation():
    try:
        # Simple TensorFlow operation
        a = tf.constant(2)
        b = tf.constant(3)
        result = tf.add(a, b).numpy()
        return {"result": int(result)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.post("/iterate")
async def iterate_conways_game_of_life(grid: Grid):
    try:
        new_grid = iterate_grid(grid.grid)
        return {"grid": new_grid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/iterate10")
async def iterate_conways_game_of_life(grid: Grid):
    try:
        new_grid = grid.grid
        for _ in range(10):
            new_grid = iterate_grid(new_grid)
        return {"grid": new_grid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/iterate100")
async def iterate_conways_game_of_life(grid: Grid):
    try:
        new_grid = grid.grid
        for _ in range(100):
            new_grid = iterate_grid(new_grid)
        return {"grid": new_grid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.post("/iterate1000")
async def iterate_conways_game_of_life(grid: Grid):
    try:
        new_grid = grid.grid
        for _ in range(1000):
            new_grid = iterate_grid(new_grid)
        return {"grid": new_grid}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))