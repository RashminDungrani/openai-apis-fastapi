import enum
from typing import Optional

from pydantic import BaseSettings

# from yarl import URL

# TEMP_DIR = Path(gettempdir())


class LogLevel(str, enum.Enum):
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    OPENAI_API_KEY: str = ""
    host: str = "192.168.1.237"
    # host: str = "0.0.0.0"
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    # Current environment
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO

    # Variables for the database
    db_scheme: str = "sqlite"
    db_host: str = "localhost"
    db_port: Optional[int] = None  # 5432
    db_user: Optional[str] = None
    db_pass: Optional[str] = None
    db_path: str = "UNDEFINED"
    db_echo: Optional[bool] = False

    # @property
    # def db_url(self) -> URL:
    #     """
    #     Assemble database URL from settings.

    #     :return: database URL.
    #     """
    #     generated_url = URL.build(
    #         scheme=self.db_scheme,
    #         host=self.db_host,
    #         port=self.db_port,
    #         user=self.db_user,
    #         password=self.db_pass,
    #         path="/" + self.db_path,  # path should be commented only while creating db from main file
    #     )
    #     # generated_url = URL("mysql+aiomysql://root:password@mysql_db:3306/dyv_db")
    #     print("Generated DB URL ::", generated_url)
    #     return generated_url
    #     # return URL("mysql+aiomysql://mysql:password@localhost:3306/dyv_db")

    class Config:
        env_file = "envs/dev.env"
        env_file_encoding = "utf-8"


settings = Settings()
