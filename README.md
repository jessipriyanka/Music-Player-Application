## 🎵 Music Player (Python)

Welcome to the **Music Player** project for the CO7095 Software Measurement & Quality Assurance module at the University of Leicester (2025–2026).

This is a **text-based, console-only** music player application built entirely with Python, using a JSON file (`data/songs.json`) for data storage.

This project implements mandatory QA techniques including Black-box, White-box, and Symbolic/Concolic testing.

---

### 🚀 How to Run the Application

1.  **Open in PyCharm:**
    * In PyCharm, go to **File** $\rightarrow$ **Open**.
    * Select the root project folder: `music_player/`.
2.  **Run `main.py`:**
    * Find the file `main.py`.
    * Right-click on `main.py` and select **Run 'main'**.

The application will start with the main menu interface.

---

### 🧪 Running Tests (Quality Assurance)

This project uses **`pytest`** for running all test suites.

1.  **Install `pytest`** (if not already installed):
    ```bash
    pip install pytest
    ```
2.  **Run All Tests:**
    Open the **PyCharm Terminal** (View $\rightarrow$ Tool Windows $\rightarrow$ Terminal) and execute:
    ```bash
    pytest tests/
    ```
3.  **Run Specific QA Suites:**
    You can target specific mandatory testing folders:
    * **Black-box tests :** `pytest tests/blackbox/`
    * **White-box tests :** `pytest tests/whitebox/`
    * **Symbolic/Concolic tests :** `pytest tests/symbolic/`

---

### 📂 Project Structure & Team Division


| Member                                        | Role | Key File(s)                                                  | Focus |
|:----------------------------------------------| :--- |:-------------------------------------------------------------| :--- |
| ** HIMANISH DEBNATH HIMU (hdh3) **            | CLI & Docs | `main.py`, `_init_.py` ,`data/songs.json` , ` team (proof) ` | JSON handling, User Interface. |
| ** Javvaji Lalitha Vighneswar (lvj4)  **      | Storage & QA | `player/storage.py` , ` tests/symbolic `                     | White-box testing coverage. |
| ** Jessica Priyanka David Penumolu (jpdp1) ** | Playback & QA | `player/music_player.py` , ` tests/blackcox `                | Black-box testing boundary checks. |
| ** Jahnavi Posani (jp698) **                  | Playlist & QA | `player/playlist_manager.py` , ` tests/whitebox `            | Symbolic/Concolic execution. |


---

🏃 – Sprint Summary

🟦 Sprint 1 — Foundation & Core Features (Completed)

Project structure and JSON storage setup.
Implementation of Storage, PlaylistManager, and MusicPlayer basic controls.
Initial Black-box, White-box, and Symbolic test skeletons.

🟩 Sprint 2 — Expanded Logic & QA Coverage (Completed)

Storage error handling (missing/corrupt JSON).
Playback edge cases (resume, already playing, invalid ID).
Expanded test coverage for all primary functions.

🟧 Sprint 3 — Integration & Final QA (Completed)

Full integration across all modules.
Symbolic execution tree completion.
Team contribution documentation and final verification




