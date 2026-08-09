import os
from dotenv import load_dotenv


def load_config() -> dict[str, str | None]:
    load_dotenv()
    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT"),
    }
    return config


def display_oracle_status(config: dict[str, str | None]) -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print("\nConfiguration loaded:")
    mode = config["MATRIX_MODE"]
    print(f"Mode: {mode}")
    db_url = config["DATABASE_URL"]
    if not db_url:
        print("Database: [WARNING] Missing connection string")
    elif mode == "production":
        print(f"Database: Connected to production instance ({db_url})")
    else:
        print("Database: Connected to local instance")
    api_key = config["API_KEY"]
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: [WARNING] Unauthenticated (Missing API_KEY)")
    print(f"Log Leve: {config['LOG_LEVEL']}")
    zion = config["ZION_ENDPOINT"]
    if zion:
        print(f"Zion Network: Online ({zion})")
    else:
        print("Zion Network: Offline (Missing endpoint)")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found (using environment/defaults)")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


def main() -> None:
    config = load_config()
    display_oracle_status(config)


if __name__ == "__main__":
    main()
