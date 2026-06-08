import os
from dotenv import load_dotenv
from huggingface_hub import HfApi

# Load environment variables from .env file
load_dotenv()

# Get token and repo name from environment variables
token = os.environ.get("HUGGINGFACE_TOKEN")
repo_url = os.environ.get("HUGGINGFACE_REPO")

if not token or not repo_url:
    print("Error: HUGGINGFACE_TOKEN or HUGGINGFACE_REPO not found in .env")
    exit(1)

# Extract repo id from repo url
# Assuming URL format is https://huggingface.co/spaces/Lee010043/seismiology_experiment_2
repo_id = repo_url.replace("https://huggingface.co/spaces/", "")

api = HfApi()

print(f"Deploying to space: {repo_id}")

try:
    api.upload_folder(
        folder_path="hf_space_app",
        repo_id=repo_id,
        repo_type="space",
        token=token
    )
    print("Deployment successful!")
    print(f"Checkout your space at: {repo_url}")
except Exception as e:
    print(f"Failed to deploy: {e}")
