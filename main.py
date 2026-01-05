import uvicorn
from dotenv import load_dotenv
from pathlib import Path
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)
from app.app import example

if __name__ == '__main__':
    uvicorn.run(example, host="0.0.0.0", port=8000)