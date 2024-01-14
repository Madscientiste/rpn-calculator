from fastapi import status, HTTPException, APIRouter
from pydantic import BaseModel

from .utils import calculate, CalculatorError
from .models import Operation

router = APIRouter()


class Body(BaseModel):
    expression: str


@router.post("/calc")
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
        response = {
            "expression": body.expression,
            "result": calculate(body.expression),
        }

        # Will do the job for now.
        Operation.create_operation(**response)

        return response
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
