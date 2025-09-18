#!/bin/bash

# Activate virtual environment
if [ -f ".venv/Scripts/activate" ]; then
    source .venv/Scripts/activate
else
    echo "Virtual environment not found. Please run setup first."
    exit 1
fi

# Function to display menu
show_menu() {
    echo ""
    echo "======================================"
    echo "   Live Face Recognition Project"
    echo "======================================"
    echo "1. Run Live Recognition"
    echo "2. Encode Faces from Source Images"
    echo "3. Exit"
    echo ""
}

# Main loop
while true; do
    show_menu
    read -p "Enter your choice [1-3]: " choice

    case $choice in
        1)
            echo "Starting live recognition...(Press 'q' to quit)"
            python -m src.live_recognition
            ;;
        2)
            echo "Starting face encoding process..."
            python -m src.encode_faces
            ;;
        3)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 3."
            ;;
    esac
done
