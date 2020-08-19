import threading
import time

class RouteSimulator :
    def __init__(self) :
        self.routeKm = 0
        self.sleepTime = 5
        self.running = False
        self.simThread = threading.Thread(target = self.simulate , args=())
        self.tlock = threading.Lock()

    def __del__(self) :
        self.stopThread()

    def startThread(self) :
        self.running = True
        self.simThread.start()

    def stopThread(self) :
        self.running = False
        self.simThread.join()
        self.simThread = threading.Thread(target = self.simulate , args=())
        self.routeKm = 0

    def simulate(self) :
        while self.running :
            self.tlock.acquire()
            self.routeKm += 0.1 # this is equal to 72 km/h
            self.tlock.release()
            time.sleep(self.sleepTime)
            
