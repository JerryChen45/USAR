# USAR
Raspberry Pi–based robotics control stack for teleoperation and autonomy. Includes cross-platform controller input (PyGame), networking, and hardware interfaces for motors and sensors. Designed for modular development, testing, and deployment across team-built robotic systems.

---

## Setup

### Mac (without Homebrew) & Windows

#### 1. Install Python
- **Mac:** Download from [python.org](https://www.python.org/downloads/) and run the installer.
- **Windows:** Download from [python.org](https://www.python.org/downloads/) and run the installer. **Check "Add python.exe to PATH"** before clicking Install.

Verify the install:
```
python --version
```
or on Mac you may need:
```
python3 --version
```

#### 2. Install pygame

**Mac:**
```
pip3 install pygame
```

**Windows:**
```
pip install pygame
```

#### 3. Plug in your controller
Connect your Xbox controller via USB (or wireless USB dongle). Bluetooth may work but USB is more reliable.

#### 4. Run the test script

**Mac:**
```
python3 PyGameTest.py
```

**Windows:**
```
python PyGameTest.py
```

Move the sticks and press buttons — you should see live axis/button output in the terminal.

---

### Mac (with Homebrew)
```
brew install python
pip3 install pygame
python3 PyGameTest.py
```
