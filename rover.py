# A program to calculate the time it takes for a photo to reach earth when transmitted from Mars
# Written by: Murray Coueslant, Date: 2017-09-08

# The Mars Curiosity rover takes photos of the Mars surface and then transmits them to NASA at the speed
# of light. Light travels at about 186,000 miles per second. When Mars is at its closest orbit to Earth,
# it is at a distance of about 34 million miles.

lightSpeed = 186000
distanceToMars = 34000000

# Speed = Distance / Time
photoTime = round(distanceToMars / lightSpeed, 2)

print("The photo takes", photoTime, "seconds to reach earth.")
