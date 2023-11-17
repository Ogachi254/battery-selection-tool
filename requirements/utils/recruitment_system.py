# recruitment_system.py
from random import randint

class RecruitmentSystem:
    @staticmethod
    def personality_test(candidate):
        """
        Implement a personality test logic.
        Example: Assess the candidate's adaptability by asking questions related to handling change.
        Return a score (1-100) based on the candidate's responses.
        """
        adaptability_score = randint(1, 100)
        return adaptability_score

    @staticmethod
    def cognitive_ability_test(candidate):
        """
        Implement a cognitive ability test logic.
        Example: Assess problem-solving skills by presenting a hypothetical scenario.
        Return a score (1-100) based on the candidate's performance.
        """
        problem_solving_score = randint(1, 100)
        return problem_solving_score

    @staticmethod
    def interview_questions():
        """
        Define interview questions.
        """
        questions = [
            "Can you describe a challenging situation you faced at work and how you handled it?",
            "How do you prioritize tasks when faced with multiple deadlines?",
            "Describe a situation where you had to work with a difficult team member. How did you handle it?",
            "Give an example of a time when you had to meet a tight deadline. How did you manage it?",
            "How do you stay updated with industry trends and advancements?",
            "Describe a situation where you had to adapt to a major change in a project. How did you handle it?",
            # Add more questions as needed
        ]
        return questions

    @staticmethod
    def ideal_answers():
        """
        Define ideal answers for interview questions.
        """
        return [
            "An ideal answer involves describing the situation, the actions taken, and the positive outcome. It demonstrates problem-solving and communication skills.",
            "An ideal answer includes a systematic approach to prioritization, considering urgency and importance.",
            "An ideal answer involves addressing the difficult situation diplomatically, attempting resolution, and ensuring a positive team dynamic.",
            "An ideal answer includes effective time management, prioritization, and possibly collaboration with team members to meet the deadline.",
            "An ideal answer involves a proactive approach to staying informed, such as reading industry publications, attending conferences, or participating in relevant online forums.",
            "An ideal answer involves demonstrating adaptability, flexibility, and a positive attitude in response to changes.",
            # Add more ideal answers as needed
        ]

    @staticmethod
    def rating_criteria():
        """
        Define rating criteria for interview questions.
        """
        return [
            "Rate based on clarity, problem-solving approach, and positive outcomes.",
            "Rate based on the systematic approach and understanding of task priorities.",
            "Rate based on diplomacy, conflict resolution, and maintaining a positive team environment.",
            "Rate based on time management, prioritization, and collaboration skills.",
            "Rate based on the candidate's proactive efforts to stay informed about industry trends.",
            "Rate based on adaptability, flexibility, and maintaining a positive attitude during change.",
            # Add more rating criteria as needed
        ]

    @staticmethod
    def rate_answers(answers):
        """
        Implement a rating system for interview answers.
        Example: Rate answers based on clarity, problem-solving, and communication skills.
        Return a score (1-10) for each answer.
        """
        return [randint(1, 10) for _ in range(len(answers))]

    @staticmethod
    def filter_candidates(candidates):
        """
        Implement candidate filtering logic using selection tools.
        Example: Filter candidates based on personality, cognitive ability, and interview ratings.
        """
        filtered_candidates = []
        for candidate in candidates:
            personality_score = RecruitmentSystem.personality_test(candidate)
            cognitive_score = RecruitmentSystem.cognitive_ability_test(candidate)
            interview_answers = candidate.interview_answers.all()
            interview_scores = RecruitmentSystem.rate_answers(interview_answers)

            # Customize the filtering criteria based on your requirements
            if (
                personality_score > 70
                and cognitive_score > 80
                and all(score > 5 for score in interview_scores)
            ):
                filtered_candidates.append(candidate)

        return filtered_candidates