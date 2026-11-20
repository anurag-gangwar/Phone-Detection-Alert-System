# Phone Detection Alert System

A real-time computer vision application that detects cell phones using a YOLOv8 model and plays escalating audio warnings. Detected phones are highlighted on the camera feed.

## Features

- Real-time webcam phone detection
- YOLOv8 object detection
- Visual bounding boxes and detection labels
- Normal warning for the first two detections
- Strict warning after repeated detections
- Five-second cooldown between alerts
- Press `Q` to exit

## Requirements

- Python 3.9 or later
- Webcam
- Working audio output
- macOS, Linux, or Windows

## Installation

```bash
git clone <repository-url>
cd spacle

python -m venv .venv
source .venv/bin/activate

pip install --upgrade pip
pip install opencv-python ultralytics playsound
