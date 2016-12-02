
MANDATORY_DIRECTORIES = [
    ['controllers',],
    ['models',],
    ['views',],
]


OPTIONAL_DIRECTORIES = [
    ['static'],
    ['static', 'css'],
    ['static', 'js'],
    ['static', 'images'],
]


NEW_CREATE_FILES = [
    # Controllers
    {'template': 'app_controller.py.pystr', 'dest_dir': ['controllers']},
    # Static files
    {'template': 'application.css.pystr', 'dest_dir': ['static', 'css']},
    # Views
    {'template': 'base.html.pystr', 'dest_dir': ['views']},
]
