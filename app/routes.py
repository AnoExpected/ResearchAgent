from flask import render_template, request, jsonify
from werkzeug.utils import secure_filename
import os
from app import app
from agent_setup import setup_agent

# Setup the agent
papers = ["metagpt.pdf", "longlora.pdf", "selfrag.pdf"]
agent = setup_agent(papers)

# Define upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    query_text = request.form['query']
    response = agent.query(query_text)
    return jsonify({'response': str(response)})

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})
    
    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Add uploaded paper to papers list
        papers.append(filepath)
        
        # Update agent with new paper
        global agent
        agent = setup_agent(papers)

        return jsonify({'success': 'File uploaded successfully'})
    else:
        return jsonify({'error': 'File extension not allowed'})
