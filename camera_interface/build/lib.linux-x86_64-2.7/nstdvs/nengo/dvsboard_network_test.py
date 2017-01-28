import nstdvs
import nengo


model = nengo.Network()
with model:
    brd1 = nstdvs.DVSBoardNetwork(
            nstdvs.Serial('/dev/ttyUSB0', baud=12000000),
            retina=True, freqs=[100, 200, 300],
            msg_period=0.01)

    brd2 = nstdvs.DVSBoardNetwork(
            nstdvs.Serial('/dev/ttyUSB1', baud=12000000),
            retina=True,  freqs=[100, 200, 300],
            msg_period=0.01)
