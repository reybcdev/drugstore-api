from supabase import create_client, Client
import os

def get_supabase_client() -> Client:
    """Create and return a Supabase client instance."""
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    
    if not url or not key:
        raise ValueError("SUPABASE_URL and SUPABASE_KEY must be set in .env file")
        
    return create_client(url, key)
