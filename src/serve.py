import os
import uvicorn
from dotenv import load_dotenv

from .main import get_settings

if __name__ == "__main__":
    load_dotenv()  

    if not os.getenv("FASTAPI_SETTINGS_MODULE"):
        os.environ["FASTAPI_SETTINGS_MODULE"] = "core.configs.settings"

    settings = get_settings()

    uvicorn.run(
        "main:app",
        debug=os.getenv("DEBUG").lower() == "true",
        port=int(os.getenv("PORT")),
        host=os.getenv("HOST"),
        reload=settings.reload,
        lifespan="on",
        log_level="info",
    )