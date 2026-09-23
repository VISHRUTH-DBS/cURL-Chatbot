# SSL Setup

If the Groq API shows an `SSL: CERTIFICATE_VERIFY_FAILED` error, set the SSL certificate bundle before running the Streamlit application. Make sure `groq-ca-bundle.pem` is present in the project directory. These environment variables apply only to the current PowerShell session.

```powershell
$env:SSL_CERT_FILE = "$PWD\groq-ca-bundle.pem"
$env:REQUESTS_CA_BUNDLE = "$PWD\groq-ca-bundle.pem"
python -c "import httpx; print(httpx.get('https://api.groq.com', timeout=10).status_code)"
python -m streamlit run app.py
```
