# YTShadow (Personal Use)

*A small utility to clone any public YouTube playlist into **your own account** as a **private** playlist. Built strictly for personal use while the app is in Google OAuth **Testing** mode.*

> **Important:** This project is configured for **personal use only**. **Only my Google account is added as a Test User** on the OAuth consent screen. No other users are authorized, and I do **not** provide support or access for third parties.

## ⚠️ Personal Use & Access Scope

* **OAuth status:** *Testing* (not verified, not public).
* **Allowed users:** **Only me** (my Google account email is added under *Test users* in the Google Cloud OAuth consent screen).
* **Data scope used:** `https://www.googleapis.com/auth/youtube` (required to create and modify playlists in my own account).
* **No external storage:** Credentials and tokens are stored **locally** on my machine only.
* **No data sharing:** The app does **not** collect, transmit, or sell any user data.

## ✨ What it does

* Fetches all video IDs from a **public** YouTube playlist.
* Creates a **new private playlist** in **my** YouTube account.
* Adds all fetched videos to the new playlist.
* Optional: can be extended to incremental sync (add only new items on re-run).

## 🛠 Tech Stack

* **Language:** Python 3.9+
* **APIs/SDKs:** YouTube Data API v3, `google-api-python-client`, `google-auth-oauthlib`, `google-auth-httplib2`


## 🔐 OAuth & Credentials (Testing Mode)

This app uses a **Desktop** OAuth client. Since it’s in Testing mode:

* Google only allows sign‑in from **whitelisted Test users**.
* I have added **only my account** as a Test user.
* Any other account attempting to sign in will see **`Error 403: access_denied`**.

## 📄 Usage

* Input: **Public** YouTube playlist URL (contains `list=...`).
* The script creates a **private** playlist in my account and copies all videos.
* I can then rename, reorder, or edit my copy without affecting the original.

## 🧭 Limitations

* Intended for **personal archival/cloning** of public playlists.
* Does **not** monitor changes automatically (unless I add a sync routine).
* Subject to YouTube Data API quotas/policies.

## 📜 License

* **Unlicensed / Personal Use Only.** You may copy concepts for your own personal, non‑commercial projects, but this repository is not intended for redistribution or third‑party use.

## 🛡️ Disclaimer

This project is provided **as is** for personal educational use. It is **not** an official Google/YouTube product. 
Use is subject to the YouTube Terms of Service and Google API Services User Data Policy. I am solely responsible for my usage and data handling.
