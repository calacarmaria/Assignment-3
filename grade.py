from student import Student

class Grade(Student):
    def __init__(self, history, architecture, network, communication) -> None:
        self.history = history
        self.architecture = architecture
        self.network = network
        self.communication = communication

    def getAverage(self):
        return (int(self.history) + int(self.architecture) + int(self.network) + int(self.communication))/4