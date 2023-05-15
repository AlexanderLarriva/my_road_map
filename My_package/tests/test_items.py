from items import take

assert take([1, 2, 3], 2) == [1, 2]
assert take([1, 2, 3]) == [1]
assert take([1, 2, 3], 9) == [1, 2, 3]
assert take([], 9) == []
assert take([1, 2, 3], 0) == []
