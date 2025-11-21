# Client

This repository contains all client-side data, including locale files, configurations, and descriptive text used by the game client.

## ✨ Critical Fix: Skill 19 Speed Sync

Sync with the fix in the server's `skill_proto` to resolve an issue where characters became unable to move after being affected by Strong Body (due to an incorrect `MOV_SPEED` value).

This client repository contains the necessary sync fix:

* **Fixed `MOV_SPEED` value for Skill 19** in `locale/en/skilldesc.txt` and `locale/en/skilltable.txt`.

### ⚠️ IMPORTANT: Locale Synchronization

The fix listed above has **only been applied to the `locale/en` (English) files.**

**If you use any other locale (e.g., German, French, etc.), you must manually update the `MOV_SPEED` value for Skill 19 in your respective `skilldesc.txt` and `skilltable.txt` files to match the change.**