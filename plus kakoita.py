a = int(31536000)

class ch:

    def __init__ (self,voz):
        self.voz = voz

    def secondscalculator(self):
        print("soconds: ",self.voz*365*26*60*60)

one_ch = ch(20)
one_ch.secondscalculator()