# Client

This repository contains all client-side data, including locale files, configurations, and descriptive text used by the game client.

## 📋 Changelog

### ⬆️ Feature Improvements
* **Quickslot Definitions:** The maximum number of quickslot slots is now explicitly defined for python scripts to improve consistency.
* **Alchemy Deck Toggling:** Alchemy decks can now be toggled via hotkeys: CTRL+C for the first deck and CTRL+D for the second. Activating one deck will automatically disable the other (if active).
* **Taskbar Item Swapping:** Improved taskbar logic: dragging an item to a non-empty slot now swaps positions with the existing item if it already exists on the taskbar, rather than replacing it.
