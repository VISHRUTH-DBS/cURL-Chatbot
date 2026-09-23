# cURL AI Chatbot

An AI-powered chatbot that understands a user's request and finds the most relevant website from a collection of cURL commands stored in `curl.txt`.

Instead of requiring the user to know the exact website, they can describe what they are looking for in natural language.

For example:

> I want to watch videos

The chatbot can identify YouTube as the relevant website and return its cURL command and URL.

## Features

* Natural-language website search
* AI-powered semantic matching using Groq
* cURL commands stored in `curl.txt`
* Supports websites across multiple categories
* Displays the matching cURL command
* Provides a clickable link to the selected website
* Maintains previous requests and results during the current session
* Case-insensitive natural-language understanding
* Easy to add new websites by editing `curl.txt`

## Example Queries

You can ask questions such as:

```text
I want to watch videos
```

```text
I need a website to learn Python
```

```text
I want to solve coding problems
```

```text
I need free images
```

```text
I want information about movies
```

```text
I want cricket information
```

```text
I want to find open source projects
```

```text
I want to buy something online
```

```text
I want to compare flights
```

The chatbot analyzes the request and selects the most relevant website from `curl.txt`.

## Project Structure

```text
cURL-Chatbot/
│
├── app.py
├── curl.txt
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## Technologies Used

* Python
* Streamlit
* LangChain
* Groq
* Python Dotenv

## Requirements

Make sure the following are installed:

* Python 3.10 or newer
* pip
* Groq API key

## Installation

Clone the repository:

```bash
git clone https://github.com/VISHRUTH-DBS/cURL-Chatbot
cd "Chatbot Ver2"
```

Create a virtual environment:

```powershell
python -m venv myenv
```

Activate it:

```powershell
.\myenv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

## Environment Variables

Create a `.env` file in the project directory:

```text
GROQ_API_KEY=your_groq_api_key_here
```

Do not commit the `.env` file to GitHub.

The repository contains `.env.example` as a template:

```text
GROQ_API_KEY=your_groq_api_key_here
```

## cURL Database

The website and cURL information is stored in:

```text
curl.txt
```

Each website is stored as a separate cURL command:

```bash
curl "https://www.youtube.com"

curl "https://www.github.com"

curl "https://www.coursera.org"
```

To add another website, simply add another cURL command to `curl.txt`.

## Running the Application

Start Streamlit:

```powershell
python -m streamlit run app.py
```

The application will normally be available at:

```text
http://localhost:8501
```

Open the address in your browser.

## How It Works

```text
User
  │
  │ Natural-language request
  ▼
Streamlit Chat Interface
  │
  ▼
Groq LLM
  │
  │ Understands user's request
  ▼
cURL Collection
  │
  │ Selects the most relevant website
  ▼
Matching cURL
  │
  ├── cURL command
  │
  └── Website URL
  ▼
User
```

## Example

User:

```text
I want to learn programming online
```

The AI analyzes the available websites in `curl.txt` and selects a relevant learning platform.

The chatbot then displays:

```text
Matching API

curl "https://www.codecademy.com"
```

and provides a link to open the website.

## API / Website Categories

The current `curl.txt` contains websites covering categories such as:

* Search engines
* Social media
* Video platforms
* Online learning
* Programming
* Developer resources
* Open-source software
* Images
* Design
* Companies
* Shopping
* Sports
* Cricket
* Football
* Formula 1
* Movies
* Entertainment
* Books
* Travel
* Hotels
* Flights
* News
* Technology

## Session History

The chatbot keeps previous questions and matching results in the current Streamlit session.

For example:

```text
User:
I want to watch videos

Assistant:
YouTube
```

Then:

```text
User:
I want to solve coding problems

Assistant:
LeetCode
```

The previous YouTube result remains visible in the conversation.

Session history is reset when the Streamlit session is restarted or reset.

## SSL Certificate Setup

If your network uses corporate SSL inspection and Groq returns:

```text
CERTIFICATE_VERIFY_FAILED
```

make sure `groq-ca-bundle.pem` is present in the project directory.

Then run:

```powershell
$env:SSL_CERT_FILE = "$PWD\groq-ca-bundle.pem"
$env:REQUESTS_CA_BUNDLE = "$PWD\groq-ca-bundle.pem"
python -m streamlit run app.py
```

The environment variables apply only to the current PowerShell session.

The certificate file should not be committed to GitHub.

## Security

Never commit secrets or private certificates.

The following files should remain local:

```text
.env
groq-ca-bundle.pem
zscaler.cer
zscaler.pem
myenv/
```

These files should be included in `.gitignore`.

## Future Improvements

Possible future improvements include:

* Support for complete multi-line cURL commands
* Website category filtering
* Multiple matching results
* Website descriptions
* Search history
* Favorite websites
* Automatic cURL classification
* Adding websites through the UI
* Website availability checking
* Better ranking of matching websites
* Support for company-specific cURL collections
* Separate collections for different projects or teams

## License

This project is intended for educational and development purposes.
