from flask import render_template, request, redirect, url_for, flash, jsonify, json, session
from app import app
import http.server
import socketserver
import google.generativeai as genai
import os

# Set Google API Key
os.environ['GOOGLE_API_KEY'] = "AIzaSyAgaIHfGlas-QilDiOQtr1p9eY0usq2huI"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Simple in-memory user storage
users = {}

java_questions = [
    "What is Java's feature for type-safe data manipulation using collections?",
    "Which feature allows handling multiple exceptions in a single block?",
    "What is the result of the code involving conditional (ternary) operator?",
    "Explain inheritance in object-oriented programming.",
    "What is a Python decorator and how is it used?",
    "Explain the role of abstraction in object-oriented programming.",
    "What is the difference between a process and a thread?",
    "How does memory management work in Python?",
    "What is a database index and why is it used?",
    "Explain the difference between SQL and NoSQL databases.",
    "What is an API and how is it different from a Web Service?",
    "Explain the difference between TCP and UDP protocols.",
    "What is REST and how does it differ from SOAP?",
    "What are the key principles of Agile methodology?",
    "What is the purpose of unit testing in software development?",
]
dotnet_questions =  [
    
        "Which of the following .NET types is used to represent a single-precision floating-point number?",
        "What will be the output of the following C# code using StringBuilder?",
        "Which of the following is NOT a reference type in C#?",
        "What is the difference between ref and out parameters in C#?",
        "Which .NET class is used to work with XML data in memory?",
        "What does the async keyword do in C#?",
        "In C#, what is the primary use of the delegate keyword?",
        "What is the main purpose of the LINQ feature in .NET?",
        "Which of the following methods is used to sort an array in C#?",
        "What will be the result of the following C# code involving foreach?",
        "Which of the following C# data types can store any type of value?",
        "Which C# keyword is used to explicitly implement an interface method?",
        "What will be the result of the following code using Task.Run in C#?",
        "What is the use of the IDisposable interface in C#?",
        "Which of the following collections does NOT allow duplicates in .NET?"

    ]
data_engineering_questions = [

        "In Python, which library is most commonly used for numerical computations?",
        "What will be the output of the following Python code using pandas?\n\npython\nimport pandas as pd\ndf = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})\ndf['C'] = df['A'] + df['B']\nprint(df)\n",
        "Which Python library is used for data visualization?",
        "What is the purpose of the GROUP BY clause in SQL?",
        "What will be the result of the following SQL query?\n\nsql\nSELECT COUNT(*)\nFROM orders\nWHERE order_date > '2023-01-01';\n",
        "Which of the following is a valid method to handle missing data in pandas?",
        "What is the main purpose of a data pipeline in data engineering?",
        "Which SQL function is used to compute the average value of a numeric column?",
        "What will be the output of the following Python code using itertools?\n\npython\nimport itertools\nresult = list(itertools.permutations([1, 2, 3]))\nprint(len(result))\n",
        "Which of the following is a common data format used for big data processing?",
        "What is the main advantage of using Apache Spark over Hadoop MapReduce?",
        "Which of the following methods is used to handle categorical data in machine learning?",
        "What will be the result of the following Python code using pandas?\n\npython\nimport pandas as pd\ndf = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})\ndf = df.set_index('A')\nprint(df)\n",
        "Which SQL clause is used to filter records after grouping?",
        "What is the result of the following Python code using pandas and groupby?\n\npython\nimport pandas as pd\ndf = pd.DataFrame({'A': ['X', 'X', 'Y', 'Y'], 'B': [1, 2, 3, 4]})\nresult = df.groupby('A').sum()\nprint(result)\n",
        
]


from flask import render_template, request, redirect, url_for, flash, jsonify, json, session
from app import app, db  # Import Firestore client (db) from app
import google.generativeai as genai
import os

from firebase_admin import firestore

# Set Google API Key
os.environ['GOOGLE_API_KEY'] = "AIzaSyAgaIHfGlas-QilDiOQtr1p9eY0usq2huI"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Firebase user collection reference
users_ref = db.collection('users')

# Java, .NET, Data Engineering questions (omitted for brevity)


@app.route('/', methods=['GET', 'POST'])
def login_register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if 'login' in request.form:
            # Firebase login logic
            user_doc = users_ref.document(username).get()
            if user_doc.exists and user_doc.to_dict()['password'] == password:
                return redirect(url_for('profile', username=username))
            else:
                flash('Invalid credentials. Please try again.')
        elif 'register' in request.form:
            # Check if user exists in Firebase
            if users_ref.document(username).get().exists:
                flash('Username already exists. Please choose another one.')
            else:
                # Save user in Firestore
                users_ref.document(username).set({
                    'password': password,
                    'email': '',
                    'degree': '',
                    'specialization': '',
                    'phone': '',
                    'certifications': '',
                    'internship': '',
                    'courses': '',
                    'linkedin': '',
                    'github': '',
                    'languages': ''
                })
                return redirect(url_for('register', username=username))
    return render_template('login.html')


@app.route('/register/<username>', methods=['GET', 'POST'])
def register(username):
    if request.method == 'POST':
        # Update user data in Firestore
        users_ref.document(username).update({
            'email': request.form['email'],
            'degree': request.form['degree'],
            'specialization': request.form['specialization'],
            'phone': request.form['phone'],
            'certifications': request.form['certifications'],
            'internship': request.form['internship'],
            'courses': request.form['courses'],
            'linkedin': request.form['linkedin'],
            'github': request.form['github'],
            'languages': request.form['languages']
        })
        session['username'] = username
        return redirect(url_for('profile', username=username))
    return render_template('register.html')


@app.route('/profile/<username>', methods=['GET'])
def profile(username):
    # Fetch user from Firestore
    user_doc = users_ref.document(username).get()
    if not user_doc.exists:
        flash('User not found.')
        return redirect(url_for('login_register'))
    
    user_data = user_doc.to_dict()
    return render_template('profile.html', username=username, **user_data)


# Remaining routes (exam-details, start-exam, save-answers, recommendation) remain the same.


@app.route('/exam-details', methods=['POST'])
def exam_details():
    course = request.form['course']
    session['course'] = course
    exam_data = {
        'Java': {
            'duration': 15,
            'questions': 15,
            'summary': 'Java is a high-level, class-based, object-oriented programming language designed to have as few implementation dependencies as possible.'
        },
        '.NET': {
            'duration': 15,
            'questions': 15,
            'summary': '.NET is a free, cross-platform, open-source developer platform for building many different types of applications.'
        },
        'Data Engineering': {
            'duration': 15,
            'questions': 15,
            'summary': 'Data Engineering involves the collection, storage, processing, and analysis of data to help businesses make informed decisions.'
        }
    }

    if course in exam_data:
        return render_template('exam_details.html',
            course=course,
            summary=exam_data[course]['summary'],
            duration=exam_data[course]['duration'],
            questions=exam_data[course]['questions']
        )

@app.route('/start-exam/<course>', methods=['GET'])

def start_exam(course):
    
    if course == 'Java':
        return render_template('java_question.html')
    elif course == 'Data Engineering':
        return render_template('data_engineering.html')
    elif course == '.NET':
        return render_template('net_questions.html')
    else:
        flash('Invalid course selected.')
        return redirect(url_for('exam_details')) 
    
@app.route('/save-answers', methods=['POST'])
def save_answers():
    data = request.json
    answers = data.get('answers')
    course = session.get('course')

    return jsonify({'redirect': url_for('recommendation', course= course,answers=json.dumps(answers))})


def format_input(mcq_scores, mcq_questions):
    incorrect_questions = [q for i, q in enumerate(mcq_questions) if mcq_scores[i] == 0]
    num_wrong_answers = len(incorrect_questions)
    
    prompt = f"""
    Based on the following evaluation scores and questions, suggest topics for improvement.
    Scores: {', '.join([str(score) for score in mcq_scores])}
    Questions where the candidate answered incorrectly:
    {incorrect_questions}
    your recommended topics should be seperated with ","
    use numbers for each topics
    """
    return prompt

def get_recommendations(mcq_scores, mcq_questions):
    prompt = format_input(mcq_scores, mcq_questions)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(prompt)

    recommendations = response.text.replace('*', '').strip()  
    recommendations_list = [rec.strip() for rec in recommendations.split(',') if rec]

    return recommendations_list 

@app.route('/recommendation')
def recommendation():
    course = session.get('course')
    answers_str = request.args.get('answers')

    # Load user data from Firestore
    username = session.get('username')  # Get the username from the session
    user_doc = users_ref.document(username).get()
    user_data = user_doc.to_dict() if user_doc.exists else {}

    answers = json.loads(answers_str) if answers_str else []
    mcq_questions = []
    
    if course == 'Java':
        mcq_questions = java_questions
    elif course == '.NET':
        mcq_questions = dotnet_questions
    elif course == 'Data Engineering':
        mcq_questions = data_engineering_questions
  
    recommendations = get_recommendations(answers, mcq_questions)

    # Pass user data and recommendations to the template
    return render_template('recommendation.html', recommendations=recommendations, user_data=user_data)

if __name__ == 'main':
 app.run(debug=True)