from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

from utils import calculate

app = FastAPI(
    title="RPN Calculator",
    description="A simple RPN calculator",
)

app.mount("/", StaticFiles(directory="resources/dist", html=True), name="static")


class Body(BaseModel):
    expression: str


@app.post("/")
async def root(body: Body):
    """
    ## Calculate the result of a Reverse Polish Notation (RPN) expression.

    This endpoint accepts a JSON object with a single field `expr` that contains a string of space-separated numbers and operators in RPN format.
    It returns a JSON object with the fields `expression` and `result`, where `expression` is the input expression and `result` is the calculated result of the given expression.

    **Returns**:
        dict: A dictionary with the input `expression` and the `result` of the calculation.

    **Example**:

        Request:
        { "expression": "3 4 + 5 *" }

        Response:
        { "expression": "3 4 + 5 *", "result": 35 }
    """
    return {
        "expression": body.expression,
        "result": calculate(body.expression),
    }
