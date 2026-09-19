from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

items = []

@app.post("/items/")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int) -> dict:
    if item_id < 0 or item_id >= len(items):
        return {"error": "Item not found"}
    return {"item": items[item_id]}