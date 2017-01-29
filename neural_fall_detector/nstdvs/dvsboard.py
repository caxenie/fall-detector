from . import retina


class DVSBoard(retina.Retina):
    def initialize(self):
        super(DVSBoard, self).initialize()
        
    def disconnect(self):
        super(DVSBoard, self).disconnect()

if __name__ == '__main__':
    import connection
    # enable testing for both cameras
    brd1 = DVSBoard()
    brd1.connect(connection.Serial('/dev/ttyUSB0', baud=12000000))
    brd1.track_frequencies(freqs=[50, 100, 150])
    brd1.retina(True)
    brd1.show_image()
    brd1.track_spike_rate(all=(0, 0, 128, 128))
    # brd2 = DVSBoard()
    # brd2.connect(connection.Serial('/dev/ttyUSB1', baud=12000000))
    # brd2.track_frequencies(freqs=[50, 100, 150])
    # brd2.retina(True)
    # brd2.show_image()
    # brd2.track_spike_rate(all=(0, 0, 128, 128))
    
    import time
    while True:
        time.sleep(1)
