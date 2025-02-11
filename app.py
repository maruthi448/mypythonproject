import os
import git
import yaml
import base64
#from cryptography.fernet import Fernet
'''
# Load encryption key
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()


# Decrypt the token
def decrypt_token(encrypted_token):
    key = load_key()
    cipher = Fernet(key)
    return cipher.decrypt(encrypted_token.encode()).decode()

# Load Git credentials from config.yml
with open("config.yml", "r") as file:
    config = yaml.safe_load(file)

GITHUB_USERNAME = config["github_username"]
ENCRYPTED_TOKEN = config["encrypted_token"]
GITHUB_TOKEN = decrypt_token(ENCRYPTED_TOKEN)
'''

GITHUB_USERNAME = os.environ["GIT_USERNAME"]
GITHUB_TOK = os.environ["GIT_TOKEN"]

GITHUB_TOKEN = base64.b64decode(GITHUB_TOK)

if isinstance(GITHUB_TOKEN, bytes):
    GITHUB_TOKEN = GITHUB_TOKEN.decode("utf-8")


print("the value of token is:", GITHUB_TOKEN)
# Define Repository and File Paths
TARGET_REPO_URL = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/maruthi448/sampleproj.git"

print (" the target repo is:", TARGET_REPO_URL)
LOCAL_CLONE_DIR = "/Users/maruthikumark/Training/Python_practice"
CONFIG_FILE_NAME = "template.yml"
DOCKER_FILE_NAME = "Dockerfile"
COMMIT_MESSAGE = "Added template.yml"

# Create YAML Configuration File
yaml_data = {
    "project": "Secure Git Project",
    "version": "1.0",
    "settings": {
        "debug": True,
        "log_level": "INFO"
    }
}

os.makedirs(LOCAL_CLONE_DIR, exist_ok=True)
config_file_path = os.path.join(LOCAL_CLONE_DIR, CONFIG_FILE_NAME)

with open(config_file_path, "w") as file:
    yaml.dump(yaml_data, file, default_flow_style=False)

print("✅ YAML file created.")

# Create Dockerfile
dockerfile_content = """\
FROM python:3.9

WORKDIR /app
COPY template.yml /app/

CMD ["cat", "/app/template.yml"]
"""

dockerfile_path = os.path.join(LOCAL_CLONE_DIR, DOCKER_FILE_NAME)

with open(dockerfile_path, "w") as file:
    file.write(dockerfile_content)

print("✅ Dockerfile created.")

# Clone Repository
repo = git.Repo.clone_from(TARGET_REPO_URL, LOCAL_CLONE_DIR)
print("✅ Repository cloned successfully.")

# Commit and Push Changes
repo.index.add([config_file_path, dockerfile_path])
repo.index.commit(COMMIT_MESSAGE)
origin = repo.remote(name="origin")
origin.push()

print(f"✅ {CONFIG_FILE_NAME} and {DOCKER_FILE_NAME} pushed securely to {TARGET_REPO_URL}")




'''
import os
import yaml
import git 
#from cryptography.fernet import Fernet

# Configuration
YML_FILE_NAME = "config.yml"
TARGET_REPO_URL = "https://id:{pwd}@github.com/maruthi448/sampleproj.git"  # Use SSH or HTTPS
LOCAL_CLONE_DIR = "/tmp/git_repo"  # Temporary directory to clone repo
COMMIT_MESSAGE = "Added config.yml via automation"

# YAML Content
yaml_data = {
    "name": "MyProject",
    "version": "1.0.0",
    "settings": {
        "debug": True,
        "logging_level": "INFO"
    }
}

# Step 1: Create a YAML File
os.makedirs(LOCAL_CLONE_DIR, exist_ok=True)
yml_file_path = os.path.join(LOCAL_CLONE_DIR, YML_FILE_NAME)

with open(yml_file_path, "w") as file:
    yaml.dump(yaml_data, file, default_flow_style=False)

print(f" YAML file created at {yml_file_path}")

# Step 2: Clone the Target Repository
if os.path.exists(LOCAL_CLONE_DIR):
    repo = git.Repo.clone_from(TARGET_REPO_URL, LOCAL_CLONE_DIR)
    print("Repository cloned successfully.")

# Step 3: Commit and Push Changes
repo.index.add([yml_file_path])
repo.index.commit(COMMIT_MESSAGE)
origin = repo.remote(name="origin")
origin.push()

print(f" {YML_FILE_NAME} pushed to {TARGET_REPO_URL}")
'''
