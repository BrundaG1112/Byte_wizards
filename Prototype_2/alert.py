import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Function to send email
def send_email(subject, body, to_email):
    from_email = "raghavendraamberkar07@gmail.com"
    from_password = "zfbe fotv lwjk izhw"  # Use the app-specific password here

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")

# Function to check pulse values and send an email if needed
def check_pulse_and_notify(csv_file_path, to_email):
    try:
        data = pd.read_csv(csv_file_path)
        if 'Pulse' not in data.columns:
            print("Pulse column not found in the CSV file")
            return

        high_pulse_entries = data[data['Pulse'] > 100]
        
        if not high_pulse_entries.empty:
            for index, row in high_pulse_entries.iterrows():
                subject = "High Pulse Alert"
                body = f"High pulse detected:\n\n{row.to_string()}"
                send_email(subject, body, to_email)
        else:
            print("No high pulse values found.")
    except Exception as e:
        print(f"Error reading the CSV file: {e}")

# Usage
csv_file_path = 'BPMX-1.csv'  # Replace with the path to your CSV file
to_email = 'raghavendraamberkar05@gmail.com'  # Replace with the recipient's email address

check_pulse_and_notify(csv_file_path, to_email)
