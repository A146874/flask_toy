import statistics

class MeanModel():
    def __init__(self):
        pass
    
    def predict(self, x):
        return statistics.mean(x)
