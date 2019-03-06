from collections import OrderedDict

from aiohttp_utils import negotiation
from aiohttp_utils import path_norm

from demo import views
from demo.utils import JSONRender


def setup_routes(app):
    # test routes
    app.router.add_route('GET', '/hello', views.hello)
    app.router.add_route('GET', '/version', views.version)
    app.router.add_route('GET', '/user/{id:[0-9a-fA-F]{32}}', views.get_user)
    app.router.add_route('POST', '/validate_profile', views.profile_validation)

    negotiation.setup(
        app,
        renderers=OrderedDict([
            ('application/json', JSONRender())
        ])
    )
    path_norm.setup(app, merge_slashes=True)
