import os
from git import Repo

#token = os.environ.get("GIT_TOKEN")  # Set token as an environment variable
#repo_url = f"https://{token}@github.com/your_username/your_repo.git"
local_dir = "/Users/maruthikumark/Training/Python_practice"

TARGET_REPO_URL = "https://id:{pwd}@github.com/maruthi448/sampleproj.git"

#git clone TARGET_REPO_URL

Repo.clone_from(TARGET_REPO_URL, local_dir)
