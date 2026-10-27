# My Developer Rebuild 🔧

Started 2026-10-27. Goal: become a **Python + full-stack + machine-learning engineer** who can build, explain and debug real software **without AI help**.

## Files in this folder
| File | What it is |
|---|---|
| `ROADMAP.md` | The full plan: 6 stages, ~24 weeks, one milestone project per stage. **Read first.** |
| `ALGORITHMS.md` | Every algorithm explained simply: everyday picture, real uses, worked by hand, speed, exercise |
| `week01/`, `week02/` | Day-by-day guide (`README.md`), exercises with automatic tests, milestone project |
| `INTERVIEW_BANK.md` | Questions to answer out loud + in writing, starting with the 4 from the interview |
| `PROGRESS.md` | Daily log, gates passed, mistake journal, weak spots |
| `CLAUDE.md` | Makes Claude act as your tutor here: hints and explanations, never your solutions |
| `Python_Master_Roadmap_...pdf` | The original roadmap (topic reference) |

## Day 0 setup (do it yourself; this IS the first lesson)

Open this folder in VS Code → Terminal → run these one at a time, and make sure you understand each:

```powershell
python --version                      # should say 3.14.x
python -m venv .venv                  # create a virtual environment (an isolated box for packages)
.venv\Scripts\Activate.ps1            # activate it; the prompt now shows (.venv)
#  If PowerShell blocks scripts, run once:  Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
python -m pip install pytest          # install the test runner
pytest week01 -v                      # lots of red FAILED. That's your starting line.
```

Then Git (watch "Git and GitHub for Beginners" by freeCodeCamp first if Git is new):
```powershell
git init
git add .
git commit -m "Day 0: start of my developer rebuild"
# Create a PRIVATE repo on github.com named dev-rebuild, then:
git remote add origin https://github.com/<your-username>/dev-rebuild.git
git branch -M main
git push -u origin main
```

In VS Code: **turn off GitHub Copilot / AI inline suggestions.**

Then open `week01/README.md` and start Day 1.

## Using Claude as your tutor (open Claude Code in this folder)
| Say this | You get |
|---|---|
| `what's next` | The exact next step: what to watch, read and build |
| `explain binary search` | Plain-language explanation, worked by hand, then questions to check you got it |
| `hint for compress` | One nudge, not the answer |
| `review my ex02` | A senior-engineer code review |
| `grade my answer to exception handling` | Score + what's missing |
| `Monday quiz` | Spaced-repetition quiz on recent weeks |
| `mock interview week 2` | Interview practice, one question at a time |
| `review my week 1` | Honest check: did I pass the gate? |
| `generate week 3` | Next week's guide, exercises, tests and project |
| `no-AI proof` | Timed blank-file challenge for your current milestone |
