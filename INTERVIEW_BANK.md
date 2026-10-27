# Interview Bank

**How to use:** For each question:
1. Answer **out loud** as if to an interviewer (record yourself on your phone if you can).
2. Write your answer below the question in your own words, **with a code example from your own exercises**.
3. Ask Claude: *"Grade my answer to <question>"*.
4. Mark it: ⬜ not yet · 🟨 shaky · ✅ solid. Re-answer 🟨 ones in the Monday quiz.

A strong answer has 3 parts: **what it is → why/when you'd use it → a short example (ideally from your own code).**

---

## ⭐ The four questions from the interview (master these by the end of Week 2; revisit in Week 8)

### 1. What is exception handling in Python? ⬜
*A strong answer covers:* exceptions are objects raised when something goes wrong at runtime · `try` / `except SpecificError` / `else` (runs if no error) / `finally` (always runs: cleanup) · catch **specific** exceptions, not a bare `except:` · `raise` to signal errors yourself · custom exceptions by subclassing `Exception` · example: parsing user input, reading a file.

My answer:

### 2. What's the difference between an error and an exception? How do you handle errors in a real program? ⬜
*A strong answer covers:* syntax errors (code can't run, fix the code) vs runtime exceptions (can be handled) · expected failures (bad user input, missing file, network timeout) → handle them · programmer bugs → let them crash loudly, then fix them · log errors (`logging`), give useful messages, fail safely, retry with backoff for network issues · validate input early.

My answer:

### 3. What is an API? What is a REST API? ⬜
*A strong answer covers:* API = a contract for how one program talks to another · web/REST API: a client sends HTTP requests (method + URL + headers + body) and the server returns a status code + JSON · resources as URLs (`/users/42`), methods as actions (GET/POST/PUT/PATCH/DELETE) · stateless · status codes (200, 201, 400, 401, 404, 500) · example: calling a weather API with `requests`, or an endpoint you built in FastAPI.

My answer:

### 4. What is the backend? What happens when you open a website? ⬜
*A strong answer covers:* frontend = what runs in the browser; backend = server-side code that handles requests, business logic, auth, and talks to the database · request flow: DNS lookup → TCP/TLS connection → HTTP request → server/framework routes it → logic + DB query → response → browser renders it · examples of backend tech: Python + FastAPI/Django, PostgreSQL, Redis.

My answer:

---

## Week 1: Basics
- How does Python run your code? What does "interpreted" mean? ⬜
- What are Python's basic data types? ⬜
- What's the difference between `/`, `//` and `%`? ⬜
- What are truthy and falsy values? Name 5 falsy ones. ⬜
- `for` vs `while`: when do you use each? `break` vs `continue` vs `pass`? ⬜
- Strings are immutable. What does that mean? ⬜

## Week 2: Collections, functions, errors
- Mutable vs immutable: give 2 examples of each. ⬜
- List vs tuple vs set vs dict: when do you use each? ⬜
- `==` vs `is`? ⬜
- `return` vs `print`? ⬜
- What are `*args` and `**kwargs`? ⬜
- What is a list comprehension? Write one that squares even numbers. ⬜
- What is recursion? What happens without a base case? ⬜
- Why is `def f(items=[])` a bug? ⬜

## Week 3: Files, modules, testing
- What does the `with` statement do? What is a context manager? ⬜
- When does `else` run in a try block? When does `finally` run? ⬜
- How do you create a custom exception, and why would you? ⬜
- What does `if __name__ == "__main__":` do? ⬜
- What is a virtual environment and why use one? ⬜
- Module vs package? ⬜
- What is a unit test? What makes a good one? ⬜

## Week 4: OOP
- Explain the 4 pillars of OOP with examples from your code. ⬜
- Class vs instance variables? What is `self`? ⬜
- Inheritance vs composition: which do you prefer and why? ⬜
- `__str__` vs `__repr__`? ⬜
- What is a dataclass? What is `@property` for? ⬜

## Week 5: Pythonic Python
- Iterable vs iterator? ⬜
- What is a generator, and why does it save memory? ⬜
- What is a decorator? Write a timing decorator. ⬜
- What is a closure? ⬜
- What is a lambda? When should you NOT use one? ⬜
- Why use type hints if Python doesn't enforce them? ⬜

## Weeks 6–7: Algorithms & data structures
- What is Big-O? Why does O(n²) matter on large data? ⬜
- Why is `x in set` faster than `x in list`? How does a hash table work? ⬜
- Explain binary search. What is its precondition? ⬜
- Merge sort vs quick sort: speed, memory, worst case? ⬜
- Stack vs queue, with a real use of each. ⬜
- BFS vs DFS: when do you use each? ⬜
- How does Dijkstra's algorithm work? Why does it need a priority queue? ⬜
- What is dynamic programming? Give an example. ⬜
- Shallow vs deep copy? ⬜
- What is the GIL? Threading vs multiprocessing vs asyncio? ⬜
- Git: merge vs rebase? What is a pull request? ⬜

## Weeks 8–11: Backend & APIs
- Walk through the structure of an HTTP request and response. ⬜
- GET/POST/PUT/PATCH/DELETE: what each does. PUT vs PATCH? Idempotency? ⬜
- 200 vs 201 vs 204? 400 vs 422? 401 vs 403? ⬜
- What is CORS and why does it exist? ⬜
- What does Pydantic do in FastAPI? ⬜
- SQL vs NoSQL? What is an index and what does it cost? ⬜
- INNER vs LEFT JOIN? ⬜
- What is a transaction? What does ACID mean? ⬜
- What is an ORM? Pros and cons? ⬜
- What is SQL injection and how do you prevent it? ⬜
- Authentication vs authorization? How does JWT work? ⬜
- How should passwords be stored? ⬜
- Sync vs async: when does async help, and when doesn't it? ⬜
- What is caching? What's hard about it? ⬜
- What is Docker? Image vs container? ⬜

## Weeks 12–15: Frontend & full-stack
- What happens when you type a URL into the browser? ⬜
- Flexbox vs Grid? ⬜
- `let` vs `const` vs `var`? ⬜
- What is a Promise? What does `await` do? ⬜
- What is the DOM? ⬜
- React props vs state? When does a component re-render? ⬜
- What does `useEffect` do? What's the dependency array for? ⬜
- What is CI/CD? What does your pipeline do? ⬜

## Weeks 16–22: Machine learning
- Supervised vs unsupervised learning? Regression vs classification? ⬜
- Explain gradient descent to a non-technical person. What is the learning rate? ⬜
- Why a train/validation/test split? Why a chronological split for time series? ⬜
- Bias vs variance? How do you detect and fix overfitting? ⬜
- What is data leakage? Give an example. ⬜
- Precision vs recall: when do you care about which? ⬜
- Why scale features? Which models need it and which don't? ⬜
- Decision tree vs random forest vs gradient boosting? ⬜
- How does K-means work? How do you choose k? ⬜
- What is backpropagation? ⬜
- What is an activation function, and why do we need non-linearity? ⬜
- How do you deploy an ML model behind an API? What can go wrong in production? ⬜

## Week 23+: Applied AI
- What are embeddings? ⬜
- What is RAG and why use it instead of fine-tuning? ⬜
- What is attention / a transformer, at a high level? ⬜
- What is prompt injection, and how do you defend against it? ⬜
