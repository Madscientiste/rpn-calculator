from starlette.responses import RedirectResponse
from fastapi import FastAPI, status, HTTPException
from pydantic import BaseModel

from fastapi.staticfiles import StaticFiles

from utils import calculate, CalculatorError

app = FastAPI(
    title="RPN Calculator",
    description="A simple RPN calculator",
)


app.mount("/calculator", StaticFiles(directory="resources/dist", html=True), name="calculator")


class Body(BaseModel):
    expression: str


@app.get("/")
async def redirect():
    return RedirectResponse(url="/calculator")


@app.post("/api/calc")
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

    try:
        return {
            "expression": body.expression,
            "result": calculate(body.expression),
        }
    except Exception as e:
        raise HTTPException(
            detail=str(e),
            #
            # Return a 400 Bad Request status code if the error is a CalculatorError,
            # otherwise return a 500 Internal Server Error status code.
            status_code=status.HTTP_400_BAD_REQUEST
            if isinstance(e, CalculatorError)
            else status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
