Netlogix: Hybrid Log Classification Framework
This project provides a robust, modular hybrid log classification system. It is designed to intelligently categorize log messages by utilizing a tiered approach that combines pattern-based rules, machine learning, and generative AI. This ensures high accuracy for common patterns and reliable fallbacks for complex or unknown data.

Classification Architecture
Our system processes each log message through a structured decision pipeline:

Regex Classification: The first layer for high-speed, deterministic classification of predictable and well-defined log patterns.

BERT-based Classification: For more complex log entries, the system utilizes Sentence Transformer embeddings combined with a trained Logistic Regression model. This layer is ideal for patterns that require semantic understanding and have historical training data.

LLM-based Fallback: For logs that cannot be classified by the first two methods, the system leverages a Large Language Model (via the Groq API) to perform context-aware classification. This ensures that even unique or previously unseen logs are handled effectively.

Project Structure
models/: Stores the serialized .joblib model files used for the BERT-based classification layer.

resources/: Houses supporting files, including sample datasets, CSV outputs, and documentation assets.

training/: Contains the Jupyter notebooks and scripts used to train and evaluate the machine learning components.

Root Directory: Contains the core logic, including the FastAPI server (server.py), modular processing scripts (processor_llm.py, bert_model_processor.py), and environment configurations.

Setup & Deployment
To run this project on your local machine, ensure you have Python installed, then follow these steps:

Environment Setup: Create and activate a virtual environment to manage your dependencies.

Install Requirements: Install the necessary libraries:
pip install -r requirements.txt

Configure API Keys: Create a .env file in the root directory and add your GROQ_API_KEY to enable the LLM classification layer. Ensure your .env file is included in your .gitignore to keep your credentials secure.

Launch the Server: Start the API server:
python server.py

Access the API:

Main endpoint: http://127.0.0.1:8000/

Interactive API docs: http://127.0.0.1:8000/docs

Usage
The system is designed to accept CSV uploads containing source and log_message columns. The API will process the logs through the hybrid framework and return a new CSV file containing the original data with an appended target_label column.
