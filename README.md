# Node.js Interview Preparation  
---

# 📚 Table of Contents

| No. | Question |
|---|---|
| 1 | [What is Node.js? Why is it used?](#1-what-is-nodejs-why-is-it-used) |
| 2 | [Explain the event-driven architecture in Node.js](#2-explain-the-event-driven-architecture-in-nodejs) |
| 3 | [What is the event loop and how does it work?](#3-what-is-the-event-loop-and-how-does-it-work) |
| 4 | [What are microtasks and macrotasks in Node.js?](#4-what-are-microtasks-and-macrotasks-in-nodejs) |
| 5 | [Difference between processnexttick setImmediate and setTimeout](#5-difference-between-processnexttick-setimmediate-and-settimeout) |
| 6 | [How does Node.js handle asynchronous operations?](#6-how-does-nodejs-handle-asynchronous-operations) |
| 7 | [Difference between blocking and non-blocking code](#7-difference-between-blocking-and-non-blocking-code) |
| 8 | [What are streams in Node.js?](#8-what-are-streams-in-nodejs-types) |
| 9 | [How does Node.js handle child processes?](#9-how-does-nodejs-handle-child-processes) |
| 10 | [Purpose of cluster module](#10-what-is-the-purpose-of-the-cluster-module) |
| 11 | [CommonJS vs ES Modules](#11-difference-between-commonjs-and-es-modules) |
| 12 | [Create and export custom modules](#12-how-do-you-create-and-export-a-custom-module) |
| 13 | [What is package.json?](#13-what-is-packagejson-and-important-fields) |
| 14 | [dependencies vs devDependencies](#14-difference-between-dependencies-and-devdependencies) |
| 15 | [Environment variables](#15-how-do-you-handle-environment-variables-in-nodejs) |
| 16 | [Callbacks vs Promises vs Async/Await](#16-difference-between-callbacks-promises-and-asyncawait) |
| 17 | [Error handling in async functions](#17-how-do-you-handle-errors-in-async-functions) |
| 18 | [Promise.all vs Promise.race](#18-difference-between-promiseall-and-promiserace) |
| 19 | [Forgetting await](#19-what-happens-if-you-forget-await-in-an-async-function) |
| 20 | [Explain libuv](#20-explain-libuv-in-nodejs) |
| 21 | [What is semantic versioning (semver)?](#21-what-is-semantic-versioning-semver) |
| 22 | [Difference between npm install and npm ci](#22-difference-between-npm-install-and-npm-ci) |
| 23 | [What is package-lock.json?](#23-what-is-package-lockjson) |
| 24 | [How do you handle dependency vulnerabilities?](#24-how-do-you-handle-dependency-vulnerabilities) |
| 25 | [What are peer dependencies?](#25-what-are-peer-dependencies) |
| 26 | [How does Promise chaining work?](#26-how-does-promise-chaining-work) |
| 27 | [What is util.promisify()?](#27-what-is-utilpromisify) |
| 28 | [How do you retry failed async operations?](#28-how-do-you-retry-failed-async-operations) |
| 29 | [How do you implement timeout for promises?](#29-how-do-you-implement-timeout-for-promises) |
| 30 | [What is backpressure in streams?](#30-what-is-backpressure-in-streams) |
| 31 | [What are middleware functions in Express?](#31-what-are-middleware-functions-in-express) |
| 32 | [Difference between app.use() and app.get()](#32-difference-between-appuse-and-appget) |
| 33 | [How do you handle global errors in Express?](#33-how-do-you-handle-global-errors-in-express) |
| 34 | [How do you handle 404 routes in Express?](#34-how-do-you-handle-404-routes-in-express) |
| 35 | [Route params vs query params](#35-route-params-vs-query-params) |
| 36 | [How do you validate request data?](#36-how-do-you-validate-request-data) |
| 37 | [How do you secure Express APIs?](#37-how-do-you-secure-express-apis) |
| 38 | [How do you upload files in Express?](#38-how-do-you-upload-files-in-express) |
| 39 | [How do you handle request body limits?](#39-how-do-you-handle-request-body-limits) |
| 40 | [Difference between unit, integration, and E2E tests](#40-difference-between-unit-integration-and-e2e-tests) |
| 41 | [What testing frameworks have you used in Node.js?](#41-what-testing-frameworks-have-you-used-in-nodejs) |
| 42 | [How do you write a unit test in Jest?](#42-how-do-you-write-a-unit-test-in-jest) |
| 43 | [How do you test async code in Jest?](#43-how-do-you-test-async-code-in-jest) |
| 44 | [What are mocks, stubs, and spies?](#44-what-are-mocks-stubs-and-spies) |
| 45 | [How do you mock external APIs in tests?](#45-how-do-you-mock-external-apis-in-tests) |
| 46 | [How do you test Express routes?](#46-how-do-you-test-express-routes) |
| 47 | [What is Supertest?](#47-what-is-supertest) |
| 48 | [How do you run specific Jest tests?](#48-how-do-you-run-specific-jest-tests) |
| 49 | [How do you measure test coverage?](#49-how-do-you-measure-test-coverage) |
| 50 | [What is snapshot testing?](#50-what-is-snapshot-testing) |
| 51 | [How do you debug Node.js applications?](#51-how-do-you-debug-nodejs-applications) |
| 52 | [What are memory leaks in Node.js?](#52-what-are-memory-leaks-in-nodejs) |
| 53 | [How do you profile CPU usage?](#53-how-do-you-profile-cpu-usage) |
| 54 | [How do you improve Node.js performance?](#54-how-do-you-improve-nodejs-performance) |
| 55 | [What tools are used for API debugging?](#55-what-tools-are-used-for-api-debugging) |
| 56 | [How do you connect Node.js with PostgreSQL?](#56-how-do-you-connect-nodejs-with-postgresql) |
| 57 | [What are connection pools?](#57-what-are-connection-pools) |
| 58 | [How do you prevent SQL injection?](#58-how-do-you-prevent-sql-injection) |
| 59 | [How do you test database queries?](#59-how-do-you-test-database-queries) |
| 60 | [What are in-memory databases in testing?](#60-what-are-in-memory-databases-in-testing) |
| 61 | [What is the difference between EventEmitter.on() and once()?](#61-what-is-the-difference-between-eventemitteron-and-once) |
| 62 | [What is process.exit() in Node.js?](#62-what-is-processexit-in-nodejs) |
| 63 | [How does Node.js handle uncaught exceptions?](#63-how-does-nodejs-handle-uncaught-exceptions) |
| 64 | [What is the difference between path.join() and path.resolve()?](#64-what-is-the-difference-between-pathjoin-and-pathresolve) |
| 65 | [What is zero-copy buffering in Node.js?](#65-what-is-zero-copy-buffering-in-nodejs) |
| 66 | [What are common security risks in Node.js?](#66-what-are-common-security-risks-in-nodejs) |
| 67 | [How do you prevent NoSQL injection?](#67-how-do-you-prevent-nosql-injection) |
| 68 | [What is CORS and how do you handle it?](#68-what-is-cors-and-how-do-you-handle-it) |
| 69 | [What is Helmet middleware?](#69-what-is-helmet-middleware) |
| 70 | [How do you protect API keys and secrets?](#70-how-do-you-protect-api-keys-and-secrets) |
| 71 | [Difference between process and thread](#71-difference-between-process-and-thread) |
| 72 | [What are worker threads in Node.js?](#72-what-are-worker-threads-in-nodejs) |
| 73 | [How do you implement caching in Node.js?](#73-how-do-you-implement-caching-in-nodejs) |
| 74 | [What is load balancing in Node.js?](#74-what-is-load-balancing-in-nodejs) |
| 75 | [What design patterns are used in Node.js?](#75-what-design-patterns-are-used-in-nodejs) |
| 76 | [Reverse a string without built-in methods](#76-reverse-a-string-without-built-in-methods) |
| 77 | [Find duplicate elements in an array](#77-find-duplicate-elements-in-an-array) |
| 78 | [Move all zeros to the end of an array](#78-move-all-zeros-to-the-end-of-an-array) |
| 79 | [Implement a debounce function](#79-implement-a-debounce-function) |
| 80 | [Write a retry API function](#80-write-a-retry-api-function) |
| 81 | [What is module caching in Node.js?](#81-what-is-module-caching-in-nodejs) |
| 82 | [How do circular dependencies work in Node.js?](#82-how-do-circular-dependencies-work-in-nodejs) |
| 83 | [What is require.resolve()?](#83-what-is-requireresolve) |
| 84 | [How does Node.js resolve modules internally?](#84-how-does-nodejs-resolve-modules-internally) |
| 85 | [What is the difference between fs.readFile and createReadStream?](#85-what-is-the-difference-between-fsreadfile-and-createreadstream) |
| 86 | [What are highWaterMark settings in streams?](#86-what-are-highwatermark-settings-in-streams) |
| 87 | [What is object mode in streams?](#87-what-is-object-mode-in-streams) |
| 88 | [What is stream.pipeline()?](#88-what-is-streampipeline) |
| 89 | [How do you handle stream errors properly?](#89-how-do-you-handle-stream-errors-properly) |
| 90 | [What is the purpose of Buffer.alloc()?](#90-what-is-the-purpose-of-bufferalloc) |
| 91 | [Difference between Buffer.alloc and Buffer.from](#91-difference-between-bufferalloc-and-bufferfrom) |
| 92 | [How does process memoryUsage() work?](#92-how-does-processmemoryusage-work) |
| 93 | [What is process.hrtime()?](#93-what-is-processhrtime) |
| 94 | [What is the purpose of setMaxListeners()?](#94-what-is-the-purpose-of-setmaxlisteners) |
| 95 | [How do you create custom events in Node.js?](#95-how-do-you-create-custom-events-in-nodejs) |
| 96 | [What are domains in Node.js?](#96-what-are-domains-in-nodejs) |
| 97 | [What is process.stdin and process.stdout?](#97-what-is-processstdin-and-processstdout) |
| 98 | [How do you create CLI tools in Node.js?](#98-how-do-you-create-cli-tools-in-nodejs) |
| 99 | [What is the purpose of shebang in Node.js scripts?](#99-what-is-the-purpose-of-shebang-in-nodejs-scripts) |
| 100 | [How does Node.js support internationalization (i18n)?](#100-how-does-nodejs-support-internationalization-i18n) |

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

---
---

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

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

[⬆ Back to Top](#-table-of-contents)

---

# 21. What is semantic versioning (semver)?

## Answer

Semantic Versioning is a version naming convention:

```txt
MAJOR.MINOR.PATCH
```

Example:

```txt
2.5.1
```

| Part | Meaning |
|---|---|
| MAJOR | Breaking changes |
| MINOR | New features |
| PATCH | Bug fixes |

---

## Example

```txt
1.0.0 → Initial release
1.1.0 → Added feature
1.1.1 → Fixed bug
2.0.0 → Breaking API changes
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 22. Difference between npm install and npm ci

| npm install | npm ci |
|---|---|
| Used for development | Used mainly in CI/CD |
| Updates package-lock.json | Strictly uses lock file |
| Slower | Faster |
| Flexible installs | Clean installs |

---

## npm ci Benefits

- Faster pipeline builds
- Consistent dependencies
- Better reproducibility

---

## Example

```bash
npm ci
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 23. What is package-lock.json?

## Answer

`package-lock.json` locks exact dependency versions.

It ensures:
- Same dependency versions
- Consistent builds
- Stable deployments

---

## Why Important

Without lock files:
- Different developers may get different package versions.

---

## Example

```json
"express": {
  "version": "5.2.1"
}
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 24. How do you handle dependency vulnerabilities?

## Answer

Use:
- npm audit
- npm audit fix
- Dependabot
- Snyk

---

## Commands

```bash
npm audit
```

```bash
npm audit fix
```

---

## Best Practices

- Keep dependencies updated
- Remove unused packages
- Use trusted libraries only

---

[⬆ Back to Top](#-table-of-contents)

---

# 25. What are peer dependencies?

## Answer

Peer dependencies specify that a package expects another package to already exist.

Common in plugins.

---

## Example

React plugin requiring React:

```json
"peerDependencies": {
  "react": "^18.0.0"
}
```

---

## Why Useful

Prevents duplicate installations and version conflicts.

---

[⬆ Back to Top](#-table-of-contents)

---

# 26. How does Promise chaining work?

## Answer

Promise chaining passes results from one `.then()` to another.

---

## Example

```js
fetch(url)
  .then(res => res.json())
  .then(data => {
    console.log(data);
    return data.id;
  })
  .then(id => {
    console.log(id);
  })
  .catch(err => console.error(err));
```

---

## Benefits

- Cleaner async flow
- Better error handling
- Avoids callback hell

---

[⬆ Back to Top](#-table-of-contents)

---

# 27. What is util.promisify()?

## Answer

`util.promisify()` converts callback-based functions into promise-based functions.

---

## Example

```js
const util = require("util");
const fs = require("fs");

const readFile = util.promisify(fs.readFile);

async function test() {
  const data = await readFile("a.txt", "utf8");
  console.log(data);
}
```

---

## Why Useful

Helps modernize older Node.js APIs.

---

[⬆ Back to Top](#-table-of-contents)

---

# 28. How do you retry failed async operations?

## Answer

Use retry loops or recursive functions.

---

## Example

```js
async function retry(fn, retries = 3) {
  try {
    return await fn();
  } catch (err) {
    if (retries === 0) throw err;

    return retry(fn, retries - 1);
  }
}
```

---

## Real Usage

- API retries
- Database reconnects
- Network failures

---

[⬆ Back to Top](#-table-of-contents)

---

# 29. How do you implement timeout for promises?

## Answer

Use `Promise.race()`.

---

## Example

```js
function timeout(ms) {
  return new Promise((_, reject) => {
    setTimeout(() => reject("Timeout"), ms);
  });
}

Promise.race([
  fetch(url),
  timeout(3000)
]);
```

---

## Use Cases

- Prevent hanging APIs
- Improve reliability
- Fail fast systems

---

[⬆ Back to Top](#-table-of-contents)

---

# 30. What is backpressure in streams?

## Answer

Backpressure occurs when data is produced faster than it is consumed.

---

## Problem

Without backpressure handling:
- Memory usage increases
- App may crash

---

## Solution

Streams automatically pause/resume flow.

---

## Example

```js
readable.pipe(writable);
```

---

## Benefit

Efficient memory usage for large files.

---

[⬆ Back to Top](#-table-of-contents)

---

# 31. What are middleware functions in Express?

## Answer

Middleware functions execute between request and response.

They can:
- Modify request/response
- Validate auth
- Log requests
- Handle errors

---

## Example

```js
app.use((req, res, next) => {
  console.log(req.method);
  next();
});
```

---

## Important

Without `next()`, request flow stops.

---

[⬆ Back to Top](#-table-of-contents)

---

# 32. Difference between app.use() and app.get()

| app.use | app.get |
|---|---|
| Handles middleware | Handles GET routes |
| Works for all HTTP methods | Only GET |
| Can apply globally | Route specific |

---

## Example

```js
app.use(express.json());

app.get("/users", (req, res) => {
  res.send("Users");
});
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 33. How do you handle global errors in Express?

## Answer

Use centralized error middleware.

---

## Example

```js
app.use((err, req, res, next) => {
  res.status(500).json({
    error: err.message
  });
});
```

---

## Benefits

- Cleaner code
- Centralized logging
- Standard responses

---

[⬆ Back to Top](#-table-of-contents)

---

# 34. How do you handle 404 routes in Express?

## Answer

Add a catch-all route at the end.

---

## Example

```js
app.use((req, res) => {
  res.status(404).json({
    message: "Route not found"
  });
});
```

---

## Important

Must be placed after all routes.

---

[⬆ Back to Top](#-table-of-contents)

---

# 35. Route params vs query params

| Route Params | Query Params |
|---|---|
| Part of URL path | Optional filters |
| req.params | req.query |

---

## Route Param Example

```txt
/users/10
```

```js
req.params.id
```

---

## Query Param Example

```txt
/users?page=1
```

```js
req.query.page
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 36. How do you validate request data?

## Answer

Use validation libraries like:
- Joi
- Zod
- express-validator

---

## Example

```js
const schema = Joi.object({
  email: Joi.string().email().required()
});
```

---

## Why Important

Prevents:
- Invalid requests
- Security issues
- DB corruption

---

[⬆ Back to Top](#-table-of-contents)

---

# 37. How do you secure Express APIs?

## Answer

Common security measures:

- Helmet
- CORS
- Rate limiting
- Input validation
- JWT auth

---

## Example

```js
const helmet = require("helmet");

app.use(helmet());
```

---

## Additional Security

- HTTPS
- Secure cookies
- Environment variables

---

[⬆ Back to Top](#-table-of-contents)

---

# 38. How do you upload files in Express?

## Answer

Use multer middleware.

---

## Install

```bash
npm install multer
```

---

## Example

```js
const multer = require("multer");

const upload = multer({
  dest: "uploads/"
});

app.post("/upload",
  upload.single("file"),
  (req, res) => {
    res.send("Uploaded");
  }
);
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 39. How do you handle request body limits?

## Answer

Configure Express parser limits.

---

## Example

```js
app.use(express.json({
  limit: "10mb"
}));
```

---

## Why Important

Prevents:
- DOS attacks
- Huge payload crashes
- Memory exhaustion

---

[⬆ Back to Top](#-table-of-contents)

---

# 40. Difference between unit, integration, and E2E tests

| Test Type | Scope |
|---|---|
| Unit | Single function/module |
| Integration | Multiple modules together |
| E2E | Full application flow |

---

## Examples

### Unit Test

```js
add(2,3)
```

---

### Integration Test

```txt
API + Database
```

---

### E2E Test

```txt
Login → Dashboard → Logout
```

---

## Testing Pyramid

```txt
More Unit Tests
Some Integration Tests
Few E2E Tests
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 41. What testing frameworks have you used in Node.js?

## Answer

Popular testing frameworks:

| Framework | Purpose |
|---|---|
| Jest | Unit & integration testing |
| Mocha | Flexible testing framework |
| Chai | Assertions |
| Supertest | API testing |
| Nock | HTTP mocking |

---

## Most Common Stack

```txt
Jest + Supertest
```

---

## Why Jest is Popular

- Built-in mocking
- Snapshot support
- Coverage reports
- Parallel execution

---

[⬆ Back to Top](#-table-of-contents)

---

# 42. How do you write a unit test in Jest?

## Example Function

```js
function add(a, b) {
  return a + b;
}

module.exports = add;
```

---

## Test File

```js
const add = require("./add");

test("adds numbers", () => {
  expect(add(2, 3)).toBe(5);
});
```

---

## Run Test

```bash
npx jest
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 43. How do you test async code in Jest?

## Using async/await

```js
test("fetches user", async () => {
  const data = await getUser();

  expect(data.name).toBe("Ashish");
});
```

---

## Using resolves

```js
await expect(getUser())
  .resolves
  .toHaveProperty("name");
```

---

## Important

Always return or await async operations.

---

[⬆ Back to Top](#-table-of-contents)

---

# 44. What are mocks, stubs, and spies?

| Type | Purpose |
|---|---|
| Mock | Fake implementation |
| Stub | Returns predefined data |
| Spy | Tracks function calls |

---

## Spy Example

```js
const spy = jest.spyOn(console, "log");

console.log("hello");

expect(spy).toHaveBeenCalled();
```

---

## Why Important

Helps isolate tests from external dependencies.

---

[⬆ Back to Top](#-table-of-contents)

---

# 45. How do you mock external APIs in tests?

## Using Jest Mock

```js
jest.mock("axios");

axios.get.mockResolvedValue({
  data: { name: "Ashish" }
});
```

---

## Using Nock

```js
nock("https://api.com")
  .get("/users")
  .reply(200, { success: true });
```

---

## Benefits

- Faster tests
- No internet dependency
- Stable test results

---

[⬆ Back to Top](#-table-of-contents)

---

# 46. How do you test Express routes?

## Answer

Use:
- Jest
- Supertest

---

## Example

```js
const request = require("supertest");

test("GET /users", async () => {
  const res = await request(app)
    .get("/users");

  expect(res.statusCode).toBe(200);
});
```

---

## What to Verify

- Status codes
- Response body
- Headers
- Error handling

---

[⬆ Back to Top](#-table-of-contents)

---

# 47. What is Supertest?

## Answer

Supertest is a library for testing HTTP APIs.

It allows testing Express routes without running a real server.

---

## Example

```js
const request = require("supertest");

await request(app)
  .post("/login")
  .send({
    email: "a@test.com"
  });
```

---

## Why Useful

- Fast API testing
- Easy assertions
- CI friendly

---

[⬆ Back to Top](#-table-of-contents)

---

# 48. How do you run specific Jest tests?

## Run Single File

```bash
npx jest user.test.js
```

---

## Run by Test Name

```bash
npx jest -t "login test"
```

---

## Run Only One Test

```js
test.only("my test", () => {});
```

---

## Skip Test

```js
test.skip("skip test", () => {});
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 49. How do you measure test coverage?

## Command

```bash
npx jest --coverage
```

---

## Coverage Metrics

| Metric | Meaning |
|---|---|
| Statements | Executed lines |
| Branches | if/else coverage |
| Functions | Function calls |
| Lines | Total executed lines |

---

## Good Practice

Aim for meaningful coverage, not only high percentages.

---

[⬆ Back to Top](#-table-of-contents)

---

# 50. What is snapshot testing?

## Answer

Snapshot testing compares current output with previously saved output.

Useful for:
- UI testing
- JSON response validation

---

## Example

```js
expect(response.body)
  .toMatchSnapshot();
```

---

## Benefit

Detects unexpected changes automatically.

---

[⬆ Back to Top](#-table-of-contents)

---

# 51. How do you debug Node.js applications?

## Methods

- console.log
- Node Inspector
- Chrome DevTools
- VS Code debugger

---

## Start Debug Mode

```bash
node --inspect app.js
```

---

## Useful Tools

| Tool | Purpose |
|---|---|
| nodemon | Auto restart |
| debugger keyword | Breakpoints |
| Chrome DevTools | Visual debugging |

---

[⬆ Back to Top](#-table-of-contents)

---

# 52. What are memory leaks in Node.js?

## Answer

Memory leaks happen when unused memory is not released.

---

## Common Causes

- Global variables
- Unremoved event listeners
- Infinite caches
- Closures

---

## Symptoms

- Increasing RAM usage
- Slow performance
- Crashes

---

## Detection Tools

- heapdump
- Chrome DevTools
- clinic.js

---

[⬆ Back to Top](#-table-of-contents)

---

# 53. How do you profile CPU usage?

## Using Built-in Profiler

```bash
node --prof app.js
```

---

## Analyze

```bash
node --prof-process isolate.log
```

---

## Tools

| Tool | Purpose |
|---|---|
| clinic.js | Performance analysis |
| autocannon | Load testing |
| Chrome DevTools | CPU profiling |

---

[⬆ Back to Top](#-table-of-contents)

---

# 54. How do you improve Node.js performance?

## Best Practices

- Use async operations
- Avoid blocking code
- Use caching
- Optimize DB queries
- Use streams for large files

---

## Additional Optimizations

- Compression middleware
- Connection pooling
- Clustering
- Pagination

---

## Example

```js
app.use(compression());
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 55. What tools are used for API debugging?

| Tool | Usage |
|---|---|
| Postman | API testing |
| Newman | CLI automation |
| Curl | Terminal requests |
| Insomnia | REST client |
| Swagger | API documentation |

---

## Example Curl

```bash
curl http://localhost:3000/users
```

---

## CI Usage

Newman can run Postman collections in pipelines.

---

[⬆ Back to Top](#-table-of-contents)

---

# 56. How do you connect Node.js with PostgreSQL?

## Install

```bash
npm install pg
```

---

## Example

```js
const { Pool } = require("pg");

const pool = new Pool({
  user: "postgres",
  password: "1234",
  database: "test"
});
```

---

## Query

```js
const result = await pool.query(
  "SELECT * FROM users"
);
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 57. What are connection pools?

## Answer

Connection pools reuse database connections instead of creating new ones every request.

---

## Benefits

- Faster DB access
- Better scalability
- Reduced overhead

---

## Example

```js
const pool = new Pool({
  max: 10
});
```

---

## Important

Always release unused connections.

---

[⬆ Back to Top](#-table-of-contents)

---

# 58. How do you prevent SQL injection?

## Use Parameterized Queries

```js
pool.query(
  "SELECT * FROM users WHERE id=$1",
  [id]
);
```

---

## Avoid

```js
"SELECT * FROM users WHERE id=" + id
```

---

## Additional Security

- Input validation
- ORM usage
- Least DB permissions

---

[⬆ Back to Top](#-table-of-contents)

---

# 59. How do you test database queries?

## Approaches

- Mock DB calls
- Use test database
- In-memory database

---

## Example

```js
jest.spyOn(pool, "query")
  .mockResolvedValue({
    rows: []
  });
```

---

## Best Practice

Separate DB logic into repository/service layers.

---

[⬆ Back to Top](#-table-of-contents)

---

# 60. What are in-memory databases in testing?

## Answer

In-memory databases run entirely in RAM during tests.

---

## Examples

| Database | Tool |
|---|---|
| MongoDB | mongodb-memory-server |
| SQLite | sqlite-memory |

---

## Benefits

- Faster tests
- Isolated environment
- No real DB dependency

---

## Common Usage

Integration testing.

---

[⬆ Back to Top](#-table-of-contents)

---

# 61. What is the difference between EventEmitter.on() and once()?

| on() | once() |
|---|---|
| Executes every time event occurs | Executes only once |
| Listener remains attached | Listener auto removed |

---

## Example

```js
const EventEmitter =
  require("events");

const emitter =
  new EventEmitter();

emitter.once("login", () => {
  console.log("Logged In");
});

emitter.emit("login");
emitter.emit("login");
```

---

## Output

```txt
Logged In
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 62. What is process.exit() in Node.js?

## Answer

`process.exit()` terminates the Node.js process immediately.

---

## Example

```js
console.log("Start");

process.exit();

console.log("End");
```

---

## Output

```txt
Start
```

---

## Important

Exit code:
- `0` → Success
- Non-zero → Failure

---

## Example

```js
process.exit(1);
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 63. How does Node.js handle uncaught exceptions?

## Answer

Uncaught exceptions can crash the application.

---

## Global Handler

```js
process.on(
  "uncaughtException",
  err => {
    console.error(err);
  }
);
```

---

## Best Practice

- Log the error
- Cleanup resources
- Restart application safely

---

## Important

Do not continue running unstable applications after critical exceptions.

---

[⬆ Back to Top](#-table-of-contents)

---

# 64. What is the difference between path.join() and path.resolve()?

| path.join | path.resolve |
|---|---|
| Joins path segments | Resolves absolute path |
| Relative output possible | Always absolute |

---

## Example

```js
path.join("a", "b");
```

Output:

```txt
a/b
```

---

## Example

```js
path.resolve("a", "b");
```

Output:

```txt
/full/path/a/b
```

---

## Common Usage

- `join()` → Relative paths
- `resolve()` → Absolute paths

---

[⬆ Back to Top](#-table-of-contents)

---

# 65. What is zero-copy buffering in Node.js?

## Answer

Zero-copy buffering avoids unnecessary memory copying between buffers.

---

## Benefits

- Better performance
- Lower memory usage
- Faster networking/file operations

---

## Example

Buffers can share memory internally instead of duplicating data.

---

## Common Usage

- Streams
- TCP sockets
- File transfers

---

[⬆ Back to Top](#-table-of-contents)

---

# 66. What are common security risks in Node.js?

## Common Risks

- SQL Injection
- NoSQL Injection
- XSS
- CSRF
- Dependency vulnerabilities

---

## Prevention

- Input validation
- Helmet
- Rate limiting
- Secure authentication

---

## Important

Always update dependencies regularly.

---

[⬆ Back to Top](#-table-of-contents)

---

# 67. How do you prevent NoSQL injection?

## Example Risk

```js
User.find({
  username: req.body.username
});
```

Malicious objects can manipulate queries.

---

## Prevention

- Validate inputs
- Sanitize requests
- Use strict schemas

---

## Example

```js
typeof username === "string"
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 68. What is CORS and how do you handle it?

## Answer

CORS (Cross-Origin Resource Sharing) controls which domains can access APIs.

---

## Install

```bash
npm install cors
```

---

## Example

```js
const cors = require("cors");

app.use(cors({
  origin: "https://example.com"
}));
```

---

## Why Important

Prevents unauthorized frontend access.

---

[⬆ Back to Top](#-table-of-contents)

---

# 69. What is Helmet middleware?

## Answer

Helmet secures Express apps by setting HTTP security headers.

---

## Install

```bash
npm install helmet
```

---

## Example

```js
const helmet = require("helmet");

app.use(helmet());
```

---

## Protection Includes

- XSS protection
- Clickjacking prevention
- Hiding server details

---

[⬆ Back to Top](#-table-of-contents)

---

# 70. How do you protect API keys and secrets?

## Best Practices

- Store in `.env`
- Use secret managers
- Rotate keys regularly
- Restrict permissions

---

## Avoid

```txt
Uploading .env to GitHub
```

---

## Example

```js
process.env.API_KEY
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 71. Difference between process and thread

| Process | Thread |
|---|---|
| Independent program | Lightweight execution unit |
| Separate memory | Shared memory |
| More overhead | Faster |

---

## Node.js

Node mainly runs on:
```txt
Single main thread
```

But uses worker threads internally.

---

[⬆ Back to Top](#-table-of-contents)

---

# 72. What are worker threads in Node.js?

## Answer

Worker threads allow parallel execution of CPU-intensive tasks.

---

## Useful For

- Image processing
- Data compression
- Heavy calculations

---

## Example

```js
const {
  Worker
} = require("worker_threads");
```

---

## Benefit

Prevents blocking the main event loop.

---

[⬆ Back to Top](#-table-of-contents)

---

# 73. How do you implement caching in Node.js?

## Types

- In-memory cache
- Redis cache

---

## Example

```js
const cache = new Map();

cache.set("user", data);
```

---

## Redis Benefits

- Shared across servers
- Persistent
- Faster reads

---

## Common Usage

Caching API responses.

---

[⬆ Back to Top](#-table-of-contents)

---

# 74. What is load balancing in Node.js?

## Answer

Load balancing distributes traffic across multiple servers/processes.

---

## Benefits

- Better scalability
- High availability
- Fault tolerance

---

## Common Tools

- Nginx
- PM2
- AWS ELB

---

## Flow

```txt
Client
→ Load Balancer
→ Multiple Node Servers
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 75. What design patterns are used in Node.js?

## Common Patterns

| Pattern | Usage |
|---|---|
| Singleton | Single DB instance |
| Factory | Object creation |
| Middleware | Express request flow |
| Observer | EventEmitter |

---

## Example Singleton

```js
module.exports = new Database();
```

---

## Benefit

Improves code maintainability and scalability.

---

[⬆ Back to Top](#-table-of-contents)

---

# 76. Reverse a string without built-in methods

## Example

```js
function reverse(str) {
  let result = "";

  for (let i = str.length - 1; i >= 0; i--) {
    result += str[i];
  }

  return result;
}
```

---

## Complexity

| Time | Space |
|---|---|
| O(n) | O(n) |

---

[⬆ Back to Top](#-table-of-contents)

---

# 77. Find duplicate elements in an array

## Example

```js
function findDuplicates(arr) {
  const seen = new Set();
  const duplicates = new Set();

  for (const num of arr) {
    if (seen.has(num)) {
      duplicates.add(num);
    }

    seen.add(num);
  }

  return [...duplicates];
}
```

---

## Complexity

| Time | Space |
|---|---|
| O(n) | O(n) |

---

[⬆ Back to Top](#-table-of-contents)

---

# 78. Move all zeros to the end of an array

## Example

```js
function moveZeros(arr) {
  const nonZeros = arr.filter(n => n !== 0);
  const zeros = arr.filter(n => n === 0);

  return [...nonZeros, ...zeros];
}
```

---

## Input

```js
[1,0,2,0,3]
```

---

## Output

```js
[1,2,3,0,0]
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 79. Implement a debounce function

## Answer

Debounce delays function execution until user stops triggering events.

---

## Example

```js
function debounce(fn, delay) {
  let timer;

  return function (...args) {
    clearTimeout(timer);

    timer = setTimeout(() => {
      fn.apply(this, args);
    }, delay);
  };
}
```

---

## Common Usage

- Search inputs
- Resize events
- Scroll handlers

---

[⬆ Back to Top](#-table-of-contents)

---

# 80. Write a retry API function

## Example

```js
async function retryApi(fn, retries = 3) {
  try {
    return await fn();
  } catch (err) {
    if (retries === 0) {
      throw err;
    }

    return retryApi(fn, retries - 1);
  }
}
```

---

## Usage

```js
retryApi(() => axios.get(url));
```

---

## Real Use Cases

- Temporary network failures
- External API instability

---

[⬆ Back to Top](#-table-of-contents)

---

# 81. What is module caching in Node.js?

## Answer

When a module is loaded using `require()`, Node.js caches it.

Future `require()` calls return the cached version instead of reloading the file.

---

## Example

```js
const math1 = require("./math");
const math2 = require("./math");

console.log(math1 === math2);
```

---

## Output

```txt
true
```

---

## Benefit

Improves performance and avoids duplicate execution.

---

[⬆ Back to Top](#-table-of-contents)

---

# 82. How do circular dependencies work in Node.js?

## Answer

Circular dependency occurs when:
- Module A imports B
- Module B imports A

---

## Problem

Modules may receive partially initialized exports.

---

## Example

```txt
A → B
B → A
```

---

## Best Practice

Avoid tight coupling between modules.

---

[⬆ Back to Top](#-table-of-contents)

---

# 83. What is require.resolve()?

## Answer

`require.resolve()` returns the resolved file path of a module.

---

## Example

```js
console.log(
  require.resolve("express")
);
```

---

## Use Cases

- Debugging
- Checking module paths
- Dynamic loading

---

[⬆ Back to Top](#-table-of-contents)

---

# 84. How does Node.js resolve modules internally?

## Resolution Order

1. Core modules
2. Local files
3. node_modules folders

---

## Example

```js
require("fs");
require("./app");
require("express");
```

---

## Important

Node searches parent directories recursively for `node_modules`.

---

[⬆ Back to Top](#-table-of-contents)

---

# 85. What is the difference between fs.readFile and createReadStream?

| fs.readFile | createReadStream |
|---|---|
| Loads full file | Reads chunks |
| High memory usage | Memory efficient |
| Better for small files | Better for large files |

---

## Stream Example

```js
fs.createReadStream("big.zip");
```

---

## Best Practice

Use streams for large file processing.

---

[⬆ Back to Top](#-table-of-contents)

---

# 86. What are highWaterMark settings in streams?

## Answer

`highWaterMark` controls internal buffer size in streams.

---

## Example

```js
fs.createReadStream("a.txt", {
  highWaterMark: 1024
});
```

---

## Benefit

Helps optimize memory and performance.

---

## Units

- Bytes for binary streams
- Objects for object mode

---

[⬆ Back to Top](#-table-of-contents)

---

# 87. What is object mode in streams?

## Answer

Object mode allows streams to process JavaScript objects instead of binary/string data.

---

## Example

```js
new stream.Readable({
  objectMode: true
});
```

---

## Common Usage

- JSON processing
- Data transformations

---

[⬆ Back to Top](#-table-of-contents)

---

# 88. What is stream.pipeline()?

## Answer

`stream.pipeline()` safely connects streams together.

---

## Example

```js
const pipeline =
  require("stream").pipeline;

pipeline(
  readStream,
  writeStream,
  err => {
    if (err) console.error(err);
  }
);
```

---

## Benefits

- Automatic cleanup
- Better error handling

---

[⬆ Back to Top](#-table-of-contents)

---

# 89. How do you handle stream errors properly?

## Example

```js
readStream.on("error", err => {
  console.error(err);
});
```

---

## Important

Unhandled stream errors can crash applications.

---

## Better Option

Use:
```txt
stream.pipeline()
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 90. What is the purpose of Buffer.alloc()?

## Answer

Creates a new buffer with initialized memory.

---

## Example

```js
const buf = Buffer.alloc(10);
```

---

## Benefit

Prevents security issues caused by uninitialized memory.

---

[⬆ Back to Top](#-table-of-contents)

---

# 91. Difference between Buffer.alloc and Buffer.from

| Buffer.alloc | Buffer.from |
|---|---|
| Creates empty buffer | Creates from existing data |
| Size based | Data based |

---

## Examples

```js
Buffer.alloc(5);

Buffer.from("hello");
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 92. How does process.memoryUsage() work?

## Answer

Returns memory usage statistics for current process.

---

## Example

```js
console.log(
  process.memoryUsage()
);
```

---

## Common Metrics

| Metric | Meaning |
|---|---|
| rss | Total memory |
| heapUsed | Used heap |
| heapTotal | Total heap |

---

[⬆ Back to Top](#-table-of-contents)

---

# 93. What is process.hrtime()?

## Answer

Provides high-resolution time measurements.

---

## Example

```js
const start = process.hrtime();

/* task */

const end = process.hrtime(start);

console.log(end);
```

---

## Common Usage

Performance benchmarking.

---

[⬆ Back to Top](#-table-of-contents)

---

# 94. What is the purpose of setMaxListeners()?

## Answer

Controls maximum listeners allowed on EventEmitter.

---

## Example

```js
emitter.setMaxListeners(20);
```

---

## Default Limit

```txt
10 listeners
```

---

## Why Important

Prevents memory leak warnings.

---

[⬆ Back to Top](#-table-of-contents)

---

# 95. How do you create custom events in Node.js?

## Example

```js
const EventEmitter =
  require("events");

const emitter =
  new EventEmitter();

emitter.on("login", user => {
  console.log(user);
});

emitter.emit("login", "Ashish");
```

---

## Common Usage

- Notifications
- Logging systems
- Background jobs

---

[⬆ Back to Top](#-table-of-contents)

---

# 96. What are domains in Node.js?

## Answer

Domains were used for error handling across async operations.

---

## Important

Domains are deprecated.

---

## Modern Alternative

Use:
- try/catch
- async handlers
- centralized error middleware

---

[⬆ Back to Top](#-table-of-contents)

---

# 97. What is process.stdin and process.stdout?

## Answer

Standard input/output streams for CLI interaction.

---

## Example

```js
process.stdout.write("Hello");
```

---

## Reading Input

```js
process.stdin.on("data", data => {
  console.log(data.toString());
});
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 98. How do you create CLI tools in Node.js?

## Steps

1. Create executable script
2. Add shebang
3. Configure package.json

---

## Example

```js
#!/usr/bin/env node

console.log("CLI Tool");
```

---

## Install Globally

```bash
npm install -g
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 99. What is the purpose of shebang in Node.js scripts?

## Example

```js
#!/usr/bin/env node
```

---

## Purpose

Allows scripts to run directly from terminal.

---

## Example

```bash
./app.js
```

---

[⬆ Back to Top](#-table-of-contents)

---

# 100. How does Node.js support internationalization (i18n)?

## Answer

Node.js supports i18n using:
- Intl API
- Libraries like i18next

---

## Example

```js
new Intl.DateTimeFormat(
  "en-IN"
).format(new Date());
```

---

## Common Features

- Date formatting
- Currency formatting
- Multi-language support

---

[⬆ Back to Top](#-table-of-contents)

---