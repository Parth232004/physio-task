# session_scoring.py
# Tracks per-exercise session scores based on consistency and completion quality

import statistics

class SessionScorer:
    def __init__(self, exercise_name):
        """
        Initialize scorer for a specific exercise.

        :param exercise_name: Name of the exercise
        """
        self.exercise_name = exercise_name
        self.frames = []  # List of dicts with angle data and validation

    def add_frame(self, angles, validations):
        """
        Add a frame's data.

        :param angles: Dict of angle names to values
        :param validations: Dict of angle names to bool (safe or not)
        """
        self.frames.append({"angles": angles, "validations": validations})

    def calculate_score(self):
        """
        Calculate the session score based on consistency and completion quality.

        :return: Score from 0-100
        """
        if not self.frames:
            return 0

        total_frames = len(self.frames)
        safe_frames = sum(1 for frame in self.frames if all(frame["validations"].values()))

        # Completion quality: percentage of frames with all angles safe
        completion_quality = (safe_frames / total_frames) * 100

        # Consistency: average deviation from safe ranges, but simplified as inverse of variance
        angle_names = list(self.frames[0]["angles"].keys())
        consistencies = {}
        for angle_name in angle_names:
            values = [frame["angles"][angle_name] for frame in self.frames]
            if len(values) > 1:
                variance = statistics.variance(values)
                # Lower variance = higher consistency
                consistency = max(0, 100 - variance)  # Arbitrary scaling
            else:
                consistency = 100
            consistencies[angle_name] = consistency

        average_consistency = statistics.mean(consistencies.values()) if consistencies else 100

        # Overall score: weighted average
        score = (completion_quality * 0.7) + (average_consistency * 0.3)

        return round(score, 2)

    def get_summary(self):
        """
        Get a summary of the session.

        :return: Dict with score and stats
        """
        score = self.calculate_score()
        total_frames = len(self.frames)
        safe_frames = sum(1 for frame in self.frames if all(frame["validations"].values()))

        return {
            "exercise": self.exercise_name,
            "total_frames": total_frames,
            "safe_frames": safe_frames,
            "score": score
        }

# Example usage
if __name__ == "__main__":
    scorer = SessionScorer("arm_raise")
    # Simulate adding frames
    # In real use, integrate with video processing
    print("Session scoring module ready.")