import os
import uvicorn
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()  

    if not os.getenv("FASTAPI_SETTINGS_MODULE"):
        os.environ["FASTAPI_SETTINGS_MODULE"] = "core.configs.settings"

    uvicorn.run(
        "main:app",
        debug=os.getenv("DEBUG").lower() == "true",
        port=int(os.getenv("PORT")),
        host=os.getenv("HOST"),
        lifespan="on",
        log_level="info",
    )