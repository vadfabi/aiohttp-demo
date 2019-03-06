import ujson


class JSONRender:
    json_module = ujson

    def __call__(self, request, data):
        return self.json_module.dumps(data).encode('utf-8')
