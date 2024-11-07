class MyDict(dict):
    def get(self, __key, default=None):
        return super().get(__key, 0)
