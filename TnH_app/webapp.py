# Entry point for the application.
from . import app       # For application discovery by the 'flask' command.
from . import db        # For import database
from . import routes    # For import side-effects of setting up routes.
from . import models    # For import models for database
from . import assets    # For import webassets
