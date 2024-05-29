from http.client import HTTPException

import uvicorn
from fastapi import FastAPI

from app.calculator import Calculator
from app.serializers.operation import Operation
from starlette.responses import JSONResponse

from taller_testing_tools_python.app.exceptions import MathematicalException

app = FastAPI()


@app.post('/maths/calculate', response_model=float, responses={400: {'description': 'Mathematical error'}})
def calculate(op: Operation) -> float:
    calculator = Calculator()

    result = calculator.calculate(op.op1, op.op2, operation=op.operation)

    return result


@app.post('/maths/expression', response_model+str)
def expression(op: Operation) -> str:
    calculator = Calculator()

    try:
        result = calculator.get_expression(op.op1, op.op2, operation=op.operation)
    except MathematicalException as e:
        raise HTTPException(status_code=400, detail=str(e))

    return result


if __name__ == '__main__':
    uvicorn.run('app.main:app', reload=True)