
MANDATORY_DIRECTORIES = [
    'controllers',
    'models',
    'views',
]


OPTIONAL_DIRECTORIES = [
    'static',
    'static/css',
    'static/js',
    'static/images',
]


NEW_CREATE_FILES = [
    # Format: ('template name', 'destination')
    ('app_controller.py.pystr', 'controllers/app_controller.py'),
    ('application.css.pystr', 'static/css/application.css'),
    ('base.html.pystr', 'views/base.html'),
]
