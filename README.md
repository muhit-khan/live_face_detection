# Live Face Recognition

This project is a real-time face recognition system that can identify known individuals from a live video stream. It uses the `face_recognition` library, which is built on top of `dlib`.

## Features

- Encodes faces from a directory of images.
- Performs real-time face recognition using a webcam.
- Displays the name of the recognized person on the video stream.

## Folder Structure

```
.
├── .flake8
├── .gitignore
├── run.sh                  # Main script to run the project
├── requirements.txt        # Python dependencies
├── source_images/          # Directory for source images of people to recognize
└── src/
    ├── encode_faces.py     # Script to encode faces from source_images
    ├── live_recognition.py # Script to run live face recognition
    ├── face_encodings/
    │   └── encodings.pkl   # Saved face encodings
    └── models/
        └── person.py       # Data model for a person
```

## Installation

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/muhit-khan/live_face_detection
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
    _Note: Installing `dlib` can be tricky. You might need to install `cmake` first. If you face issues, please refer to the official installation guides for `dlib` and `face_recognition`._

## Usage

### 1. Add Photos of Individuals

To add a new person to the recognition system, you need to add one or more photos of them to the `source_images` directory.

- **Image Naming Convention:** The script extracts the person's name from the image filename. The name is the part of the filename **before the first underscore (`_`)**.

  - **Correct Naming:**
    - `Elon_Musk_1.jpg` -> Name: `Elon`
    - `Bill_Gates_2.png` -> Name: `Bill`
    - `Jeff_Bezos_3.jpeg` -> Name: `Jeff`

  - **Incorrect Naming:**
    - `Elon Musk 1.jpg` (contains spaces)
    - `Bill-Gates-2.png` (uses hyphens instead of underscores)

  The text after the first underscore is ignored, so you can use it to number the images or add other information.

- **Supported formats:** The supported image formats are `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.tiff`.

### 2. Encode Faces

After adding new photos, you need to run the face encoding process. This will scan the `source_images` directory, detect faces in the new photos, and save their encodings to the `src/face_encodings/encodings.pkl` file.

### 3. Run Live Recognition

Once the faces are encoded, you can start the live recognition process. This will open a window with your webcam feed and display the names of any recognized individuals.

## Running the Project

There are two ways to run the functionalities of this project:

### Method 1: Using the `run.sh` script (Recommended)

The easiest way to run the project is to use the `run.sh` script, which provides a simple command-line menu.

1.  **Open a terminal** in the project's root directory.
2.  **Run the script:**
    ```bash
    bash run.sh
    ```
3.  **Choose an option from the menu:**
    - **`1. Run Live Recognition`**: Starts the live face recognition.
    - **`2. Encode Faces from Source Images`**: Encodes the faces from the `source_images` directory.
    - **`3. Exit`**: Exits the script.

### Method 2: Running the scripts directly

You can also run the Python scripts directly from the command line. Make sure your virtual environment is activated.

- **To encode faces:**

  ```bash
  python -m src.encode_faces
  ```

- **To run live recognition:**

  ```bash
  python -m src.live_recognition
  ```

## Dependencies

- click==8.2.1
- cmake==4.1.0
- colorama==0.4.6
- dlib
- face-recognition==1.2.3
- face-recognition-models
- iniconfig==2.1.0
- numpy==2.2.6
- opencv-python==4.12.0.88
- packaging==25.0
- pillow==11.3.0
- pluggy==1.6.0
- Pygments==2.19.2
- pytest==8.4.2
- setuptools==80.9.0

## Contributing

Contributions are welcome! Please feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Copyright (c) 2025 MUHIT KHAN
