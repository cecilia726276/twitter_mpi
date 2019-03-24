class MelbGrid(object):
    def __init__(self, id, xmin, xmax, ymin, ymax):
        self.id = id
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

    def checkInGrid(self, x, y):
        if x >= self.xmin and x <= self.xmax and y >= self.ymin and y <= self.ymax:
            return True
        return False
