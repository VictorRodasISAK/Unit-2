from Quiz_031_Library import get_sensor, smoothing

s1 = get_sensor(id=1)
s2 = get_sensor(id=2)
s3 = [a + b for a, b in zip(s1, s2)]

