# RPN Calculator

-   Served with [FastAPI](https://fastapi.tiangolo.com/).
-   Tested with [pytest](https://docs.pytest.org/en/stable/).

## Usage

### Run

```bash
docker-compose up
```

### Test

```bash
docker-compose run --rm app pytest
```

### API Documentation

#### POST /

**Request Body**:

```json
{ "expression": "1 2 + 4 * 3 +" }
```

**Response**:

```json
{ "expression": "1 2 + 4 * 3 +", "result": 15 }
```
