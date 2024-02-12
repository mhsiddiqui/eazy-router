from typing import Any

from .path import Path
from .router import Router
from easy_router.base import RouteHandler


class FlaskRouteHandler(RouteHandler):
    def get_paths(self, root: Any, router: Router):
        if hasattr(router, 'root'):
            root.register_blueprint(router.root)
            root = router.root
        paths = router.urls
        for path in paths:
            if isinstance(path, Path):
                path.root = root
                self._urls.append(path)
            else:
                return self.get_paths(root, path)
