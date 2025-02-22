from fastapi import FastAPI
import os
import  git
import yaml
import base64
import shutil

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

app = FastAPI()

@app.get("/home")
def home():
    print('Welcome to our python dashboard')
    return{'Welcome to our python dashboard'}


@app.get("/gitpushtotargeturl")
def gitpushtotargeturl():
    try:
        GITHUB_USERNAME = os.environ["GIT_USERNAME"]
        GITHUB_TOK = os.environ["GIT_TOKEN"]
        GITHUB_TOKEN = base64.b64decode(GITHUB_TOK)
        if isinstance(GITHUB_TOKEN, bytes):
            GITHUB_TOKEN = GITHUB_TOKEN.decode("utf-8")

        #print("the value of token is:", GITHUB_TOKEN)
        # Define Repository and File Paths
        TARGET_REPO_URL = f"https://{GITHUB_USERNAME}:{GITHUB_TOKEN}@github.com/maruthi448/sampleproj.git"

        print (" the target repo is:", TARGET_REPO_URL)
        LOCAL_CLONE_DIR = "/Users/maruthikumark/Training/Python_practice/targetgitrepo"
        CONFIG_FILE_NAME = "template.yml"
        Destina_file_path = "/Users/maruthikumark/Training/Python_practice/targetgitrepo/template"
        DOCKER_FILE_NAME = "Dockerfile"
        COMMIT_MESSAGE = "Added template.yml"

        if os.path.exists(LOCAL_CLONE_DIR):

            shutil.rmtree(LOCAL_CLONE_DIR)

        # Clone Repository
        repo = git.Repo.clone_from(TARGET_REPO_URL, LOCAL_CLONE_DIR)
        print("✅ Repository cloned successfully.")

        # Create YAML Configuration File
        yaml_data = {
        "project": "Secure Git MY Project",
        "version": "1.0",
        "settings": {
            "debug": True,
            "log_level": "INFO"
        }
        }


        os.makedirs(LOCAL_CLONE_DIR, exist_ok=True)
        config_file_path = os.path.join(Destina_file_path, CONFIG_FILE_NAME)
        os.makedirs(os.path.dirname(config_file_path), exist_ok=True)
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

        dockerfile_path = os.path.join(Destina_file_path, DOCKER_FILE_NAME)

        with open(dockerfile_path, "w") as file:
            file.write(dockerfile_content)

        print("✅ Dockerfile created.")

        # Commit and Push Changes
        repo.index.add([config_file_path, dockerfile_path])
        repo.index.commit(COMMIT_MESSAGE)
        origin = repo.remote(name="origin")
        origin.push()
        print(f"✅ {CONFIG_FILE_NAME} and {DOCKER_FILE_NAME} pushed securely to {TARGET_REPO_URL}")
        return {"message": f"{CONFIG_FILE_NAME} and {DOCKER_FILE_NAME} to {TARGET_REPO_URL} pushed successfully!"}
    except Exception as e:
        return {"error": str(e)}