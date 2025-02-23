from cryptography.fernet import Fernet

# Generate a key and save it securely
key = Fernet.generate_key()
with open("secret.key", "wb") as key_file:
    key_file.write(key)

# Encrypt the GitHub token
token = "pwd"  # Replace with your actual token
cipher = Fernet(key)
encrypted_token = cipher.encrypt(token.encode())

# Save encrypted token in config.yml
import yaml
config_data = {
    "github_username": "id",
    "encrypted_token": encrypted_token.decode()
}
with open("config.yml", "w") as file:
    yaml.dump(config_data, file)

print("GitHub token encrypted and saved in config.yml")
