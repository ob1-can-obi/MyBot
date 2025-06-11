"""
This ensures MongoDB container is running before starting the agent.
"""

import subprocess
import sys
import time
import os


def ensure_mongodb_container():
    """Ensure MongoDB MCP container is running"""
    container_name = "mongodb-mcp-persistent"
    image_name = "mongodb/mongodb-mcp-server:latest" 
    connection_string = # Add mongodb connection string here
    
    print("Checking MongoDB MCP container status...")
    
    try:
        # Check if container is running
        result = subprocess.run(
            ["docker", "ps", "-q", "-f", f"name={container_name}"],
            capture_output=True, text=True, check=True
        )
        
        if result.stdout.strip():
            print(f"MongoDB MCP container '{container_name}' is already running")
            return True
            
        # Check if container exists but is stopped
        result = subprocess.run(
            ["docker", "ps", "-a", "-q", "-f", f"name={container_name}"],
            capture_output=True, text=True, check=True
        )
        
        if result.stdout.strip():
            # Start existing container
            print(f"Starting existing container '{container_name}'...")
            subprocess.run(["docker", "start", container_name], check=True)
        else:
            # Create and start new container
            print(f"Creating and starting new container '{container_name}'...")
            subprocess.run([
                "docker", "run", "-d",
                "--name", container_name,
                "-e", f"MDB_MCP_CONNECTION_STRING={connection_string}",
                image_name
            ], check=True)
        
        # Wait a moment for container to be ready
        time.sleep(3)
        print(f"MongoDB MCP container '{container_name}' is ready!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"Error managing Docker container: {e}")
        print("Please ensure Docker is running and try again.")
        return False
    except FileNotFoundError:
        print("Docker not found. Please install Docker first.")
        return False

def main():
    """Main startup function"""
    print("Starting Jishnu's Personal Chatbot...")
    
    # Ensure MongoDB container is running
    if not ensure_mongodb_container():
        print("Cannot start agent without MongoDB MCP container")
        print("Please ensure Docker is running and try again.")
        sys.exit(1)
    
    print("\nStarting ADK web interface...")
    print("The web interface will be available at: http://localhost:8000")
    print("Once it starts, open the URL and start with 'Hello'")
    print("\n" + "="*60)
    
    # Start ADK web
    try:
        subprocess.run(["adk", "web"], check=True)
    except KeyboardInterrupt:
        print("\nShutting down...")
    except subprocess.CalledProcessError as e:
        print(f"Error starting ADK: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 
