from mcp.server.fastmcp import FastMCP
import os

mcp = FastMCP("Sticky notes")

NOTE_FILE = "notes.txt"
NOTE_FILE_PATH = os.path.join(os.path.dirname(__file__), NOTE_FILE)

def ensure_note_file_exists():
    if not os.path.exists(NOTE_FILE_PATH):
        with open(NOTE_FILE_PATH, "w") as f:
            f.write("")


@mcp.tool()
def add_note(note: str):
    """
    append a note to the note file
    Args:
        note(str): the note to add
    Returns:
        a confirmation message
    """
    ensure_note_file_exists()
    with open(NOTE_FILE_PATH, "a") as f:
        f.write(note + "\n")
    return "Note added"

@mcp.tool()
def read_notes():
    """
    read the notes from the note file and return all the notes of file
    Returns:
        all note as a single string separated by newlines.
        If no notes are present , a default message is returned.
    """
    ensure_note_file_exists()
    with open(NOTE_FILE_PATH, "r") as f:
        content = f.read().strip()
    return content

@mcp.resource("notes://latest")
def get_latest_note():
    """
    get the latest note from the note file
    Returns:
       str: the latest note, if note not present, a default message is returned.
    """
    ensure_note_file_exists()
    with open(NOTE_FILE_PATH, "r") as f:
        lines = f.readlines()
    return lines[-1].strip() if lines else "No notes yet"

@mcp.prompt()
def note_summary_prompt():
    """
    Generate a prompt asking the AI to summarize all current notes.
    Returns:
       str:  A prompt string that includes all notes and asks for a summary.
        If no notes are present, it returns a default message.   
    """
    ensure_note_file_exists()
    with open(NOTE_FILE_PATH, "r") as f:
        content = f.read().strip()
    if not content:
        return "No notes yet"
    return f"Summarize the current notes: {content}"


    
