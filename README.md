# Research Agent

Research Agent is a web application that allows users to upload research papers and interact with an AI agent to ask questions related to the content of those papers. The AI agent utilizes advanced natural language processing techniques to understand and answer user queries effectively.

## Features

- Upload research papers in PDF format.
- Interact with an AI agent to ask questions about the uploaded papers.
- View responses provided by the AI agent in real-time.

## Technologies Used

- Python
- Flask
- OpenAI GPT-3.5-turbo
- LlamaIndex
- HTML/CSS/JavaScript

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/research-agent.git
    ```

2. Navigate to the project directory:

    ```bash
    cd research-agent
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up the OpenAI API key:

    - Obtain an API key from OpenAI.
    - Set the API key as an environment variable named `OPENAI_API_KEY`.

5. Run the Flask app:

    ```bash
    python main.py
    ```

6. Access the web application:

    Open a web browser and go to `http://localhost:5000`.

## Usage

1. Upload Research Papers:
    - Click on the "Upload Research Paper" button.
    - Choose a PDF file containing the research paper.
    - Click the "Upload" button to upload the file.

2. Ask Questions:
    - Use the "Ask a Question" form to enter your query.
    - Click the "Submit" button to get a response from the AI agent.
    - The response will be displayed below the form.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
