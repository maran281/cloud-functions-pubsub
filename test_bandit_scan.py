import os
import subprocess
import hashlib

# Hardcoded password (Bandit issue: B105)
def connect_to_database():
    password = "SuperSecret123"  # Hardcoded secret
    print(f"Connecting to the database with password: {password}")

# Use of eval (Bandit issue: B307)
def evaluate_expression(user_input):
    result = eval(user_input)  # Dangerous: User-controlled input
    print(f"Result of evaluation: {result}")

# Use of subprocess with shell=True (Bandit issue: B602/B603)
def execute_command(command):
    subprocess.call(command, shell=True)  # Dangerous: Shell injection risk

# MD5 is a weak hash algorithm (Bandit issue: B303)
def hash_password(password):
    hashed = hashlib.md5(password.encode()).hexdigest()  # Insecure: MD5 is vulnerable
    print(f"MD5 hash of the password: {hashed}")

# Insecure file permissions (Bandit issue: B108)
def create_sensitive_file():
    with open("sensitive_data.txt", "w") as file:
        file.write("Sensitive information")
    os.chmod("sensitive_data.txt", 0o777)  # Too permissive

if __name__ == "__main__":
    connect_to_database()
    evaluate_expression("2 + 2")
    execute_command("ls -la")
    hash_password("example_password")
    create_sensitive_file()
