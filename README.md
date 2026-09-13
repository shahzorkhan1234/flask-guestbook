# Class Guestbook 📖

A tiny website with a **Python backend**, an **HTML/CSS front end**, and a
**real database**. Anyone who signs it is saved for everyone to see — because
the data lives on the server, not in one browser.

## The four parts

| File | Job |
|------|-----|
| `templates/index.html` | The page people see (front end) |
| `static/style.css` | How the page looks (front end) |
| `app.py` | The Python server: routes + database (back end) |
| `guestbook.db` | The database file, made automatically (storage) |

## Run it on your own computer

```bash
pip install -r requirements.txt
python app.py
```

Then open the link it prints (usually http://127.0.0.1:5000).

## How the pieces talk to each other

1. You open `/` → `app.py` reads the database → fills in `index.html` → browser shows it.
2. You submit the form → browser sends data to `/sign` → `app.py` saves it → page reloads.

## Deploy it live (Render)

1. Push this folder to a GitHub repo.
2. Open [Render's Git provider instructions](https://render.com/docs/git-provider) and sign in to Render.
3. When Render asks to connect GitHub, choose **Connect GitHub** and authorize Render to access your GitHub account.
4. If GitHub asks which repositories Render can access, choose **Only select repositories** and add this guestbook repository, or choose **All repositories** if that is appropriate for your account.
5. Return to Render and choose **New → Web Service**. Select **Connect a repository** and choose this GitHub repository.
6. If the repository does not appear, open your Render account settings, reconnect GitHub, and update the repository access permissions.
7. Build command: `pip install -r requirements.txt`
8. Start command: `gunicorn app:app`
9. Deploy. You get a public URL to share.

## Expand it with GitHub Copilot — try these prompts

- "Add a delete button next to each signature"
- "Add a column to store the date and time each person signed"
- "Only show the 10 most recent signatures"
- "Add a text box to search signatures by name"
- "Give each signature a random background color"

Change one thing, run it, see what happens. That's the whole game.
