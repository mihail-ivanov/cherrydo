
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


REQUIREMENTS = [
    'cherrypy',
    'jinja2',
    'sqlalchemy',
]


NEW_CREATE_FILES = [
    {
        'template_name': 'gitignore',
        'destination': '.gitignore',
        'skip_format': True,
    },

    {
        'template_name': 'site_config.py',
        'destination': 'site_config.py',
        'skip_format': True,
    },

    {
        'template_name': 'run.py',
        'destination': 'run.py',
        'skip_format': True,
    },

    {
        'template_name': 'app_controller.py.pystr',
        'destination': 'controllers/app_controller.py',
    },

    {
        'template_name': 'app_model.py.pystr',
        'destination': 'models/app_model.py',
    },

    {
        'template_name': 'application.css.pystr',
        'destination': 'static/css/application.css',
    },

    {
        'template_name': 'application.js.pystr',
        'destination': 'static/js/application.js',
    },

    {
        'template_name': 'base.html.pystr',
        'destination': 'views/base.html',
    },
]


GENERATE_CONTROLLER = [
    {
        'template_name': '_controller.py.pystr',
        'destination': 'controllers/{controller_name}_controller.py',
    },

    {
        'template_name': '_css.css.pystr',
        'destination': 'static/css/{controller_name}.css',
    },

    {
        'template_name': '_js.js.pystr',
        'destination': 'static/js/{controller_name}.js',
    },
]


GENERATE_CONTROLLER_VIEW = {
    'template_name': '_controller_view.py.pystr',
}
