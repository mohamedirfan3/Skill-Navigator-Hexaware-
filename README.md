# Skill-Navigator-Hexaware-# User Login, Profile, Exam Details, Recommendation, and Report Generation System

This project is a web application built using **Flask** that allows users to register, log in, take exams, receive personalized recommendations, and generate performance reports. It utilizes **SQLAlchemy** for database management and **Google Generative AI** for generating recommendations based on exam performance.

## Features

### 1. User Registration and Login
- **Login**: Users can log in with their username and password.
- **Registration**: New users can register by providing basic details such as username, password, and other profile information (e.g., degree, specialization, phone, etc.).
- **Profile Page**: After login, users can view and update their profile information.

### 2. Exam Details and Question Selection
- **Exam Courses**: Users can choose from multiple courses, such as:
  - Java
  - .NET
  - Data Engineering
- **Exam Summary**: Each course includes details such as exam duration, number of questions, and a brief summary of the topic.
- **Questions**: The system presents users with multiple-choice questions (MCQs) from the selected course.

### 3. Answer Submission and Recommendation
- **Answer Submission**: Users submit their answers after completing the exam.
- **Answer Evaluation**: The system calculates the correct, incorrect, and unanswered questions.
- **Recommendation Generation**: Based on the user's performance, the system utilizes **Google Generative AI** to provide personalized learning recommendations, suggesting topics for improvement.

### 4. Report Generation
- **Performance Report**: After submitting the exam, users are provided with a report that shows:
  - The number of correct answers
  - The number of incorrect answers
  - The number of questions not attended
- **Recommendations**: Along with the performance report, users receive topic recommendations based on the questions they answered incorrectly.

## Technologies Used
- **Flask**: Web framework for developing the application.
- **SQLAlchemy**: ORM for managing user data and exam results.
- **Google Generative AI**: For generating personalized recommendations.
- **HTML/CSS**: Frontend structure and design.
- **Firebase**: (Optional) For data storage and user authentication, though SQLAlchemy is used primarily.

## Project Structure
- **app.py**: The main Flask application file that routes between login, registration, exam details, and recommendation pages.
- **templates/**: Contains all HTML templates for pages such as `login.html`, `registration.html`, `profile.html`, `examdetails.html`, `javaquestion.html`, `recommendation.html`.
- **models.py**: SQLAlchemy models for managing user data and exam answers.
- **static/**: Directory for CSS and JavaScript files.

## Future Enhancements
- **Report Download**: Add functionality to download performance reports as PDF.
- **Improved Recommendations**: Enhance the recommendation system by integrating more advanced AI models.
- **Multiple Languages**: Add support for different programming languages in the exams.
- **Time Tracking**: Track the time spent on each question for further analysis.

## How to Run the Project
1. **Install Dependencies**: Install required packages using `pip install -r requirements.txt`.
2. **Set Up Database**: Configure the database using SQLAlchemy.
3. **Run the Application**: Start the Flask server using `flask run`.
4. **Access the Application**: Open a web browser and go to `http://localhost:5000/`.

## Acknowledgements
This project was developed as a learning and exam platform with recommendation features for users to improve their skills in various programming domains.
