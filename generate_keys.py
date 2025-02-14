import secrets
import re
from pathlib import Path

def generate_secure_key(length: int = 32) -> str:
    """Generate a secure random key of specified length."""
    return secrets.token_urlsafe(length)

def update_env_file(env_path: Path) -> None:
    """Update the .env file with new secure keys."""
    if not env_path.exists():
        print(f"Error: {env_path} does not exist")
        return

    # Read the current .env content
    content = env_path.read_text()
    
    # Generate new keys
    bull_auth_key = generate_secure_key(32)
    test_api_key = generate_secure_key(32)
    
    # Replace the placeholder keys with new secure keys
    content = re.sub(
        r'BULL_AUTH_KEY=.*',
        f'BULL_AUTH_KEY={bull_auth_key}',
        content
    )
    content = re.sub(
        r'TEST_API_KEY=.*',
        f'TEST_API_KEY={test_api_key}',
        content
    )
    
    # Write the updated content back to the file
    env_path.write_text(content)
    
    print("Generated new secure keys:")
    print(f"BULL_AUTH_KEY={bull_auth_key}")
    print(f"TEST_API_KEY={test_api_key}")

if __name__ == "__main__":
    env_path = Path(__file__).parent / ".env"
    update_env_file(env_path) 