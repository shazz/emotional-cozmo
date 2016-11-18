import random
import math

from . import stimulus

class Vision(object):
    """ Interacts with the vision sensor and records stimuli """

    def __init__(self, perception_system):
        self.perception_system = perception_system

        # For testing!
        self.test_target = random.randint(-100, 100)
        self.test_current = 0

        self.test_face = stimulus.FaceStimulus(self.perception_system)
        self.test_face.id = 'face-1'
        self.perception_system.stimuli[self.test_face.id] = self.test_face

    def update(self, elapsed):
        self.test_update(elapsed)

    def test_update(self, elapsed):
        """ Generate random detections and disappearances for a stimulus """
        if self.test_current == self.test_target:
            self.test_target = random.randint(-100, 100)

        delta = min(math.floor(random.randint(0, 40) * elapsed), abs(self.test_target - self.test_current))
        
        if self.test_current < self.test_target:
            self.test_current += delta
        else:
            self.test_current -= delta

        # Generate events based upon this smooth randomness
        if self.test_current > 0:
            self.test_face.detect()
        else:
            self.test_face.disappear()