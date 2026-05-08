# Node.js Interview Preparation  
## Chunk 1 — Questions 1 to 20

---

# 📚 Table of Contents

| No. | Question |
|---|---|
| 1 | What is Node.js? Why is it used? |
| 2 | Explain the event-driven architecture in Node.js |
| 3 | What is the event loop and how does it work? |
| 4 | What are microtasks and macrotasks in Node.js? |
| 5 | Difference between process.nextTick(), setImmediate(), and setTimeout() |
| 6 | How does Node.js handle asynchronous operations? |
| 7 | What is the difference between blocking and non-blocking code? |
| 8 | What are streams in Node.js? Types of streams? |
| 9 | How does Node.js handle child processes? |
| 10 | What is the purpose of the cluster module? |
| 11 | Difference between CommonJS and ES Modules |
| 12 | How do you create and export a custom module? |
| 13 | What is package.json and important fields? |
| 14 | Difference between dependencies and devDependencies |
| 15 | How do you handle environment variables in Node.js? |
| 16 | Difference between callbacks, promises, and async/await |
| 17 | How do you handle errors in async functions? |
| 18 | Difference between Promise.all() and Promise.race() |
| 19 | What happens if you forget await in an async function? |
| 20 | Explain libuv in Node.js |

---

# 1. What is Node.js? Why is it used?

## Answer

Node.js is an open-source JavaScript runtime environment built on Chrome’s V8 engine.

It allows JavaScript to run outside the browser.

It is mainly used for:
- Backend APIs
- Real-time applications
- Streaming applications
- Microservices
- Automation tools

---

## Why Node.js is Popular

### 1. Non-blocking I/O
Node.js handles multiple requests simultaneously without blocking execution.

### 2. Fast Execution
Uses Google's V8 engine which compiles JavaScript into machine code.

### 3. Single Language
Frontend and backend both use JavaScript.

### 4. Event-Driven Architecture
Efficient for scalable applications.

---

## Example

```js
const http = require("http");

http.createServer((req, res) => {
  res.end("Hello Node.js");
}).listen(3000);
```

---

# 2. Explain the event-driven architecture in Node.js

## Answer

Node.js follows an event-driven architecture where actions trigger events, and listeners respond to those events.

Instead of waiting for one task to finish before starting another, Node.js registers callbacks and continues execution.

---

## Key Components

| Component | Description |
|---|---|
| Event Loop | Handles async tasks |
| Event Queue | Stores pending events |
| EventEmitter | Emits and listens to events |

---

## Example

```js
const EventEmitter = require("events");

const emitter = new EventEmitter();

emitter.on("login", (user) => {
  console.log(`${user} logged in`);
});

emitter.emit("login", "Ashish");
```

---

## Output

```txt
Ashish logged in
```

---

# 3. What is the event loop and how does it work?

## Answer

The event loop is the core mechanism that allows Node.js to perform non-blocking asynchronous operations.

Even though JavaScript is single-threaded, Node.js can handle multiple operations concurrently using the event loop.

---

## Event Loop Phases

| Phase | Purpose |
|---|---|
| Timers | Executes setTimeout/setInterval |
| Pending Callbacks | Executes deferred callbacks |
| Idle/Prepare | Internal operations |
| Poll | Retrieves new I/O events |
| Check | Executes setImmediate |
| Close Callbacks | Handles close events |

---

## Example

```js
console.log("Start");

setTimeout(() => {
  console.log("Timeout");
}, 0);

Promise.resolve().then(() => {
  console.log("Promise");
});

console.log("End");
```

---

## Output

```txt
Start
End
Promise
Timeout
```

---

# 4. What are microtasks and macrotasks in Node.js?

## Answer

Node.js divides async tasks into:
- Microtasks
- Macrotasks

---

## Microtasks

Executed immediately after current execution completes.

### Examples
- Promise.then()
- process.nextTick()

---

## Macrotasks

Executed in later event loop phases.

### Examples
- setTimeout()
- setInterval()
- setImmediate()

---

## Priority

```txt
Current Code
→ process.nextTick
→ Promise Microtasks
→ Macrotasks
```

---

## Example

```js
setTimeout(() => console.log("timeout"));

Promise.resolve().then(() => console.log("promise"));

process.nextTick(() => console.log("nextTick"));
```

---

## Output

```txt
nextTick
promise
timeout
```

---

# 5. Difference between process.nextTick(), setImmediate(), and setTimeout()

## Answer

| Method | Executes |
|---|---|
| process.nextTick | Before event loop continues |
| setImmediate | Check phase |
| setTimeout(fn,0) | Timer phase |

---

## Example

```js
setTimeout(() => console.log("timeout"), 0);

setImmediate(() => console.log("immediate"));

process.nextTick(() => console.log("nextTick"));
```

---

## Expected Output

```txt
nextTick
immediate
timeout
```

---

# 6. How does Node.js handle asynchronous operations?

## Answer

Node.js uses:
- Event Loop
- Callback Queue
- Worker Threads (libuv thread pool)

Heavy I/O operations are delegated to the system kernel or thread pool.

---

## Flow

```txt
Request
→ Node APIs
→ Background Thread
→ Callback Queue
→ Event Loop
→ Execution
```

---

## Example

```js
const fs = require("fs");

fs.readFile("demo.txt", "utf8", (err, data) => {
  console.log(data);
});

console.log("Reading...");
```

---

## Output

```txt
Reading...
<File Content>
```

---

# 7. Difference between blocking and non-blocking code

## Blocking Code

Stops execution until task completes.

```js
const data = fs.readFileSync("demo.txt");
console.log(data.toString());
```

---

## Non-Blocking Code

Does not stop execution.

```js
fs.readFile("demo.txt", (err, data) => {
  console.log(data.toString());
});

console.log("Continue...");
```

---

## Key Difference

| Blocking | Non-Blocking |
|---|---|
| Synchronous | Asynchronous |
| Slower scalability | Better scalability |
| Waits for task | Continues execution |

---

# 8. What are streams in Node.js? Types?

## Answer

Streams process data piece-by-piece instead of loading everything into memory.

Useful for:
- Large files
- Video streaming
- Real-time processing

---

## Types of Streams

| Type | Description |
|---|---|
| Readable | Read data |
| Writable | Write data |
| Duplex | Read + Write |
| Transform | Modify data |

---

## Example

```js
const fs = require("fs");

const readStream = fs.createReadStream("input.txt");

readStream.on("data", chunk => {
  console.log(chunk.toString());
});
```

---

# 9. How does Node.js handle child processes?

## Answer

Node.js can create subprocesses using the `child_process` module.

Useful for:
- Running shell commands
- CPU-intensive tasks
- Python scripts
- Background jobs

---

## Methods

| Method | Description |
|---|---|
| exec | Runs full command |
| spawn | Streams data |
| fork | Creates Node.js child process |

---

## Example

```js
const { exec } = require("child_process");

exec("node -v", (err, stdout) => {
  console.log(stdout);
});
```

---

# 10. What is the purpose of the cluster module?

## Answer

Cluster module helps utilize multiple CPU cores.

Since Node.js is single-threaded, clustering creates multiple worker processes.

---

## Benefits

- Better scalability
- Improved performance
- Load distribution

---

## Example

```js
const cluster = require("cluster");
const os = require("os");

if (cluster.isMaster) {
  for (let i = 0; i < os.cpus().length; i++) {
    cluster.fork();
  }
} else {
  console.log(`Worker ${process.pid}`);
}
```

---

# 11. Difference between CommonJS and ES Modules

| Feature | CommonJS | ES Modules |
|---|---|---|
| Syntax | require | import |
| Export | module.exports | export |
| Loading | Synchronous | Asynchronous |
| Default in Node | Yes | Modern standard |

---

## CommonJS

```js
const math = require("./math");
```

---

## ES Module

```js
import math from "./math.js";
```

---

# 12. How do you create and export a custom module?

## math.js

```js
function add(a, b) {
  return a + b;
}

module.exports = add;
```

---

## app.js

```js
const add = require("./math");

console.log(add(2, 3));
```

---

# 13. What is package.json and important fields?

## Answer

`package.json` stores project metadata and dependencies.

---

## Important Fields

| Field | Purpose |
|---|---|
| name | Project name |
| version | Version |
| scripts | Commands |
| dependencies | Production packages |
| devDependencies | Development packages |
| main | Entry file |

---

## Example

```json
{
  "name": "node-app",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "start": "node index.js"
  }
}
```

---

# 14. Difference between dependencies and devDependencies

| dependencies | devDependencies |
|---|---|
| Needed in production | Needed only in development |
| Express | Jest |
| Axios | Nodemon |

---

## Install

### dependencies

```bash
npm install express
```

### devDependencies

```bash
npm install jest --save-dev
```

---

# 15. How do you handle environment variables in Node.js?

## Answer

Environment variables store sensitive configuration.

Examples:
- API Keys
- DB credentials
- Secrets

---

## Using dotenv

### Install

```bash
npm install dotenv
```

---

## .env

```env
PORT=5000
DB_URL=mongodb://localhost/test
```

---

## Usage

```js
require("dotenv").config();

console.log(process.env.PORT);
```

---

# 16. Difference between callbacks, promises, and async/await

| Type | Description |
|---|---|
| Callback | Function passed into another function |
| Promise | Represents future completion |
| async/await | Cleaner promise syntax |

---

## Callback

```js
fs.readFile("a.txt", (err, data) => {});
```

---

## Promise

```js
fetch(url)
  .then(res => res.json())
  .then(data => console.log(data));
```

---

## Async/Await

```js
async function getData() {
  const res = await fetch(url);
  const data = await res.json();
}
```

---

# 17. How do you handle errors in async functions?

## Using try/catch

```js
async function getData() {
  try {
    const data = await fetch(url);
  } catch (err) {
    console.error(err);
  }
}
```

---

## Express Async Error

```js
app.get("/", async (req, res, next) => {
  try {
    const data = await service();
    res.json(data);
  } catch (err) {
    next(err);
  }
});
```

---

# 18. Difference between Promise.all() and Promise.race()

| Method | Behavior |
|---|---|
| Promise.all | Waits for all promises |
| Promise.race | Returns first completed promise |

---

## Promise.all

```js
await Promise.all([p1, p2, p3]);
```

---

## Promise.race

```js
await Promise.race([p1, p2, p3]);
```

---

# 19. What happens if you forget await in an async function?

## Answer

Without `await`, the promise remains unresolved.

---

## Example

```js
async function test() {
  const data = fetch(url);

  console.log(data);
}
```

---

## Output

```txt
Promise { <pending> }
```

---

## Correct Version

```js
const data = await fetch(url);
```

---

# 20. Explain libuv in Node.js

## Answer

libuv is a C library used internally by Node.js.

It provides:
- Event loop
- Thread pool
- Async I/O handling
- File system operations
- Networking

---

## Why Important

JavaScript itself cannot perform async filesystem/network operations.

libuv enables Node.js to handle them efficiently.

---

## Thread Pool

Default size:
```txt
4 threads
```

Can be increased using:

```bash
UV_THREADPOOL_SIZE=8
```

---

# ✅ End of Chunk 1