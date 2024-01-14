# Reverse Łukasiewicz Notation

Reverse Polish notation, also known as Polish postfix notation or simply postfix notation, is a mathematical notation in which operators follow their operands, in contrast to Polish notation (PN), in which operators precede their operands. It does not need any parentheses as long as each operator has a fixed number of operands.

### Tech Stack

-   Python & FastAPI
-   React & TypeScript
-   Docker

## Development

I'm using [Rye](https://rye-up.com/), an experimental package management solution created by the author of [Flask](https://flask.palletsprojects.com/en/3.0.x/).

You probably don't have it, doing it the good old way `pip install -r requirements-dev.lock` should be good enough.

Otherwise you can just do `rye sync` to install the dependencies.

#### Running Tests

```bash
rye run test

# or if you are not using rye
pytest
```

#### Running the project

```bash
rye run dev

# or if you are not using rye
uvicorn app:server --reload
```

Not forgetting to build the frontend

```bash
cd resources

npm i && npm run build
```

-   Then the app will be available at [http://localhost:5050/calculator](http://localhost:5050/calculator).
-   The API will be available at [http://localhost:5050/api](http://localhost:5050/api).
-   And the docs will be available at [http://localhost:5050/docs](http://localhost:5050/docs).
