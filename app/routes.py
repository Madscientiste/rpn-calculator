from fastapi import status, HTTPException, APIRouter, Response
from pydantic import BaseModel
from pandas import DataFrame, concat

from .utils import calculate, CalculatorError
from .database import Operation

router = APIRouter()


class Body(BaseModel):
    expression: str


@router.get("/health")
def health():
    return "Healthy: OK"


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

    # cleanup the expression from unnecessary spaces
    expr = " ".join(body.expression.split())

    try:
        response = {
            "expression": expr,
            "result": calculate(expr),
        }

        # Avoid storing the same expression multiple times.
        # Why storing the same expression multiple times?
        # NOTE: Maybe return the stored result instead of the calculated one?
        # probably useless as the calculation is not expensive. But it could be useful if it was.
        operation = Operation.get_by_expression(expr)
        if not operation:
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


@router.get("/export")
async def export():
    """
    ## Export all operations to a CSV file.

    This endpoint returns a CSV file with all operations stored in the database.
    The file is downloaded by the browser.

    **Returns**:
        file: A CSV file with all operations stored in the database.
    """
    operations = Operation.get_operations()

    keys = [col.name for col in Operation.__mapper__.columns if col != "id"]
    df = DataFrame([], columns=keys)

    for operation in operations:
        opdf = DataFrame([operation.to_dict()])
        df = concat([df.astype(opdf.dtypes), opdf.astype(df.dtypes)], ignore_index=True)

    return Response(
        content=df.to_csv(sep=";", index=False),
        media_type="text/csv",
        headers={"Content-Disposition": "attachment; filename=export.csv"},
    )
