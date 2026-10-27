# Roadmap: Python Engineer → Full-Stack → Machine Learning Engineer

Built on top of `Python_Master_Roadmap_Beginner_to_Advanced.pdf`, with the same topics in a sharper order.
**Goal:** a developer who can build, explain and debug real software **without AI help**.

- **Pace:** ~24 weeks at ~4–5 focused hours/day, 6 days/week. Starts from absolute basics.
- **You move on when you pass a gate, not when the calendar says so.** If a week takes 10 days, it takes 10 days.
- **Every stage ends with a milestone project** that proves you've mastered it. You build it from an empty folder, with no AI and no tutorial.
- **Algorithms run alongside everything** (see `ALGORITHMS.md`): explained in plain language, done by hand first, then coded.

---

## How every topic is learned (the 5-step loop)

| Step | What you do | Why it works |
|---|---|---|
| **1. Watch** | One lesson, **without coding along** | Builds the mental picture |
| **2. Predict** | Before running any example, guess the output. Wrong guess = the thing to learn | Forces you to think, not copy |
| **3. Build** | Exercises in `weekNN/` until tests pass. Hints from Claude, **never solutions** | You learn by struggling and fixing |
| **4. Break** | Feed your code bad input on purpose; read the error; fix it | Debugging is half the job |
| **5. Explain** | Explain it out loud in 60 seconds, then in writing (`INTERVIEW_BANK.md`) | If you can't explain it, you don't know it yet |

### Daily template (~4.5 h)
| Time | Activity |
|---|---|
| 20 min | **Warm-up:** re-solve one older exercise from a blank file, from memory |
| 40 min | **Learn:** the day's video/reading (from the week's `README.md`) |
| 2 h | **Build:** exercises / project. Commit to Git whenever something works |
| 30 min | **Algorithm practice** (from week 3; see below) |
| 30 min | **Explain:** interview questions out loud + in writing |
| 10 min | **Log** in `PROGRESS.md`: learned / confused / mistakes |

Day 7 = rest. Every Monday: `Monday quiz` (spaced review). Every Saturday: `mock interview week N`.

### The "code without AI" rules
1. **Turn off Copilot and all AI autocomplete** in VS Code. Keep it off at least until week 12; ideally you never need it while learning.
2. Claude in this folder gives **hints, reviews, quizzes and explanations**, but never your solution.
3. Use the **official docs** as your main reference (docs.python.org, fastapi.tiangolo.com, react.dev, scikit-learn.org). Reading docs is a core developer skill.
4. **The No-AI proof:** at each milestone, rebuild a core piece of the project **from a blank file, offline, timed**. Passing that is your proof that you can code without AI.
5. Never paste code you can't explain line by line.

---

## STAGE 1: Python Foundations (Weeks 1–5)

| Week | Learn | Watch / read | Build |
|---|---|---|---|
| **1** | How programs run, variables, types, operators, f-strings, input/output, conditions, loops, strings | CS50P lectures 0–2 | `week01/` (3 exercise files, auto-tested) + **Guessing Game & Calculator** |
| **2** | Lists, tuples, dicts, sets, comprehensions, functions, `*args/**kwargs`, scope, recursion, **exceptions** | Corey Schafer beginner series · CS50P lecture 3 · `ALGORITHMS.md`: Big-O, Recursion, Hash tables | `week02/` + **CLI Expense Tracker** |
| **3** | Files, `with`, `pathlib`, CSV, JSON, exceptions in depth, modules & packages, `__name__`, venv/pip, `logging`, **pytest basics** | CS50P lectures 4–6 (Libraries, Unit Tests, File I/O) | Expense Tracker v2: saves to JSON, split into modules, with tests |
| **4** | OOP: classes, `__init__`, methods, properties, inheritance vs composition, dunder methods, `@dataclass`, `Enum`, ABCs | CS50P lecture 8 · Corey Schafer OOP series (6 videos) | **Library Management System** (Book, Member, Loan, Library) with tests |
| **5** | Pythonic code: iterators, generators, `yield`, decorators, closures, lambda, `map/filter/zip/enumerate`, type hints, `collections`, `itertools`, `functools`, `datetime`, regex basics | CS50P lectures 7 & 9 · Corey Schafer: generators, decorators | **CSV Data Analyzer CLI**: reads a large CSV with a generator, computes stats, writes a report, has `argparse` options |

### 🏁 Milestone 1: "I can write Python": **Personal Finance Manager (CLI)**
Proves: data structures, functions, OOP, files, errors, testing, clean modules.
- Accounts, transactions, categories, budgets (OOP with dataclasses)
- Saves to JSON, imports bank CSVs, monthly reports
- Never crashes on bad input; custom exceptions
- ≥ 25 pytest tests; split into a package; `argparse` CLI
- **No-AI proof:** rebuild the transaction import + monthly report from a blank file in 60 min.

---

## STAGE 2: Algorithms, Data Structures & Engineering (Weeks 6–7)

| Week | Learn | Build |
|---|---|---|
| **6** | `ALGORITHMS.md` Parts 1–4: Big-O, linear/binary search, the 5 sorts, two pointers, sliding window, stacks, queues, hash-map patterns | `algos/` package: implement every algorithm with tests + **sorting benchmark** (time each sort on growing inputs, plot the curves with matplotlib) |
| **7** | Linked lists, trees/BST, heaps, graphs, BFS, DFS, **Dijkstra**, intro to dynamic programming & greedy · Engineering: Git branching, Ruff, mypy, VS Code debugger, refactoring, env vars | **City Route Finder**: load a road network from CSV, find shortest routes with BFS and Dijkstra, compare them (the routing core of your MOBIUS AI capstone) |

**Running track from now on, the daily algorithm practice:** 1 problem/day from the **NeetCode 150** list (start with Arrays & Hashing, Two Pointers, Sliding Window, Stack). Process: 20 min trying alone → if stuck, watch only the first half of NeetCode's explanation → code it yourself → re-solve it 3 days later from memory.

### 🏁 Milestone 2: "I can think algorithmically"
- Route Finder finished, tested, and on GitHub with a README explaining the algorithms and their Big-O
- 40 NeetCode problems solved, 10 of them re-solved from memory a week later
- **No-AI proof:** from a blank file, in 45 min: binary search, merge sort, BFS on a grid. All working, explained out loud.

---

## STAGE 3: Backend & APIs (Weeks 8–11)

| Week | Learn | Watch / read | Build |
|---|---|---|---|
| **8** | How the web works: client/server, DNS, HTTP methods, status codes, headers, JSON, REST, CORS · **FastAPI**: routes, path/query params, Pydantic, response models, errors, dependencies, OpenAPI docs | MDN "HTTP overview" · FastAPI official tutorial · **freeCodeCamp "Python API Development" (Sanjeev Thiyagarajan, ~19 h)**, which runs through weeks 8–11 | Notes API (in-memory) with full CRUD |
| **9** | **SQL first:** SELECT, WHERE, JOIN, GROUP BY, indexes, transactions · then PostgreSQL, SQLAlchemy 2.x, Alembic migrations | SQLBolt (interactive) · PostgreSQL tutorial | Notes API on PostgreSQL: users, tags, pagination, search |
| **10** | Auth & quality: password hashing, JWT, OAuth2 concepts, protected routes, permissions, input validation, consistent errors, logging, integration tests, basic web security (SQL injection, XSS, CORS) | FastAPI "Security" docs | Secure Notes API with login, ownership rules and tests |
| **11** | Consuming APIs with `httpx`, timeouts, retries, async/await, background tasks, caching with Redis · **Docker basics**: Dockerfile, Docker Compose (API + Postgres) | TechWorld with Nana: Docker tutorial | Weather/News aggregator: calls 2 external APIs concurrently, caches results, serves them via FastAPI, runs in Docker Compose |

### 🏁 Milestone 3: "I can build a backend": **Job Application Tracker API**
Proves: REST design, SQL, auth, testing, Docker.
- Users, companies, applications, interview stages, notes (relational schema with migrations)
- JWT auth; users see only their own data
- Filtering, sorting, pagination; stats endpoint (applications per stage, per month)
- ≥ 30 tests (unit + API), Docker Compose, deployed with CI (GitHub Actions)
- **No-AI proof:** from a blank folder in 90 min: FastAPI + SQLAlchemy app with 2 related tables, CRUD and tests.

> 🎯 You can start applying for **Python / backend intern** roles here, with this project as proof.

---

## STAGE 4: Frontend & Full-Stack (Weeks 12–15)

| Week | Learn | Watch / read | Build |
|---|---|---|---|
| **12** | HTML (semantic, forms, accessibility) + CSS (box model, Flexbox, Grid, responsive, variables) | MDN Learn · Kevin Powell (YouTube) for CSS | Responsive portfolio page + dashboard layout, no frameworks |
| **13** | JavaScript: variables, functions, arrays/objects, `map/filter/reduce`, DOM, events, promises, `async/await`, `fetch`, modules · TypeScript basics | javascript.info · MDN JS guide | Plain-JS frontend for your Notes API (login, list, create, delete) |
| **14** | React: components, JSX, props, state, effects, forms, lists, loading/error states, routing, custom hooks · Tailwind CSS | **react.dev/learn** (official, interactive) | React version of the Notes frontend |
| **15** | Full-stack integration: auth across front & back, env vars, CORS, file uploads, production builds, deploying frontend (Vercel/Netlify) + backend (Render/Railway) + database | | Connect your Milestone 3 API to a React UI and deploy it |

### 🏁 Milestone 4: "I can ship a full product": **Job Tracker, full-stack**
Proves: frontend + backend + database + deployment.
- React + TypeScript frontend on top of your Milestone 3 API
- Sign-up/login, kanban board of applications by stage, search, filters, charts of your stats
- Every screen handles loading, empty and error states; responsive on phone
- Deployed live with a public URL and CI running tests on every push
- **No-AI proof:** from a blank folder in 90 min: a React page that fetches from an API, shows a list with search, and has a working create form.

> 🎯 You can apply for **full-stack junior** roles here.

---

## STAGE 5: Machine Learning, from the math up (Weeks 16–22)

| Week | Learn | Watch / read | Build |
|---|---|---|---|
| **16** | Math with code: vectors, matrices, dot products, derivatives, gradients, probability, mean/variance/std, distributions | 3Blue1Brown: *Essence of Linear Algebra* + *Essence of Calculus* · StatQuest statistics basics | Implement the vector/matrix operations in pure Python, then the same in NumPy, and compare speed |
| **17** | **NumPy** (arrays, shapes, broadcasting, vectorization) + **pandas** (DataFrames, cleaning, groupby, merge, time series) + Matplotlib/Seaborn | Kaggle Learn: *Pandas* + *Data Visualization* · Corey Schafer pandas series | **EDA project:** analyze a real traffic or taxi dataset (peak hours, hotspots, weekday patterns) in a clean notebook |
| **18** | **ML from scratch in NumPy:** linear regression + gradient descent, logistic regression, KNN, K-means | Andrew Ng *Machine Learning Specialization*, Course 1 (audit free) · StatQuest | `ml_from_scratch/`: each algorithm as a class with `fit()`/`predict()`, tested against scikit-learn's results |
| **19** | **scikit-learn:** train/val/test, baselines, decision trees, random forests, gradient boosting (XGBoost/LightGBM), scaling, encoding, Pipelines, cross-validation, hyperparameter tuning | scikit-learn user guide · Andrew Ng Course 2 · *Hands-On ML* (Géron), ch. 2–7 | House-price or taxi-fare predictor with a full Pipeline |
| **20** | Evaluation & features: MAE/RMSE/R², precision/recall/F1/ROC-AUC, overfitting, **data leakage**, feature engineering, time-series features (lags, rolling windows), chronological splits | StatQuest · Kaggle Learn: *Intermediate ML*, *Feature Engineering* | Model comparison report: baseline vs 3 models, with honest error analysis |
| **21** | **Deep learning:** neural networks, backprop, PyTorch tensors, training loops, optimizers, regularization, CNN basics | **Andrej Karpathy: *Neural Networks: Zero to Hero*** (lectures 1–3) · PyTorch tutorials | Micrograd-style autograd from scratch (following Karpathy, then rebuilt alone) + an image classifier in PyTorch |
| **22** | **Serving ML:** save/load models, consistent preprocessing, a FastAPI `/predict` endpoint, validation, model versioning, Docker | FastAPI docs + your own Stage 3 code | Deploy your Week 19/20 model as an API |

### 🏁 Milestone 5: "I am an ML engineer": **Traffic Speed Forecaster**
Proves: data work, modelling, honest evaluation, deployment.
- Clean a real traffic dataset; engineer time features (hour, weekday, lags, rolling means)
- Naive baseline → linear model → gradient boosting → small neural net, with chronological validation
- A written report: which model won, by how much, and **where it fails**
- Best model served via FastAPI in Docker, with tests and monitoring of latency + input ranges
- **No-AI proof:** from a blank notebook in 60 min: load a CSV, clean it, build a baseline + one model with a correct split, and report MAE.

---

## STAGE 6: Applied AI + Capstone (Weeks 23–24+)

| Week | Learn | Build |
|---|---|---|
| **23** | LLM apps: calling LLM APIs, structured outputs, tool calling, **embeddings**, **RAG**, evaluating outputs, prompt injection | A "chat with your documents" app (RAG) built with your own backend + React UI |
| **24+** | **MOBIUS AI capstone** (PDF section 14), combining everything: traffic forecasting model + route finder (Dijkstra with predicted traffic weights) + FastAPI + PostgreSQL + React map dashboard + an AI assistant that explains congestion and suggests routes | Deployed, documented, with measured results |

### 🏁 Final milestone: "I can build an AI product end to end"
You can demo MOBIUS AI, defend every design choice, and rebuild any part of it without AI.

---

## Interview readiness checkpoints

| After | You can honestly apply for | Proof on GitHub |
|---|---|---|
| Milestone 3 (wk 11) | Python / backend intern | Job Tracker API, Route Finder, 40+ NeetCode problems |
| Milestone 4 (wk 15) | Full-stack junior | Deployed Job Tracker full-stack app |
| Milestone 5 (wk 22) | ML engineer intern / junior | Traffic Forecaster + ML-from-scratch repo |
| Capstone | Strong junior / ML + full-stack engineer | MOBIUS AI |

> **Honest calibration:** "L2 engineer" usually means 1–3 years of shipping software in a team. In ~24 weeks of serious work you can reach **strong-junior skill level with projects that prove it**, and an interviewer will see the difference immediately. The rest comes from your first job.

---

## What changed from the PDF (and why)
1. **Algorithms got a full stage and a daily track** (`ALGORITHMS.md` + NeetCode). The PDF only touched them in part of week 9. Interviews test them, and they train your problem-solving.
2. **ML algorithms are coded from scratch in NumPy before you use scikit-learn,** so you understand what `.fit()` actually does.
3. **One milestone project per stage, with a No-AI proof,** so every stage ends with evidence that you can code alone.
4. **Testing and Git from week 1–3, Docker in week 11** (the PDF had them in weeks 8 and 28).
5. **Explain-out-loud practice, mock interviews and spaced-review quizzes**, the part that went wrong in your interview.
6. **Removed:** the cybersecurity focus from my first version. Basic web security stays, because every backend developer needs it.
