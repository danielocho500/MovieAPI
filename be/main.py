from dotenv import load_dotenv
import uvicorn
import logging

load_dotenv()

logging.basicConfig(level=logging.ERROR,
                    format='%(asctime)s - %(threadName)s - %(processName)s - %(levelname)s - %(message)s',
                    filename='errors.log',
                    filemode='a')

if __name__ == "__main__":
    uvicorn.run("server.app:app", host="0.0.0.0", port=8000, reload=True, env_file=".env")
