from .base import engine, Base
from .models import Operation
from .session import DBSession

# Making sure everything is imported and therefore all models will be registered
# before calling create_all() on the engine.
Base.metadata.create_all(bind=engine)
