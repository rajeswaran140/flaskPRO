from datetime import datetime

import logging

app = Flask(__name__)

@app.route('/')
def index():
    # Get the current date and time
    current_date = datetime.now()

    # Get the timezone information
    timezone = current_date.astimezone().tzinfo

    # Create the response string
    response = 'Current date and time: ' + str(current_date) + '<br>' + 'Timezone: ' + str(timezone)

    return response

if __name__ == '__main__':
    app.run(debug=True)
DEBUG:root:This is a debug message
INFO:root:This is an info message
WARNING:root:This is a warning message
ERROR:root:This is an error message
CRITICAL:root:This is a critical message
