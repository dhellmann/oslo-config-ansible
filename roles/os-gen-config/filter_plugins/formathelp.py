import textwrap

def formathelp(arg):
    return textwrap.fill(
        arg,
        initial_indent='# ',
        subsequent_indent='# ',
        width=79,
    ).rstrip() + '\n'


class FilterModule(object):
    def filters(self):
        return {'formathelp': formathelp}

