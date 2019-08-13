""" Provided by Andre """


class time_portuguese:
    """
    This class returns a given time as a range of LED-indices.
    Illuminating these LEDs represents the current time on a portuguese WCA
    """

    def __init__(self):
        self.prefix1 = range(0,3) # -> sao
        self.prefix2 = range(3,4) # -> e
        self.minutes=[[], \
            # -> e cinco
            range(99,100) + range(102,107), \
            # -> e dez
            range(99,100) + range(107,110), \
            # -> e um quarto
            range(71,72) + range(100,102) + range(115,121), \
            # -> e vinte
            range(71,72) + range(88,93), \
            # -> e vinte e cinco
            range(71,72) + range(88,93) + range(99,100) + range(102,107), \
            # -> e meia
            range(71,72) + range(84,88), \
            # -> menos vinte e cinco
            range(78,83) + range(88,93) + range (99,100) + range(102,107), \
            # -> menos vinte
            range(78,83) + range(88,93), \
            # -> menos um quarto
            range(78,83) + range(100,102) + range(115,121), \
            # -> menos dez
            range(78,83) + range(107,110), \
            # -> menos cinco
            range(78,83) + range(102,107), \
            # -> horas
            range(72,77) ]

            # -> meia noite
        self.hours= [range(44,48) + range(59,64), \
            # -> uma
            range(8,11), \
            # -> duas
            range(4,8), \
            # -> tres
            range(18,22), \
            # -> quatro
            range(11,17), \
            # -> cinco
            range(28,33), \
            # -> seis
            range(23,27), \
            # -> sete
            range(48,52), \
            # -> oito
            range(33,37), \
            # -> nove
            range(55,59), \
            # -> dez
            range(41,44),\
            # -> onze
            range(66,70), \
            # -> meio dia
            range(37,41) + range(52,55), \
            # -> uma
            range(8,11) ]

    #self.fullhour = range(72,76)

    def get_time(self, time, purist):
        hour=time.hour % 12
        hour=hour+(1 if ((time.minute+5//2)//5 >= 7) else 0) #defines whether it should round to next hour index
        hour=hour+(12 if time.hour==12 else 0) #defines whether hour index is meio dia or meia noite

        minute=(time.minute+5//2)//5
        #if minute>12:
        #   minute=0
        #   hour=hour+1
        # Assemble indices
        return  \
            (self.prefix1 if not (purist and hour%12<2) else [self.prefix2]) + \
            self.minutes[minute] + \
            self.hours[hour]
