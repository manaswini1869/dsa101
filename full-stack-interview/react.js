/*

The Virtual Document Object Model (VDOM) is a concept used to improve the efficiency of
updating the user interface in web application, especially in Javascript frameworks like React.
It acts as a lightweight copy of the real DOM, allowing for faster manipulation and rendering of UI components.
Without actually changing the real DOM, which can be slow and resource-intensive.

*/

/*

State Management in React :involves controlling the flow and handling of data withing your application to ensure
the UI responds correctly to user inputs and data changes. Common state management techniques in React include:
- Local State: using useState hook for managing state within a single component.
- Lifting State Up: sharing state between components by moving it to their closest common ancestor.
- Context API: for global state management across multiple components without prop drilling.
- Redux: a popular library for managing complex application state in a predictable way.

Component State
Props Drilling - passing message from parent to the child component
Context API - useful for global state management
State Management Libraries (Redux, MobX)
*/

/*

Common hooks in React :
- useState: for managing state in functional components, used for creating variables that can change over time
- useEffect :Lets you perform side effects in your components such as data fetching, subscriptions, or manually updating the DOM
- useContext : used to access data from a context in your component without prop drilling

*/

/*

Components Lifecycle in React :

Mounting Phase:
    - construction phase: component is being created and initialized
    - rendering phase: component's render method is called to determine what to display on the screen
    - componentDidMount: called after the component is rendered and added to the DOM

Updating Phase:
    - shouldComponentUpdate: allows you to optimize performance by preventing unnecessary re-renders
    - re-rendering phase: component's render method is called again to update the UI based on new props or state
    - componentDidUpdate: called after the component has been updated in the DOM

Unmounting Phase:
    - componentWillUnmount: called just before the component is removed from the DOM, used for cleanup tasks

*/

/*

Context API in React : provides a way to share values like themes, user information, or settings
across the component tree without having to pass props down manually at every level.
It is useful for managing global state that needs to be accessed by many components at different nesting levels.

Difference between props and state :
Props are read-only and passed from parent to child components, while state is mutable and managed within the component itself.
Props are used to pass data and event handlers down the component tree, whereas state is used to manage data that can change over time within a component.

*/

/*

Optimize Performance with React App:
- Built in performance optimization
- Code Splitting - render components only when required
- Optimize Context Usage - be smart with shared data
- memoization : remember calculations and functions
- reduce component re-renders control when component re-renders

*/


/*

higher-order component:
is a function that takes a component as an argument and returns a new component.
HOCs are a pattern for reusing component logic

*/

/*

forms in React:
managing the form inputs
capturing the inputs
store the submission
respond

*/

/*

server-side rendering :
the web-page will already be rendered and be delivered to the user's particular browser; technique where a a web page
is rendered on the server before it is sent to the user's browser, instead of sending a blank HTML file with JavaScript code
that builds the page on the client side, the server generates the HTML with content already included and sends it
to the browser

faster initial load
better seo : search engine optimization
improved performance
reduced interaction time

*/

/*

redux:
in react components manage their own internal stat, but as an application grows, managing shared state between
multiple components can become complex. This is where redux helps by providing a single global state the any component can access

*/