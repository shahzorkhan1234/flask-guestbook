# Putting Your Website on the Internet (PythonAnywhere)

Right now your guestbook only runs on your own computer. Let's put it
online so anyone in the world can open it. We'll use **PythonAnywhere**,
which is free and made for Python.

You'll need your project on **GitHub** first (ask your teacher if you
haven't pushed it yet).

---

## Step 1 — Make a free account

1. Go to **pythonanywhere.com** and click **Pricing & signup**.
2. Choose the **"Create a Beginner account"** (the $0 one).
3. Pick a username — this becomes part of your website address, like
   `yourname.pythonanywhere.com`. Choose it carefully!
4. Confirm your email.

---

## Step 2 — Get your code onto PythonAnywhere

1. On your PythonAnywhere dashboard, open a **Bash console**
   (click **Consoles** → **Bash**).
2. Type this, using YOUR GitHub link, then press Enter:

   ```bash
   git clone https://github.com/YOUR-USERNAME/flask-guestbook.git
   ```

3. Install the parts your app needs:

   ```bash
   cd flask-guestbook
   pip install --user -r requirements.txt
   ```

---

## Step 3 — Create the web app

1. Click the **Web** tab at the top, then **Add a new web app**.
2. Click **Next** (accept the free domain).
3. Choose **Flask**, then choose the newest **Python 3** version.
4. It asks for a path. It will suggest something like
   `/home/YOURNAME/mysite/flask_app.py`.
   **Change `mysite/flask_app.py` to point at your project instead** —
   ask your teacher to help match the path to your `app.py`. It should
   end in `/flask-guestbook/app.py`.

---

## Step 4 — Tell it how to start your app

1. Still on the **Web** tab, scroll to the **Code** section and click the
   link next to **WSGI configuration file**.
2. Find the part near the bottom that imports the app. Make it say:

   ```python
   import sys
   path = '/home/YOURNAME/flask-guestbook'
   if path not in sys.path:
       sys.path.append(path)

   from app import app as application
   ```

   (Replace `YOURNAME` with your real username.)
3. Click **Save**.

---

## Step 5 — Launch! 🚀

1. Go back to the **Web** tab.
2. Click the big green **Reload** button.
3. Click your website link at the top: `yourname.pythonanywhere.com`.

Your guestbook is now live on the internet. Sign it, then send the link
to a friend and watch their signature show up on YOUR screen. That's the
whole point of a server — the data is in one shared place, not stuck on
one computer.

---

## When you change your code later

1. Push your changes to GitHub from your computer (or edit on GitHub).
2. In the PythonAnywhere **Bash console**:

   ```bash
   cd flask-guestbook
   git pull
   ```

3. Go to the **Web** tab and click **Reload**.

Your changes are now live. Reload is the "publish" button — nothing
updates until you click it.

---

## Things that trip people up

- **Free accounts have a whitelist.** Your app can't call random other
  websites (like a weather API) on the free plan. Our guestbook doesn't
  need to, so we're fine.
- **You only get one web app** on the free plan. Make it count.
- **Your database is a file** (`guestbook.db`) that lives on
  PythonAnywhere. It sticks around between visits — that's good! But if
  you delete it in a console, the signatures are gone.
- **CPU is limited** (about 100 seconds of hard work a day). A guestbook
  uses almost none, so don't worry unless you build something huge.
