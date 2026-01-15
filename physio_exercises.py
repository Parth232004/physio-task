# physio_exercises.py
# Defines physiotherapy exercises with safe angle ranges for basic movement validation
# Includes basic angle calculation functions using MediaPipe pose landmarks

import math

def calculate_angle(a, b, c):
    """
    Calculate the angle at point b formed by points a, b, c.
    Points are tuples of (x, y) coordinates.

    :param a: Point a (x, y)
    :param b: Point b (x, y)
    :param c: Point c (x, y)
    :return: Angle in degrees
    """
    # Vectors ba and bc
    ba = (a[0] - b[0], a[1] - b[1])
    bc = (c[0] - b[0], c[1] - b[1])

    # Dot product
    dot = ba[0] * bc[0] + ba[1] * bc[1]

    # Magnitudes
    mag_ba = math.sqrt(ba[0]**2 + ba[1]**2)
    mag_bc = math.sqrt(bc[0]**2 + bc[1]**2)

    # Cosine of angle
    cos_angle = dot / (mag_ba * mag_bc)

    # Clamp to avoid domain errors
    cos_angle = max(min(cos_angle, 1), -1)

    # Angle in radians, then degrees
    angle_rad = math.acos(cos_angle)
    angle_deg = math.degrees(angle_rad)

    return angle_deg

def get_shoulder_abduction_angle(landmarks):
    """
    Calculate shoulder abduction angle (arm raise).
    Angle at shoulder between torso and arm.

    :param landmarks: MediaPipe pose landmarks
    :return: Angle in degrees
    """
    # Landmarks: 11: left_shoulder, 12: right_shoulder, 13: left_elbow, 14: right_elbow, 23: left_hip, 24: right_hip
    # For right arm: shoulder (12), elbow (14), hip (24)
    shoulder = (landmarks[12].x, landmarks[12].y)
    elbow = (landmarks[14].x, landmarks[14].y)
    hip = (landmarks[24].x, landmarks[24].y)

    # Angle at shoulder: hip - shoulder - elbow
    return calculate_angle(hip, shoulder, elbow)

def get_elbow_flexion_angle(landmarks):
    """
    Calculate elbow flexion angle.
    Angle at elbow between upper arm and forearm.

    :param landmarks: MediaPipe pose landmarks
    :return: Angle in degrees (0 = straight, 180 = fully bent)
    """
    # For right arm: shoulder (12), elbow (14), wrist (16)
    shoulder = (landmarks[12].x, landmarks[12].y)
    elbow = (landmarks[14].x, landmarks[14].y)
    wrist = (landmarks[16].x, landmarks[16].y)

    # Angle at elbow: shoulder - elbow - wrist
    return calculate_angle(shoulder, elbow, wrist)

def get_shoulder_rotation_angle(landmarks):
    """
    Calculate shoulder rotation angle (approximation).
    For internal/external rotation, need arm at 90 degrees abduction.
    This is a simplified version using 2D pose.

    :param landmarks: MediaPipe pose landmarks
    :return: Dict with 'internal' and 'external' angles (simplified)
    """
    # Landmarks for right arm
    shoulder = (landmarks[12].x, landmarks[12].y)
    elbow = (landmarks[14].x, landmarks[14].y)
    wrist = (landmarks[16].x, landmarks[16].y)
    hip = (landmarks[24].x, landmarks[24].y)

    # Vector from hip to shoulder (torso direction)
    torso_x = shoulder[0] - hip[0]
    torso_y = shoulder[1] - hip[1]

    # Vector from shoulder to wrist (arm direction)
    arm_x = wrist[0] - shoulder[0]
    arm_y = wrist[1] - shoulder[1]

    # Calculate angle between torso and arm vectors
    dot = torso_x * arm_x + torso_y * arm_y
    mag_torso = math.sqrt(torso_x**2 + torso_y**2)
    mag_arm = math.sqrt(arm_x**2 + arm_y**2)

    if mag_torso == 0 or mag_arm == 0:
        return {"internal": 0, "external": 0}

    cos_angle = dot / (mag_torso * mag_arm)
    cos_angle = max(min(cos_angle, 1), -1)
    angle = math.degrees(math.acos(cos_angle))

    # Approximate internal/external based on wrist position relative to elbow
    # For right arm, if wrist is to the right of elbow, assume external rotation
    if wrist[0] > elbow[0]:
        return {"internal": 0, "external": angle}
    else:
        return {"internal": angle, "external": 0}

class PhysioExercise:
    def __init__(self, name, description, angle_ranges):
        """
        Initialize a physiotherapy exercise.

        :param name: Name of the exercise
        :param description: Brief description
        :param angle_ranges: Dict of angle names to (min, max) safe ranges in degrees
        """
        self.name = name
        self.description = description
        self.angle_ranges = angle_ranges

    def is_angle_safe(self, angle_name, angle_value):
        """
        Check if a given angle is within the safe range.

        :param angle_name: Name of the angle (e.g., 'shoulder_abduction')
        :param angle_value: Angle value in degrees
        :return: True if safe, False otherwise
        """
        if angle_name not in self.angle_ranges:
            return False
        min_angle, max_angle = self.angle_ranges[angle_name]
        return min_angle <= angle_value <= max_angle

# Define exercises based on common physiotherapy movements

ARM_RAISE = PhysioExercise(
    name="Arm Raise",
    description="Raise arm from side to overhead position, keeping elbow straight.",
    angle_ranges={
        "shoulder_abduction": (0, 180),  # Full range, but in rehab often limited to 0-90 initially
        "elbow_flexion": (0, 10)  # Keep elbow nearly straight, small tolerance for natural bend
    }
)

SHOULDER_ROTATION = PhysioExercise(
    name="Shoulder Rotation",
    description="Rotate shoulder internally and externally with arm at 90 degrees abduction.",
    angle_ranges={
        "shoulder_internal_rotation": (0, 70),
        "shoulder_external_rotation": (0, 90)
    }
)

ELBOW_FLEXION = PhysioExercise(
    name="Elbow Flexion",
    description="Bend and straighten the elbow joint.",
    angle_ranges={
        "elbow_flexion": (0, 150)  # Normal ROM for elbow flexion
    }
)

# List of all exercises
EXERCISES = {
    "arm_raise": ARM_RAISE,
    "shoulder_rotation": SHOULDER_ROTATION,
    "elbow_flexion": ELBOW_FLEXION
}