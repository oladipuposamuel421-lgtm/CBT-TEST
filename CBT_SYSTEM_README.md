# Computer-Based Test (CBT) Past Question System

## Overview
This is a comprehensive Computer-Based Test (CBT) system designed to simulate real examination conditions using past questions. The system reads questions from a JSON file and provides an interactive testing experience for students preparing for exams.

## Features
- Interactive question presentation with multiple-choice options
- Two test modes: Full test (all questions) or Randomized test (customizable number of questions)
- Real-time scoring and feedback
- Performance analysis with detailed review
- Time tracking during the test
- Automatic grading with percentage calculation
- User-friendly interface with clear instructions

## File Structure
- `cbt_past_question.json` - Contains the English Language Test questions and answers
- `cbt_test_system.py` - Main Python program implementing the CBT system
- `CBT_SYSTEM_README.md` - This documentation file

## How to Use

### Prerequisites
- Python 3.x installed on your system

### Running the Program
1. Make sure both `cbt_past_question.json` and `cbt_test_system.py` are in the same directory
2. Open your terminal/command prompt and navigate to the directory containing the files
3. Run the following command:
   ```
   python cbt_test_system.py
   ```

### Test Modes
1. **Full Test Mode**: Presents all 60 questions from the dataset
2. **Randomized Test Mode**: Allows you to select how many questions you want (randomly selected from the full set)

### Navigation During Test
- Answer questions by typing A, B, C, or D
- Type 'exit' at any time to quit the test early
- Press Enter to submit your answer

## Sample Data Structure
The JSON file contains:
- `metadata`: Information about the exam title and total number of questions
- `questions`: Array of question objects with:
  - `passage_id`: Unique identifier for the passage
  - `number`: Question number
  - `question`: The actual question text
  - `options`: Array of four possible answers (A, B, C, D)
  - `correct_answer`: The correct option (A, B, C, or D)

## Example Question Format
```json
{
  "passage_id": "1",
  "number": 1,
  "question": "What point of view is the Geography master fond of advancing?",
  "options": [
    "A. Africans are infested with all kinds of problems",
    "B. Only white men are free from deadly diseases",
    "C. The Almighty God is punishing Africans for sins they committed long ago.",
    "D. God did not curse white people."
  ],
  "correct_answer": "C"
}
```

## Results Analysis
After completing the test, you'll receive:
- Total questions attempted
- Number of correct and incorrect answers
- Percentage score
- Letter grade (A-F)
- Time taken to complete the test
- Detailed review showing your answers vs correct answers

## Customization
To use your own questions:
1. Modify the `cbt_past_question.json` file with your questions
2. Ensure the structure matches the expected format
3. Update the metadata accordingly

## Error Handling
The system includes error handling for:
- Missing JSON file
- Invalid JSON format
- Invalid user inputs during the test

## Educational Benefits
- Practice with authentic past questions
- Familiarity with computer-based testing format
- Immediate feedback on answers
- Time management practice
- Self-assessment capabilities

## License
This project is created for educational purposes and can be freely used for learning and practice.