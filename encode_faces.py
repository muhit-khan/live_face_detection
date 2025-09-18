# encode_faces.py

import cv2
import face_recognition
import pickle
import numpy as np
from pathlib import Path
from src.models.person import KnownPerson, FaceEncoding


# Update this to match your actual directory structure
SOURCE_IMAGES_DIR = Path("source_images")  # Changed from "src/extracted_images"
ENCODINGS_FILE = Path("src/face_encodings/encodings.pkl")
FACE_CASCADE_PATH = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'


def extract_faces_from_image(image_path, min_face_size=(50, 50)):
    """Extract face regions from an image using OpenCV Haar Cascade."""
    try:
        # Read the image
        image = cv2.imread(str(image_path))
        if image is None:
            print(f"Warning: Could not load image {image_path}")
            return []
        
        # Convert to grayscale for face detection
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # Load the face cascade classifier
        face_cascade = cv2.CascadeClassifier(FACE_CASCADE_PATH)
        
        # Detect faces with multiple scale factors for better detection
        faces = face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=min_face_size,
            flags=cv2.CASCADE_SCALE_IMAGE
        )
        
        # Extract face regions
        face_images = []
        for (x, y, w, h) in faces:
            # Add some padding around the face
            padding = int(0.1 * max(w, h))
            x_start = max(0, x - padding)
            y_start = max(0, y - padding)
            x_end = min(image.shape[1], x + w + padding)
            y_end = min(image.shape[0], y + h + padding)
            
            face_img = image[y_start:y_end, x_start:x_end]
            
            # Resize face to standard size for better encoding consistency
            face_img = cv2.resize(face_img, (160, 160))
            face_images.append(face_img)
            
        return face_images
        
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return []


def get_face_encodings(face_image):
    """Get face encodings from a face image using face_recognition library."""
    try:
        # Convert BGR to RGB for face_recognition
        rgb_face = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
        
        # Get face encodings
        encodings = face_recognition.face_encodings(rgb_face)
        
        return encodings
        
    except Exception as e:
        print(f"Error getting encodings: {e}")
        return []


def encode_faces():
    """Encode faces from source images and save them to a file."""
    print("Starting face encoding process...")
    
    # Create directories if they don't exist
    SOURCE_IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    ENCODINGS_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    known_people = []
    total_faces_processed = 0
    
    # Supported image extensions
    supported_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    
    # Process all image files in the directory
    image_files = [f for f in SOURCE_IMAGES_DIR.iterdir() 
                   if f.is_file() and f.suffix.lower() in supported_extensions]
    
    if not image_files:
        print(f"No image files found in {SOURCE_IMAGES_DIR}")
        return
    
    print(f"Found {len(image_files)} image files to process...")
    
    for image_path in image_files:
        print(f"Processing: {image_path.name}")
        
        # Extract person name from filename (before first underscore)
        name = image_path.stem.split("_")[0]
        
        # Extract faces from the image
        face_images = extract_faces_from_image(image_path)
        
        if not face_images:
            print(f"  No faces detected in {image_path.name}")
            continue
            
        print(f"  Found {len(face_images)} face(s) in {image_path.name}")
        
        # Process each detected face
        for i, face_img in enumerate(face_images):
            # Get face encodings
            face_encodings = get_face_encodings(face_img)
            
            if not face_encodings:
                print(f"  Could not encode face {i+1} from {image_path.name}")
                continue
                
            # Use the first (and usually only) encoding
            encoding = face_encodings[0]
            face_encoding = FaceEncoding(encoding=encoding.tolist())
            
            # Check if person already exists in our list
            person = next((p for p in known_people if p.name == name), None)
            if person:
                person.encodings.append(face_encoding)
            else:
                known_people.append(KnownPerson(name=name, encodings=[face_encoding]))
            
            total_faces_processed += 1
            print(f"  Successfully encoded face {i+1} for {name}")
    
    # Save encodings to file
    if known_people:
        with open(ENCODINGS_FILE, "wb") as f:
            pickle.dump(known_people, f)
        
        # Print summary
        print(f"\n=== Encoding Complete ===")
        print(f"Total people: {len(known_people)}")
        print(f"Total faces processed: {total_faces_processed}")
        print(f"Encodings saved to: {ENCODINGS_FILE}")
        
        # Print details for each person
        for person in known_people:
            print(f"  {person.name}: {len(person.encodings)} encoding(s)")
    else:
        print("No faces were successfully encoded!")


def verify_encodings():
    """Verify that encodings file exists and can be loaded."""
    try:
        if ENCODINGS_FILE.exists():
            with open(ENCODINGS_FILE, "rb") as f:
                known_people = pickle.load(f)
            
            print(f"\n=== Verification ===")
            print(f"Encodings file loaded successfully!")
            print(f"Found {len(known_people)} people in encodings file")
            
            return True
        else:
            print("Encodings file does not exist!")
            return False
            
    except Exception as e:
        print(f"Error loading encodings file: {e}")
        return False


if __name__ == "__main__":
    print("Face Recognition - Encoding Script")
    print("=" * 40)
    
    # Run the encoding process
    encode_faces()
    
    # Verify the results
    verify_encodings()
