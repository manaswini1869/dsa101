/*
- Hoisting in Javascript : refers to the behavior where a declared variable or function is moved or hoisted
to the top of its scope before code execution. This means that you can use variables and functions before they are declared in the code.
When you run the code, JS hoists the variable to the top

variable : only the declarations are hoisted not the initializations. Declarations : when the variable is created using var, let or const.
initializations : when a value is assigned to the variable.

function : function declarations are fully hoisted meaning you can call a function even before you define it in the code.

Let and Const: variables are declared using let and const are also hoisted but they are not initialized.
they exist in a "temporal dead zone" from the start of the block until the declaration is encountered. of its scope, but the initialization remains in place.
*/

var x = 5; // Declaration and Initialization
console.log(x); // Output: 5


greet(); // Output: Hello, World!

function greet() {
    console.log("Hello, World!");
}


/*

localStorage: Data stored has not expiration time, it remains available even after the browser or tab is closed and will persist until it is
explicitly delete byt eh user or through code.

sessionStorage:Data is temporary and is only available for the duration of the page session.Data stored in sessionStorage is tied to the specific session of the browser.
It gets cleared when the browser tab is cleared, meaning the data is only available as long as the tab or window is open.

*/

/*
How can page loading time be reduced in a web application?

very important to increase the user retention and satisfaction.
- optimize the images : use format WebP formats smaller size but good quality
- Minimize HTTP Requests: Combine CSS and Javascript files where possible
- Enable Browser Caching: Allow browser to store some elements of the pager
- Content Delivery Network (CDN): Use CDN to deliver content from servers closer to the user
- Use lazy loading: Delay the loading of images and videos until they are needed
*/

/*

SOAP and REST
SoAP (Simple Object Access Protocol) is a protocol for exchanging structured information in web services using XML.
REST (Representational State Transfer) is an architectural style for designing networked applications using stateless communication and standard HTTP methods.

Soap is a strict set of rules for sending messages, only uses XML (more complicated), can remember past requests or not, uses its own rules for sending and receiving messages.
Suitable for complex and secure application

Rest is a way to use existing web rules to get data, JSON, XML, plain text, doesn't remember past requests, uses standard HTTP methods (GET, POST, PUT, DELETE).
speed and scalable
*/

/*

GraphQL and REST

GraphQL is a query language for APIs and a runtime for executing those queries by allowing clients to request only the data they need.
Single endpoint for all queries, client defines the structure of the response, reduces over-fetching and under-fetching of data.

REST is an architectural style for designing networked applications using stateless communication and standard HTTP methods.
Overfetching and underfetching of data, multiple endpoints for different resources, inflexible data structure.
multiple enedpoints for different resources, inflexible data structure.
server defines structure of the response.

*/

/*

Components of a CSS box model

1. Content: The innermost part of the box where text and images are displayed.
2. Padding: The space between the content and the border. It creates space inside the box.
3. Border: The edge of the box that surrounds the padding (if any) and content. It can be styled with different widths, colors, and styles.
4. Margin: The outermost layer that creates space between the box and other elements on the page. It is transparent and does not have a background color.

*/

/*
Class selector and id selector in CSS
- Class Selector: used to select elements with a specific class attribute. It is defined using a period (.) followed by the class name.
- Id Selector: used to select a single element with a specific id attribute. It is defined using a hash (#) followed by the id name.
*/

/*
Data Types:
primitive data types: Number, String, Boolean, Null, Undefined, Symbol, BigInt
non-primitive data types: Object, Array, Function
*/

/*

What is DOM : Document Object Model is a programming interface for web document. It represents the structure of a webpage as a tree of objects
where each element in the HTML or XML document is a node in the tree. Through the DOM,
programming languages like JacaScript can interact with and modify the content, structure, and style of a webpage dynamically.

*/

/*

this keyword in Javascript:
in Javascript the this keyword refers to the current execution context or the object that is currently executing the code. Its value can vary
depending on how a function is called

*/