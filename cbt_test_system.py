import json
import random
from datetime import datetime

class CBTTestSystem:
    def __init__(self, json_file_path):
        """
        Initialize the CBT Test System with questions from JSON file
        """
        with open(json_file_path, 'r', encoding='utf-8') as file:
            self.data = json.load(file)
        
        self.questions = self.data['questions']
        self.exam_title = self.data['metadata']['exam_title']
        self.total_questions = self.data['metadata']['total_questions']
        self.user_answers = {}
        self.score = 0
        
    def display_welcome_message(self):
        """
        Display welcome message and instructions
        """
        print("="*60)
        print(f"           WELCOME TO THE {self.exam_title.upper()}")
        print("="*60)
        print(f"Total Questions: {self.total_questions}")
        print("Instructions:")
        print("- Answer all questions by entering the letter of your choice (A, B, C, or D)")
        print("- Type 'exit' at any time to quit the test")
        print("- You will receive your score at the end")
        print("="*60)
        
    def present_question(self, question_data, question_number=None):
        """
        Present a single question to the user
        """
        if question_number:
            print(f"\nQuestion {question_number}:")
        else:
            print(f"\nQuestion {question_data['number']}:")
            
        print(question_data['question'])
        print()
        
        # Print options
        for option in question_data['options']:
            print(option)
        
        # Get user's answer
        while True:
            user_input = input("\nEnter your answer (A, B, C, D) or 'exit' to quit: ").strip().upper()
            
            if user_input == 'EXIT':
                return 'EXIT'
            elif user_input in ['A', 'B', 'C', 'D']:
                return user_input
            else:
                print("Invalid input. Please enter A, B, C, D or 'exit' to quit.")
    
    def run_full_test(self):
        """
        Run the complete test with all questions
        """
        self.display_welcome_message()
        input("\nPress Enter to start the test...")
        
        start_time = datetime.now()
        
        # Loop through all questions
        for i, question in enumerate(self.questions, 1):
            result = self.present_question(question, i)
            
            if result == 'EXIT':
                print("\nTest ended early by user.")
                break
            
            # Store the user's answer
            self.user_answers[question['number']] = {
                'user_answer': result,
                'correct_answer': question['correct_answer'],
                'is_correct': result == question['correct_answer']
            }
        
        end_time = datetime.now()
        self.calculate_score()
        self.display_results(start_time, end_time)
    
    def run_randomized_test(self, num_questions=20):
        """
        Run a randomized test with specified number of questions
        """
        if num_questions > len(self.questions):
            num_questions = len(self.questions)
        
        selected_questions = random.sample(self.questions, num_questions)
        
        self.display_welcome_message()
        print(f"This test contains {num_questions} randomly selected questions.")
        input("\nPress Enter to start the test...")
        
        start_time = datetime.now()
        
        for i, question in enumerate(selected_questions, 1):
            result = self.present_question(question, i)
            
            if result == 'EXIT':
                print("\nTest ended early by user.")
                break
            
            # Store the user's answer
            self.user_answers[question['number']] = {
                'user_answer': result,
                'correct_answer': question['correct_answer'],
                'is_correct': result == question['correct_answer']
            }
        
        end_time = datetime.now()
        self.calculate_score()
        self.display_results(start_time, end_time, randomized=True, total_asked=num_questions)
    
    def calculate_score(self):
        """
        Calculate the final score
        """
        correct_count = sum(1 for item in self.user_answers.values() if item['is_correct'])
        total_attempted = len(self.user_answers)
        self.score = correct_count
        
        print(f"\nScore calculated: {correct_count}/{total_attempted}")
    
    def display_results(self, start_time, end_time, randomized=False, total_asked=None):
        """
        Display the final results
        """
        print("\n" + "="*60)
        print("                        RESULTS")
        print("="*60)
        
        if randomized and total_asked:
            print(f"Questions Attempted: {len(self.user_answers)} out of {total_asked}")
        else:
            print(f"Questions Attempted: {len(self.user_answers)} out of {self.total_questions}")
        
        print(f"Correct Answers: {self.score}")
        print(f"Wrong Answers: {len(self.user_answers) - self.score}")
        
        if len(self.user_answers) > 0:
            percentage = (self.score / len(self.user_answers)) * 100
            print(f"Percentage Score: {percentage:.2f}%")
        
        duration = end_time - start_time
        print(f"Time Taken: {duration}")
        
        # Show performance grade
        if len(self.user_answers) > 0:
            percentage = (self.score / len(self.user_answers)) * 100
            if percentage >= 80:
                grade = "A - Excellent!"
            elif percentage >= 70:
                grade = "B - Very Good!"
            elif percentage >= 60:
                grade = "C - Good!"
            elif percentage >= 50:
                grade = "D - Fair!"
            else:
                grade = "F - Needs Improvement"
            
            print(f"Grade: {grade}")
        
        print("\nDetailed Review:")
        print("-" * 60)
        
        for q_num, answer_info in sorted(self.user_answers.items()):
            status = "✓ CORRECT" if answer_info['is_correct'] else "✗ WRONG"
            print(f"Q{q_num}: Your answer: {answer_info['user_answer']} | Correct: {answer_info['correct_answer']} | {status}")
        
        print("\nThank you for taking the test!")
        print("="*60)


def main():
    """
    Main function to run the CBT system
    """
    try:
        cbt_system = CBTTestSystem('cbt_past_question.json')
        
        print("Choose test mode:")
        print("1. Full test (all questions)")
        print("2. Randomized test (select number of questions)")
        
        while True:
            choice = input("Enter your choice (1 or 2): ").strip()
            
            if choice == '1':
                cbt_system.run_full_test()
                break
            elif choice == '2':
                try:
                    num_q = int(input("How many questions would you like? "))
                    cbt_system.run_randomized_test(num_questions=num_q)
                    break
                except ValueError:
                    print("Please enter a valid number.")
            else:
                print("Invalid choice. Please enter 1 or 2.")
                
    except FileNotFoundError:
        print("Error: cbt_past_question.json file not found!")
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in the file!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()