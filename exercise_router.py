# exercise_router.py
# Handles exercise selection and validation of detected movements against selected exercise

from physio_exercises import (
    EXERCISES,
    get_shoulder_abduction_angle,
    get_elbow_flexion_angle,
    get_shoulder_rotation_angle
)

def select_exercise(exercise_name):
    """
    Select an exercise by name.

    :param exercise_name: Name of the exercise (key in EXERCISES)
    :return: PhysioExercise object or None if not found
    """
    return EXERCISES.get(exercise_name.lower())

def validate_movement(exercise, landmarks):
    """
    Validate if the detected movement (landmarks) matches the selected exercise's safe ranges.

    :param exercise: PhysioExercise object
    :param landmarks: MediaPipe pose landmarks
    :return: Dict with validation results for each angle
    """
    results = {}
    angle_ranges = exercise.angle_ranges

    if "shoulder_abduction" in angle_ranges:
        angle = get_shoulder_abduction_angle(landmarks)
        results["shoulder_abduction"] = exercise.is_angle_safe("shoulder_abduction", angle)

    if "elbow_flexion" in angle_ranges:
        angle = get_elbow_flexion_angle(landmarks)
        results["elbow_flexion"] = exercise.is_angle_safe("elbow_flexion", angle)

    if "shoulder_internal_rotation" in angle_ranges or "shoulder_external_rotation" in angle_ranges:
        rotation_angles = get_shoulder_rotation_angle(landmarks)
        if "shoulder_internal_rotation" in angle_ranges:
            results["shoulder_internal_rotation"] = exercise.is_angle_safe("shoulder_internal_rotation", rotation_angles["internal"])
        if "shoulder_external_rotation" in angle_ranges:
            results["shoulder_external_rotation"] = exercise.is_angle_safe("shoulder_external_rotation", rotation_angles["external"])

    return results

def is_movement_valid(validation_results):
    """
    Check if all angles in the validation results are safe.

    :param validation_results: Dict from validate_movement
    :return: True if all safe, False otherwise
    """
    return all(validation_results.values())

if __name__ == "__main__":
    # Simple console interface to select exercise and simulate validation
    print("Available exercises:")
    for key in EXERCISES.keys():
        print(f"- {key}")

    exercise_name = input("Select an exercise: ").strip()
    exercise = select_exercise(exercise_name)

    if not exercise:
        print("Invalid exercise selected.")
    else:
        print(f"Selected: {exercise.name}")
        print("Note: This is a demo. In real use, provide actual MediaPipe landmarks.")
        # For demo, assume some dummy validation
        print("Validation logic ready. Provide landmarks to validate.")