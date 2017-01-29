import nengo
import numpy as np

import nstdvs

class RetinaNode(nengo.Node):
    def __init__(self, bot, msg_period):
        super(RetinaNode, self).__init__(self.retina, size_in=0, size_out=128*128)
        self.bot = bot
        self.msg_period = msg_period
        self.bot.show_image()

    def retina(self, t):
        return self.bot.image.flatten()


class FrequencyNode(nengo.Node):
    def __init__(self, bot, msg_period, freqs):
        super(FrequencyNode, self).__init__(self.freqs,
                                            size_in=0, size_out=len(freqs)*3)
        self.bot = bot
        self.bot.track_frequencies(freqs=freqs)
        self.msg_period = msg_period
        self.result = np.zeros(3*len(freqs), dtype='float')
        self.n_freqs = len(freqs)

    def freqs(self, t):
        for i in range(self.n_freqs):
            self.result[i * 3 : (i + 1) * 3] = self.bot.get_frequency_info(i)
        return self.result


class DVSBoardNetwork(nengo.Network):
    def __init__(self, connection, msg_period=0.01, label='DVSBoard', retina=True, freqs=[]):
        super(DVSBoardNetwork, self).__init__(label=label)
        self.bot = nstdvs.DVSBoard()
        self.bot.connect(connection)

        with self:
            if retina or freqs:
                self.bot.retina(True)
                if retina:
                    self.retina = RetinaNode(self.bot, msg_period=msg_period)
                if freqs:
                    self.freqs = FrequencyNode(self.bot, msg_period=msg_period, freqs=freqs)


