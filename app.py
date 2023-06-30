from flask import Flask, render_template, send_file, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    skills = [
        'Python',
        'Flask',
        'Google Cloud app deployment',
        'Vertex AI',
        'Kubeflow',
        'MLFlow Pipelines'
    ]

    interests = [
        'Machine Learning',
        'Financial Crime Risk Reduction',
        'Anti Money-Laundering'
        'Deep Learning',
        'Natural Language Processing',
        'MLOps Deployment'
    ]

    education = [
        {
            'degree': 'Master of Science in Statistics and Data Science',
            'university': 'Catholic University of Leuven, Belgium',
            'year': '2016-2018'
        },
        {
            'degree': 'Bachelor of Engineering in Metallurgical and Materials Engineering',
            'university': 'National Institute of Technology Warangal, India ',
            'year': '2010-2014'
        }
    ]

    return render_template('index.html', skills=skills, interests=interests, education=education)

@app.route('/view-pdf', methods=['POST'])
def view_pdf():
    # Assuming your PDF file is named "cv.pdf" in the same directory
    return send_from_directory('.', 'Bharat Ram Ammu CV Complidata latest.pdf', as_attachment=False)

if __name__ == '__main__':
    app.run()
