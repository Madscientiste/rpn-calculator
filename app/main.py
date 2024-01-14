from fastapi import FastAPI
from starlette.responses import RedirectResponse

from fastapi.staticfiles import StaticFiles

from .routes import router

app = FastAPI(
    title="RPN Calculator",
    description="A simple RPN calculator",
)


app.mount("/calculator", StaticFiles(directory="resources/dist", html=True), name="calculator")
app.include_router(router, prefix="/api")


@app.get("/")
async def redirect():
    return RedirectResponse(url="/calculator")
