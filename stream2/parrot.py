class Parrot(Bird):
    def __init__(self):
        Bird.__init__(self, 'Parrot', 'Kah!')
        self.learned_phrases = set()

    def learn_phrase(self, phrase):
        self.learned_phrases.add(phrase)

    def do_call(self):
        Bird.do_call(self)
        print '\n'.join(self.learned_phrases)
        
parrot.do_call()