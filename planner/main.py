from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.users import user_router
from routes.todo import todo_router
from routes.events import event_router
from database.connection import conn
import uvicorn

app = FastAPI()

# Register routes
app.include_router(user_router, prefix="/user")
app.include_router(event_router, prefix="/event")
app.include_router(todo_router)

@app.on_event("startup")
async def on_startup():
  conn()

@app.get("startup")
async def home():
  return RedirectResponse(url="/event/") 

if __name__ == "__main__":
  uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)