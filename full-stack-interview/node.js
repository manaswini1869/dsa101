const http = require('http');
const port = 5000;
const server = http.createServer((req, res) => {
    res.writeHead(200, {'content-type': 'text/plain'});
    res.end();
})

server.listen(port, () => {
    console.log(`Server listening on port ${port}`)
})

/*

nodejs and express js are closely related,

Asynchronous and non-blocking programming

Asynchronous programming allows your code to start a task and move on to the next one without waiting
for the previous task to finish; refers to the timing of tasks run independently and notify when they are done

non-blocking programming: refers to the way Node.js handles tasks without stopping or blocking the execution of other tasks;
behaviors of the code ensuring that no task waits or holds up the system

*/


/*

Event Loop : is a mechanism that handles asynchronous operations, allows nodejs to perform non-blocking I/O operations even though JS is single threaded

*/

/*

Middleware in express js: is a function that has access to the requests object (req), the response object (res), and the next middleware
function in the application's request-response cycle

logging, data arsing, authentication

*/


/*

child threads: handles child threads by using worker threads for parallel processing and child processes for creating independent processes. The event
loop and non-blocking i/O handle most asynchronous tasks, ensuring that Node.js remains efficient and fast

event loop and non blocking  i/o

worker threads: allow you to create threads that can run JavaScript code Independently, separate from the main event loop

Child processes : they run alongside the main program to handle specific tasks, these threads can work in parallel, allowing the main thread to keep doing
its job without waiting for these helper threads to finish

IPC = inter process communication
*/

/*

Streams : huge flow of data,streams are a way to handle reading or writing data continuously, piece by piece rather than all at once. They are particularly
useful for dealing with large amounts of data or data that is being received over time, like files, network requests, or nay process that requires
data to be processed gradually

readable, writable, duplex, transform

*/

/*

Callback hell : situation in programming especially in Javascript where multiple nested callbacks (functions executed after a task is completed) make the
code difficult to read, understand, and maintain

you can use promises
use async and await
modularize the code

*/

/*

promises improve callback handling : allow you to chain asynchronous operations using .then(), making the code more linear and readable

readability
error handling
flexibility
*/

/*

package,json : central configuration file that defines important information about the project

project metadata
version control
dependencies
PD management
scripts
project configuration

*/

/*

process.nextTick(): when you need to run code immediately after the current operation, with a higher priority than I/O tasks


setImmediate(): when you want to defer the execution of code until the current I/O operations are complete and wait for the next event loop cycle

*/


/*

errors in Node.js : hand;ing error is important to ensure that your application runs smoothly and can recover from unexpected issues

try-catch block
asynchronous callback
promises
global error handling

*/




