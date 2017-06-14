def error(arg):
    raise RuntimeError(arg)


class FilterModule(object):
    def filters(self):
        return {'error': error}

