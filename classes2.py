# class Foo:
#   def bar():
#     pass

# x = Foo()

# class Counter:
#     value = 0

#     def inc(self, delta=1):
#         self.value += delta
#         # return self.value

#     def dec(self, delta=1):
#         self.value -= delta
#         if self.value < 0:
#             self.value = 0
#         # return self.value
    
# c = Counter()

# c = Counter()
# print(c.inc())
# print(c.inc())
# print(c.inc(40))
# c.value  # 42
# print(c.dec())
# print(c.dec(30))
# c.value  # 11
# print(c.dec(delta=100))
# c.value  # 0

########################################

class Counter:
    def __init__(self, initial_value=0):
        if initial_value < 0:
            self._value = 0
        self._value = initial_value

    def inc(self, delta=1):
        return Counter(self._value + delta)

    def dec(self, delta=1):
        new_value = self._value - delta
        if new_value < 0:
            new_value = 0
        return Counter(new_value)

    @property
    def value(self):
        return self._value


# c = Counter()
# print(c.inc().inc(5).dec(2).value)  # 4
 
# # Старый экземпляр не должен изменяться
# d = c.inc(100)
# print(d.dec().value)  # 99
 
# forty_two = Counter(42)
# forty_two.value  # 42

# d = c.inc(-100)
# print(d.dec().value)  # 0

class LimitedCounter(Counter):
    def __init__(self, limit):
        super().__init__(0)
        self.limit = limit
        
    def inc(self, count=1):
        super().inc(count)
        if self.value > self.limit:
            self.value = self.limit
            
    def dec(self, count=1):
        super().dec(count)
        if self.value < 0:
            self.value = 0
            
counter1 = LimitedCounter(limit=10)
counter1.inc()
counter1.inc(7)
print(counter1.value)  # 8
# counter.dec(10)
# print(counter.value) 




