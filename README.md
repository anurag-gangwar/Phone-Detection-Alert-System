# Phone Detection Alert System

A real-time computer vision application that detects cell phones with YOLOv8 and plays audio warnings. Detected phones are highlighted in the webcam feed.

## Features

- Detects cell phones from a live webcam feed
- Draws a bounding box and label around detected phones
- Plays a normal warning for the first two alerts and a stricter warning afterward
- Waits at least five seconds between audio alerts
- Press `Q` to quit

## Requirements

- Python 3.9 or later
- A webcam
- Audio output

## Setup

Clone the repository and enter its directory:

```bash
git clone https://github.com/anurag-gangwar/Phone-Detection-Alert-System.git
cd Phone-Detection-Alert-System
```

Create and activate a virtual environment:

```bash
python -m venv .venv
```

macOS/Linux:

```bash
source .venv/bin/activate
```

Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies and run the application:

```bash
python -m pip install --upgrade pip
python -m pip install opencv-python ultralytics playsound
python app.py
```

The application opens the default webcam and loads the included `yolov8n.pt` model. Keep `warning1.mp3` and `warning.mp3` in the project directory so the audio alerts can be found.

## Project files

- `app.py` - Webcam capture, phone detection, and alert logic
- `yolov8n.pt` - YOLOv8 nano model
- `warning1.mp3` - Normal warning sound
- `warning.mp3` - Strict warning sound

## Notes

- The application uses the system's default camera. Close other apps that may be using it if the camera does not open.
- Ensure that Python has permission to access the camera and play audio.
- The detection counter advances when an audio alert is triggered, not for every frame in which a phone appears.
