class Path(object):
    def __init__(self, path, view, root=None, name='', **kwargs):
        self.path = path
        self.view = view
        self.name = name
        self.root = root
        self.kwargs = kwargs

    def __str__(self):
        """
        String representation of url
        :return: representation
        :rtype str
        """
        return '<url {view} ({url})>'.format(view=self._get_name(), url=self.path)

    def __repr__(self):
        """
        String representation of url
        :return: representation
        :rtype str
        """
        return self.__str__()

    def _get_name(self):
        """
        Get name of view
        :return: name of view
        :rtype str
        """
        if self.name:
            return self.name
        else:
            return '{root}:{name}'.format(root=self.root.name, name=self.view.__name__)

    def init(self):
        """
        Add route rules in app
        """
        raise NotImplemented

