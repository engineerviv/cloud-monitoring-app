import psutil
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    # Retrieve CPU and memory metrics
    cpu_percent = psutil.cpu_percent()
    mem_percent = psutil.virtual_memory().percent
    
    # Initialize the message variable
    message = None

    # Check if CPU or memory utilization is above 80%
    if cpu_percent > 80 or mem_percent > 80:
        message = "High CPU or Memory Usage Detected - Consider Scaling Up!"

    # Render the "index.html" template with metrics and message
    return render_template("index.html", cpu_metric=cpu_percent, mem_metric=mem_percent, message=message)

if __name__ == '__main__':
    # Run the Flask app with debugging enabled and make it accessible from any IP
    app.run(debug=True, host='0.0.0.0')
