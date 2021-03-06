from txros import util
from sub8 import pose_editor

SIDE_LENGTH = 1  # meters
SPEED_LIMIT = .2  # m/s

@util.cancellableInlineCallbacks
def run(sub):
    print "Heil!"
    
    center = sub.move.forward(0).zero_roll_and_pitch()
    for i in range(4):
        forward = sub.move.forward(SIDE_LENGTH).zero_roll_and_pitch()
        right = forward.right(SIDE_LENGTH).zero_roll_and_pitch()

        yield forward.go(speed=SPEED_LIMIT)
        yield right.go(speed=SPEED_LIMIT)
        yield forward.go(speed=SPEED_LIMIT)
        yield center.go(speed=SPEED_LIMIT)
        center = center.yaw_right_deg(90)
        yield center.go(speed=SPEED_LIMIT)

    print "Done!"
