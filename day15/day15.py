import sys
import re
from collections import namedtuple

Point = namedtuple("Point", "x y")

def get_intervals(sensors, y):
    intervals = []
    for sensor, beacon in sensors:
        beacon_dist = abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)
        target_dist = abs(sensor.y - y)
        leftover = beacon_dist - target_dist
        if leftover >= 0:
            intervals.append(Point(sensor.x - leftover, sensor.x + leftover))

    intervals.sort()

    i = 0
    while i < len(intervals) - 1:
        if intervals[i].y + 1 >= intervals[i + 1].x:
            intervals[i] = Point(intervals[i].x, max(intervals[i].y, intervals[i + 1].y))
            del intervals[i + 1]
        else:
            i += 1
    return intervals

def get_covered(intervals, beacons, y):
    covered = sum(interval.y - interval.x for interval in intervals)

    for beacon in beacons:
        if beacon.y == y:
            for interval in intervals:
                if beacon.x == interval.x:
                    covered -= 1
    return covered

def find_beacon(sensors, max_val):
    for i in range(max_val + 1):
        # debug since this is slow
        # if i % 100000 == 0: print(i)
        intervals = get_intervals(sensors, i)
        if len(intervals) > 1:
            return i + (intervals[0].y + 1) * 4000000

def main():
    with open(sys.argv[1]) as f:
        sensors = []
        for line in f.readlines():
            vals = list(map(int, re.findall(r'=(-?[0-9]+)', line)))
            sensors.append([Point(vals[0], vals[1]), Point(vals[2], vals[3])])
        
    intervals = get_intervals(sensors, 2000000)
    beacons = [sensors[1] for sensors in sensors]
    print(get_covered(intervals, beacons, 2000000))

    print(find_beacon(sensors, 4000000))
    
if __name__ == '__main__':
    main()