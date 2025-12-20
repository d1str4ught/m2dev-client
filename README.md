# Client

This repository contains all client-side data, including locale files, configurations, and descriptive text used by the game client.

## Changelog 📋

### 🐛 Bug Fixes
* **Skill 19:** Applied the correct `MOV_SPEED` value fix for Skill 19 across all locales.
* **Messenger - UI:** Fixed a critical UI issue where the name of a recently removed friend would sometimes appear on top of the next name in the list, or the "Empty" string, if it was selected during the removal process.

### ⬆️ Feature Improvements
* **Messenger System:**
	* **Live Status Updates:** Live updates for adding/removing friend for both parties.
	* **Auto-Deselect:** When a player removes a friend, or is removed by one, the entry is automatically deselected in the Messenger window.
	* **Early Initialization:** The Messenger window is now automatically initialized (without visually opening the window) upon starting the game phase, allowing it to receive real-time updates from the very beginning.
	* **Request Handling:** Pressing the `Escape` key while the request dialog is open now denies the request normally.
	* **Button State:** The Whisper and Delete buttons are automatically disabled when removing/getting removed by a friend with the Messenger window open.
	* **Target board:** The "Friend" button dynamically updates upon adding/removing a friend for both parties, if target is focused.
* **Inventory Management:** Inventory calculations are now correctly designed to handle togglable item activation effects across any number of inventory pages by calculating `page total slots * total pages`.
* **Skill Cooldowns and States:** A massive update to ensure reliability across various scenarios:
	* **Window/Taskbar Persistence:** Cooldowns and active slot effects are now correctly maintained and updated in the Character Window and Taskbar during actions such as: repositioning skills, leveling up, changing skill grades (including Perfect), mounting/unmounting, changing Character Window pages, switching Skill View tabs, closing/reopening the window, and relogging. Supports togglable, non-togglable, and togglable-with-cooldown skills.
	* **Level Reset Clearing:** Skill cooldowns and active slot states are properly cleared when the skill level is reset to 0.
	* **Support togglables:** Combo automatically deactivates if its level is changed to 0 (e.g., via `/setsk`).
	* **Horse Skill Cooldowns:** Horse skill cooldowns are cleared if their level is changed to 0.
	* **Horse Skill View Logic:** The Horse skills page now correctly appears when the riding skill (Skill 130) reaches **level 21+** (not 20+).
	* **Taskbar Sync:** Horse skills are automatically removed from the Taskbar, and the Skill View switches pages automatically, if the riding skill level drops below 21 (e.g., via `/setsk`).
	* **Skill group 0 support for Horse page:** The Horse skill page is now visible even if there are no skills assigned to that group, provided the riding skill level is high enough.
	* **Support skill levels:** Support and Horse skill states are correctly maintained when the character's skill group is reset.
* **.gitignore file:** Ignoring all files and directories ending in `_BAK` or `.BAK` (case-insensitive)
