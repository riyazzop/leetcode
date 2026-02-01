class RideSharingSystem(object):

    def __init__(self):
        self.riders=deque()
        self.drivers=deque()
        self.rides=set()

    def addRider(self, riderId):
        """
        :type riderId: int
        :rtype: None
        """
        self.riders.append(riderId)
        

    def addDriver(self, driverId):
        """
        :type driverId: int
        :rtype: None
        """
        self.drivers.append(driverId)
        

    def matchDriverWithRider(self):
        """
        :rtype: List[int]
        """
        if self.riders and self.drivers:
            self.rides.add(self.riders[0])
            return [self.drivers.popleft(),self.riders.popleft()]
        return [-1,-1]
        

    def cancelRider(self, riderId):
        """
        :type riderId: int
        :rtype: None
        """
        if riderId not in self.rides:
            try:
                self.riders.remove(riderId)
            except:
                pass


# Your RideSharingSystem object will be instantiated and called as such:
# obj = RideSharingSystem()
# obj.addRider(riderId)
# obj.addDriver(driverId)
# param_3 = obj.matchDriverWithRider()
# obj.cancelRider(riderId)