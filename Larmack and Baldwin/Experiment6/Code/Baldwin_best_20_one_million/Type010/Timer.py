# Name: Mei Jiaojiao
# Profession: Artificial Intelligence
# Time and date: 8/21/22 16:53
import datetime


class Timer():
    def __init__(self):
        self.total_time = 0.0
        self.start_time = None

    def start(self):
        self.start_time = datetime.datetime.now()

    def end(self):
        self.total_time += (datetime.datetime.now() - self.start_time).total_seconds()


# t1 = Timer()
# t2 = Timer()
# t3 = Timer()