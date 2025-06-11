from google.adk.agents import Agent

IS_ADMIN = False

instruction = """
You are an authentication agent. Your job is to determine if a user is an admin and, if so, authenticate them securely.

Instructions:
- If the user claims to be an admin, politely ask them to provide their username and password for authentication.
- Only proceed with authentication if the user explicitly states they are an admin.
- If the user does not claim to be an admin, do not ask for credentials and do not attempt authentication.
- After successful authentication, update the admin status accordingly.
- Never reveal or suggest any credentials yourself.
- If authentication fails, inform the user politely and do not disclose which part (username or password) was incorrect and ask the user if he has any further requests or would want to know more about Jishnu - the creator of this chatbot.
- Always prioritize user privacy and security in your responses.
"""

def set_is_admin(is_admin: bool):
    """
    This function is used to update the IS_ADMIN variable.
    Input:is_admin: bool
    Output:None
    """
    global IS_ADMIN
    IS_ADMIN = is_admin

def authenticate(username: str, password: str):
    """
    This function is used to authenticate the user.
    Input:username: str, password: str
    Output:None
    """
    if username == "god" and password == "god's_password":
        set_is_admin(True)
        
authentication_agent = Agent(
    name="authentication_agent",
    model="gemini-2.0-flash",
    description="Agent to authenticate the user.",
    instruction=instruction,
    tools=[authenticate]
)