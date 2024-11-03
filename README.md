# NLP Text Summarization Project

This project uses Google's PEGASUS model for abstractive text summarization, providing an easy-to-use REST API built with FastAPI. It enables users to quickly generate summaries for large texts, suitable for integration into various applications.

## Project Overview

- **Goal**: Develop a scalable text summarization API to provide quick, concise summaries using PEGASUS.
- **API Access**: Built with FastAPI for seamless integration and deployment.

## Project Structure

```text
├── config/           # Configuration files for model and API settings
├── research/         # Jupyter notebooks for experimentation and analysis
├── src/              # Core summarization code
├── app.py            # FastAPI server to expose REST API
├── main.py           # Script for running the summarization workflow
└── requirements.txt  # Project dependencies
```
## Getting Started

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Eidos110/NLP_Text_Summarize_Project.git
2. **Install Dependencies**:
   ```sh
   pip install -r requirements.txt
3. **Run the FastAPI Server**:
   ```sh
   uvicorn app:app --reload

## Key Features

- **Text Summarization Endpoint**: Input text and receive a summary via the REST API.
- **User-Friendly Interface**: Use Swagger UI to interactively test the API endpoints.

## Use Cases

- **Summarize Long Content**: Ideal for extracting concise information from news articles, blogs, and reports.
- **Scalable Integration**: Easily integrate summarization capabilities into other applications or services.

## Tools & Technologies

- **Languages**: Python
- **Libraries**: TensorFlow, FastAPI
- **Model**: PEGASUS (Google’s state-of-the-art summarization model)

## Future Plans

- **Enhanced Model Options**: Add support for additional NLP models for performance benchmarking.
- **File Input Capability**: Allow users to upload and summarize documents like PDFs.
- **Cloud Hosting**: Deploy the API on a cloud platform (AWS, Azure, or Heroku) for broader accessibility.

## License

Licensed under the [MIT License](LICENSE).



