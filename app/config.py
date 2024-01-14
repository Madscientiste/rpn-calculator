import pathlib

SQLITE_PATH = pathlib.Path(__file__).parent.parent / "database.sqlite"

# making sure the "dist" folder is created because otherwise FastAPI complain
(pathlib.Path(__file__).parent.parent / "resources" / "dist").mkdir(exist_ok=True)
