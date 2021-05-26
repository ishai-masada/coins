import math

class Vector2:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, isinstance(b, Vector2):
        return Vector2(x + b.x, y + b.y)


    def __truediv__(self, isinstance(b, (int, float)):
        return self(x/b, y/b)


    def point(self):
    return "something"


def ball_throw(ang, speed):
    """ angle is in degrees and speed in meters/second"""
    
    ball_throw_dict = dict()
    # Convert angle to radians
    converted_ang = (ang * math.pi) / 180

    # Get the vertical speed of the ball
    v_speed = speed * math.sin(converted_ang)
    
    acceleration = 9.8
    
    # Calculate the time it takes for ball to land
    time = round(2 * v_speed/acceleration, 2)

    # Check to see if trig functuion made time negative
    if time < 0:
        time = -1 * time

    # Use the range equation to find the distance
    distance = round((speed**2 * math.sin(2*converted_ang))/ acceleration, 2)

    # Store time and distance into dictionary
    ball_throw_dict["distance"] = distance
    ball_throw_dict["time"] = time

    return fysics_dict


def simulated_ball_throw(ang, speed):
    acceleration = 9.8
    simulated_dict = dict()
    steps_per_sec = 500
    position = Vector2()
    converted_ang = (ang * math.pi) / 180
    v_speed = speed * math.sin(converted_ang)
    h_speed = speed * math.cos(converted_ang)
    velocity = Vector2(v_speed, h_speed)
 
    
    while True:
        position.x += velocity.x/steps_per_sec
        position.y += velocity.y/steps_per_sec
        velocity.y -= 9.8/steps_per_sec
        distance = abs(round(position.x, 1))
        
        
        # Calculate the time it takes for ball to land
        time = round(2 * v_speed/acceleration, 2)

        # Check to see if trig functuion made time negative
        if time < 0:
            time = -1 * time

        # Verify the velocity to find the maximum height
        if velocity.y >= 0:
            max_altitude = round(position.y, 2)
            
            # Store the maximum altitude into the dictionary
            simulated_dict["maximum height"] = max_altitude

            # Find the magnitude of the vector
            hyp_vel = (h_speed**2 + v_speed**2)**.5

            #Store the max velocity into the dictionary
            simulated_dict["maximum velocity"] = round(hyp_vel, 2)

        # Store time and range into dictionary
        if position.y < 0:
            simulated_dict["distance"] = distance
            simulated_dict["time"] = time
            return simulated_dict
    
