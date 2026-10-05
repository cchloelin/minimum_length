import math
import statistics
from data_extraction import primordial_realization
# ^ temporary, will be replaced with arbitrary power spectrum data later

blurring_radius = 120
data = primordial_realization().tolist()
nearby_points = {}

def blurring():
    """Calculate which points are within the blurring radius and save it."""
    for a in range(len(data)):
        points_within_range = []
        for b in range(len(data)):
            point_a = data[a]
            point_b = data[b]
            if point_a != point_b:
                if math.dist(point_a[0:3], point_b[0:3]) <= blurring_radius:
                    #print(math.dist(point_a[0:3], point_b[0:3]))
                    points_within_range.append(point_b)
        nearby_points[a] = points_within_range

    """Find the average of points within the radius."""
    for points, neighbors in nearby_points.items():
        random_values = []
        for point in neighbors:
            random_values.append(point[-1])
        average = statistics.mean(random_values)
        data[points][-1] = average

    # maybe edit to only return the last value
    return data

#print(blurring())