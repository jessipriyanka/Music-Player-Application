## 🎵 Music Player (Python)

Welcome to the **Music Player** project for the CO7095 Software Measurement & Quality Assurance module at the University of Leicester (2025–2026).

This is a **text-based, console-only** music player application built entirely with Python, using a JSON file (`data/songs.json`) for data storage.

This project implements mandatory QA techniques including Black-box, White-box, and Symbolic/Concolic testing.

---

## 📌 Project Overview

The Music Player allows users to:
- Add songs with validation
- Remove songs
- Search songs
- List all songs
- Play, pause, resume, and stop playback

The application:
- Is implemented **only in Python**
- Uses a **text-based (console) interface**
- Uses a **JSON file** for storage
- Does **not** use a GUI or database (as per module rules)

---

## 🛠️ Technologies and Tools Used

- **Programming Language:** Python
- **IDE:** PyCharm
- **Version Control:** GitHub
- **Testing Framework:** PyTest
- **Coverage Tool:** Coverage.py
- **Complexity Tool:** Radon
- **Project Management:** GitHub Projects (Agile Scrum

---

### 📂 Team Division


| Member                                        | Role | Key File(s)                                                  | Focus |
|:----------------------------------------------| :--- |:-------------------------------------------------------------| :--- |
| ** HIMANISH DEBNATH HIMU (hdh3) **            | CLI & Docs | `main.py`, `_init_.py` ,`data/songs.json` , ` team (proof) ` | JSON handling, User Interface. |
| ** Javvaji Lalitha Vighneswar (lvj4)  **      | Storage & QA | `player/storage.py` , ` tests/symbolic `                     | White-box testing coverage. |
| ** Jessica Priyanka David Penumolu (jpdp1) ** | Playback & QA | `player/music_player.py` , ` tests/blackcox `                | Black-box testing boundary checks. |
| ** Jahnavi Posani (jp698) **                  | Playlist & QA | `player/playlist_manager.py` , ` tests/whitebox `            | Symbolic/Concolic execution. |


---

## ▶️ How to Run the Application

### Step 1: Open Project in PyCharm
1. Launch **PyCharm**
2. Select **File → Open**
3. Choose the root project folder

### Step 2: Run the Program
1. Open `main.py`
2. Right-click and select **Run 'main'**

The console-based menu will appear, allowing you to interact with the Music Player.

---

## 🧪 How to Run Tests

### Install Required Tools
If not already installed:
```bash
python -m pip install pytest coverage radon


Run All Tests
  python -m pytest

Run Specific Test Suites
  python -m pytest team/259034924/test/concolic/
  python -m pytest team/249057908/test/whitebox/
  python -m pytest team/259046094/test/symbolic/
  python -m pytest team/259052949/test/blackbox/

📊 Test Coverage Measurement

To measure test coverage:
  python -m coverage run -m pytest
  python -m coverage report

(Optional HTML report)
  python -m coverage html

📐 Cyclomatic Complexity Measurement
Cyclomatic complexity was measured using Radon:
  python -m radon cc player/playlist_manager.py -s
  python -m radon cc player/music_player.py -s
  python -m radon cc player/storage.py -s

Functions such as add_song() and play() achieve complexity values ≥ 10, meeting module requirements.

🔬 Research Component

Symbolic Execution

Performed manually
Symbolic execution trees were constructed for complex functions
Path conditions were derived and documented

Concolic Testing

Combined concrete execution with symbolic constraint negation
Implemented using PyTest
All concolic tests executed successfully

🧩 Agile Development

36 user stories (9 per team member)
3 sprints planned and completed
Story points estimated using Planning Poker
Progress tracked using GitHub Projects
Velocity, burndown, and EVM calculated and documented

📈 Project Estimation & Measurement

The project applies:

PERT analysis with critical path identification
COCOMO I and COCOMO II for effort estimation
Earned Value Management (EVM) for project tracking
CMMI Level 2 process documentation

All calculations and evidence are included in the final report.



