import subprocess
import smtplib
from email.mime.text import MIMEText

def check_process(host, process_name):
    """
    Checks if a given process is running on a remote host.

    Args:
        host: The hostname or IP address of the remote host.
        process_name: The name of the process to check.

    Returns:
        True if the process is running, False otherwise.
    """
    try:
        # Use SSH to execute a command on the remote host
        ssh_cmd = f"ssh {host} 'ps aux | grep -v grep | grep {process_name}'"
        output = subprocess.check_output(ssh_cmd, shell=True, text=True)
        if process_name in output:
            return True
        else:
            return False
    except Exception as e:
        print(f"Error checking {host}: {e}")
        return False

def send_email(report):
    """
    Sends an email with the report.

    Args:
        report: The report string.
    """
    sender_email = "your_email@example.com"
    receiver_email = "recipient_email@example.com"
    password = "your_email_password"

    message = MIMEText(report)
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = "Process Check Report"

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

if __name__ == "__main__":
    hosts = [  # Replace with your list of 100 hostnames/IPs
        "host1.example.com",
        "host2.example.com",
        # ...
    ]
    process_name = "your_process_name"  # Replace with the process name to check

    report = ""
    for host in hosts:
        if check_process(host, process_name):
            report += f"{host}: Process '{process_name}' is running.\n"
        else:
            report += f"{host}: Process '{process_name}' is not running.\n"

    send_email(report)