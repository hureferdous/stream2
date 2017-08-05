class Bird:
    def __init__(self, kind, call):
        self._kind = kind
        self._call = call

    def do_call(self):
        print 'a %s goes %s' % (self._kind, self._call)


owl = Bird('Owl', 'Twit Twoo!')
print owl._kind
print owl._call