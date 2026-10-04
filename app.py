"""Streamlit entry point for the ISO quality assistant."""

from pathlib import Path
import sys


SRC_DIRECTORY = Path(__file__).resolve().parent / "src"
sys.path.insert(0, str(SRC_DIRECTORY))

from iso_assistant.ui import run


if __name__ == "__main__":
    run()
