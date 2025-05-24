# Modular AI Testing Agent

An AI-powered, modular testing and analysis framework built with Python.  
Designed to help developers and QA teams automate API testing, data analysis, UI validation, and static security scanning — all in one tool.

## Features

- **API Testing**  
  Send HTTP requests to configured endpoints and validate responses.

- **Data Analysis**  
  Load CSV files and generate summaries using pandas.

- **UI Testing**  
  Use Selenium to validate the presence of UI elements on webpages.

- **Security Scanning**  
  Perform static code analysis with Bandit to catch Python security issues.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-testing-agent.git
cd ai-testing-agent
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

Make sure [ChromeDriver](https://sites.google.com/chromium.org/driver/) is in your system path for UI testing.

### 3. Run the Agent

```bash
python agent.py
```

You can configure which modules to run in `config.json`.

## Configuration (`config.json`)

```json
{
  "api_testing": {
    "endpoints": [
      {"url": "https://jsonplaceholder.typicode.com/posts", "method": "GET"}
    ]
  },
  "data_analysis": {
    "file_path": "sample_data.csv"
  },
  "ui_testing": {
    "url": "https://example.com",
    "elements": ["h1", "p"]
  },
  "security_analysis": {
    "target_path": "."
  }
}
```

## Demo

Check out the [video demo](https://youtu.be/HPaiJbjCC3g) showing the agent in action!

## Contributing

Pull requests and feature ideas are welcome!

## License

This project is licensed under the MIT License.

## Author

**Your Name**  
[LinkedIn](www.linkedin.com/in/uzair-siddiqui-13669aba)  
[GitHub](https://github.com/uzairde-max)
