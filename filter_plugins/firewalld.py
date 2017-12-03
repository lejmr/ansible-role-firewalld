

def do_protocolize(l, t="tcp"):
  return ["{}/{}".format(x,t) for x in l]

class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            # jinja2 overrides
            'protocolize': do_protocolize,
        }

