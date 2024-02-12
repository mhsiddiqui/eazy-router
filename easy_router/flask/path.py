from easy_router.base import Path


class FlaskPath(Path):
    def init(self):
        """
        Add route rules in app
        """
        self.root.add_url_rule(self.path, self._get_name(), view_func=self.view, **self.kwargs)


url = FlaskPath

