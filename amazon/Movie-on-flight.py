# Input: movieDurations = [90, 85, 75, 60, 120, 150, 125], d = 250
# Output: [0, 6]
# Explanation: movieDurations[0] + movieDurations[6] = 90 + 125 = 215 is the maximum number within 220 (250min - 30min)ˀ

def flightdetails(movies: list,duration : int) -> list:
    movies = sorted(movies)
    l = 0
    r = len(movies)
    max_val = 0
    while l<r:
        if movies[l]+movies[r]<=duration:
            if max_val <= movies[l]+movies[r]:
                max_val = movies[l]+movies[r]
                i = l
                j = r
                l+=1
        else:
            r-=1
    return [movies[i],movies[j]]