# CBT Past Question Application

This is a simple web-based Computer-Based Testing (CBT) system that allows users to take practice exams using JSON-formatted past questions.

## Features

- Interactive exam interface with navigation controls
- Real-time progress tracking
- Answer submission and scoring
- Question review functionality
- Responsive design for various screen sizes

## Files Included

- `cbt_app.html`: Main application file containing the HTML, CSS, and JavaScript for the CBT system
- `cbt_past_question.json`: Sample English Language test questions (60 questions)

## How to Use

1. Open `cbt_app.html` in a web browser
2. Click "Start Exam" to begin the test
3. Navigate through questions using Previous/Next buttons
4. Select your answers by clicking on the radio buttons
5. Click "Submit Exam" when you've completed all questions
6. View your results and review your answers

## Technical Details

- The application fetches questions dynamically from the JSON file
- User answers are stored in memory during the session
- Results include score calculation and percentage
- Review section shows which answers were correct or incorrect

## Customization

To use your own questions:

1. Modify the `cbt_past_question.json` file with your own questions in the same format
2. Or create a new JSON file with the same structure and update the filename in the JavaScript code

The JSON structure includes:
- `metadata`: Contains exam title and total number of questions
- `questions`: Array of question objects with:
  - `passage_id`: Unique identifier for the passage
  - `number`: Question number
  - `question`: The actual question text
  - `options`: Array of possible answers (A, B, C, D...)
  - `correct_answer`: The letter corresponding to the correct answer

## Browser Compatibility

The application works with all modern browsers that support:
- Fetch API
- ES6 JavaScript features
- Flexbox CSS