import importlib
from typing import Any
from .router import Router


class RouteHandler(object):
    _urls = []

    def __init__(self, config=None):
        if not (config is None or isinstance(config, dict)):
            raise ValueError("`config` must be an instance of dict or None")
        self.config = config

    def get_paths(
        self, root: Any, router: Router
    ):
        raise NotImplemented

    def init(self, app: Any):
        self.set_paths(app)
        for url in self._urls:
            url.init()

    def set_paths(self, app: Any):
        for url_path in self.config.get('ROUTER_MODULES', []):
            router = importlib.import_module(url_path)
            if hasattr(router, 'router'):
                self.get_paths(app, router.router)
            else:
                raise AttributeError(f"{url_path} must be an attribute 'router' of type 'Router'")

