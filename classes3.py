class HourClock:
    def __init__(self, hours=0):
        self._hours = hours % 12

    @property
    def hours(self):
        return self._hours

    @hours.setter
    def hours(self, value):
        self._hours = value % 12

# Пример использования
clock = HourClock()
print(clock.hours)  # 0

clock.hours = 5
print(clock.hours)  # 5

clock.hours = 14
print(clock.hours)  # 2

clock.hours += 345
print(clock.hours)



