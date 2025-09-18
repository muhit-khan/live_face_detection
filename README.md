# Live Face Recognition

This project is a real-time face recognition system that can identify known individuals from a live video stream. It uses the `face_recognition` library, which is built on top of `dlib`.

## Features

*   Encodes faces from a directory of images.
*   Performs real-time face recognition using a webcam.
*   Displays the name of the recognized person on the video stream.

## Folder Structure

```
.
├── .flake8
├── .gitignore
├── encode_faces.py         # Script to encode faces from source_images
├── live_recognition.py     # Script to run live face recognition
├── requirements.txt        # Python dependencies
├── source_images/          # Directory for source images of people to recognize
└── src/
    ├── face_encodings/
    │   └── encodings.pkl   # Saved face encodings
    └── models/
        └── person.py       # Data model for a person
```

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd live_face_detection
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/Scripts/activate  # On Windows
    # source .venv/bin/activate  # On macOS/Linux
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
    *Note: Installing `dlib` can be tricky. You might need to install `cmake` first. If you face issues, please refer to the official installation guides for `dlib` and `face_recognition`.*

## Usage

1.  **Add source images:**
    Place images of the people you want to recognize in the `source_images` directory. The images should be named in a way that you can identify the person (e.g., `john_doe_1.jpg`, `john_doe_2.jpg`). The name of the person will be extracted from the filename.

2.  **Encode the faces:**
    Run the `encode_faces.py` script to process the images in `source_images` and create the face encodings.
    ```bash
    python encode_faces.py
    ```
    This will create a file named `encodings.pkl` in the `src/face_encodings` directory.

3.  **Run live face recognition:**
    Run the `live_recognition.py` script to start the webcam and perform real-time face recognition.
    ```bash
    python live_recognition.py
    ```
    The script will open a window showing the video stream from your webcam. If a known person is recognized, their name will be displayed on the screen.

## Dependencies

*   click==8.2.1
*   cmake==4.1.0
*   colorama==0.4.6
*   dlib
*   face-recognition==1.2.3
*   face-recognition-models
*   iniconfig==2.1.0
*   numpy==2.2.6
*   opencv-python==4.12.0.88
*   packaging==25.0
*   pillow==11.3.0
*   pluggy==1.6.0
*   Pygments==2.19.2
*   pytest==8.4.2
*   setuptools==80.9.0

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 MUHIT KHAN
