import os
import subprocess
import platform

def setup_environment():
    """Set up the production environment."""
    # Create virtual environment
    subprocess.run(["python", "-m", "venv", "venv"])
    
    # Activate virtual environment and install dependencies
    if platform.system() == "MacOS":
        subprocess.run(["venv\\Scripts\\pip", "install", "-r", "requirements.txt"])
    else:
        subprocess.run(["venv/bin/pip", "install", "-r", "requirements.txt"])
    
    # Create production configuration
    with open(".env.production", "w") as f:
        f.write("ENVIRONMENT=production\n")
        f.write(f"DATABASE_URL={os.environ.get('DATABASE_URL', 'sqlite:///./ai_tutor_prod.db')}\n")
        f.write(f"AUTH0_DOMAIN={os.environ.get('AUTH0_DOMAIN', '')}\n")
        f.write(f"AUTH0_API_AUDIENCE={os.environ.get('AUTH0_API_AUDIENCE', '')}\n")
        f.write(f"OLLAMA_API_URL={os.environ.get('OLLAMA_API_URL', 'http://localhost:11434/api')}\n")

def start_server():
    """Start the production server."""
    if platform.system() == "Windows":
        subprocess.Popen(["venv\\Scripts\\uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"])
    else:
        subprocess.Popen(["venv/bin/uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"])

def main():
    setup_environment()
    start_server()
    print("Backend server started on http://0.0.0.0:8000")

if __name__ == "__main__":
    main()