import threading
import time
import random

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
            
    def randomPlace(self,without = None) :
        places = ['Ransbach-Baumbach, Bergstraße 39a','Koblenz-Güls, Am Zehnthof 12',
                'Remagen, Joseph-Rovan-Allee 2', 'Koblenz, Bahnhofplatz 2',
                'Koblenz, Konrad-Zuse-Straße 1', 'Mülheim-Kärlich, Otto-Hahn-Straße 2-6']
        if without and without in places :
            places.remove(without)
            
        selection = random.choice(places)
        if without :
            places.append(without)

        return selection
        
