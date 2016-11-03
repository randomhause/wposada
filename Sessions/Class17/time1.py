class Time:
    """
    Represent the time of day. 

    attributes: hour, minutes, seconds

    """
    
    def print_time(self):
        """Prints  string representation of the time."""
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        """Returns time in seconds format"""
        minutes = self.hour *60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds 

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def increment(self, seconds): #add seconds to it
        seconds += self.time_to_int()
        return int_to_time(seconds)

def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


start = Time()
start.hour = 9
start.minute = 45
start.second = 0

# Two ways to call:
#Time.print_time(start)
start.print_time()
print(start.time_to_int())

end = start.increment(2000) #adding seconds to it 9:45
end.print_time()
print(end.is_after(start))

traffic = Time()
traffic.hour = 0
traffic.minute = 30
traffic.second = 0

expected_time = Time()
expected_time.hour = 10
expected_time.minute = 15
expected_time.second = 0

traffic.print_time()
expected_time.print_time()
print(start.is_as_expected(traffic, expected_time))