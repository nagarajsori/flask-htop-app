from flask import Flask
import subprocess
import os
import datetime
from pytz import timezone

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the system username
    username = os.getenv("USER") or os.getenv("LOGNAME") or os.getenv("USERNAME") or "Unknown"

    # Get current IST time using pytz
    ist = datetime.datetime.now(timezone("Asia/Kolkata")).strftime('%Y-%m-%d %H:%M:%S')

    # Run the 'top' command and capture output safely
    try:
        top_output = subprocess.getoutput("top -b -n 1")
    except Exception as e:
        top_output = f"Error retrieving top output: {e}"

    # Generate response
    response = f"""
    <pre>
    Name: Nagaraj Sori
    User: {username}
    Server Time (IST): {ist} IST

    TOP output:
    {top_output}
    </pre>
    """
    
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
