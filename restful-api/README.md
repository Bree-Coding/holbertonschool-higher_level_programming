# 🌐 Basics of HTTP/HTTPS

## Background
The Hypertext Transfer Protocol (HTTP) is the foundation of data communication on the web. It allows web clients (like browsers) to communicate with web servers. HTTP has evolved over time and has a secure counterpart called HTTPS (HTTP Secure). HTTPS is just like HTTP but with an added layer of security using SSL/TLS encryption. This layer protects the data from eavesdroppers and tampering.

## Objective
At the end of this exercise, students should be able to:
- Differentiate between HTTP and HTTPS.
- Understand the basic working and structure of HTTP requests and responses.
- Recognize and explain the common HTTP methods and status codes.

## Resources
- [Mozilla Developer Network (MDN) - An Overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
- [Difference between HTTP and HTTPS](https://www.instantssl.com/http-vs-https)
- [List of HTTP status codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

## Instructions
### Differentiating HTTP and HTTPS
1. Read the provided resources to understand the basic differences between HTTP and HTTPS.
2. Jot down the main differences, focusing on security aspects.

### Understanding HTTP Structure
1. Visit a simple website, right-click, and choose “Inspect” or “Inspect Element”. Navigate to the “Network” tab. This shows all network requests made by the page.
2. Reload the page and observe the first request. Click on it. Explore the “Headers” section to understand the structure of HTTP requests and responses. You’ll see methods, paths, status codes, headers, and more.

### Exploring HTTP Methods and Status Codes
1. Based on the resources provided, make a list of at least four common HTTP methods and explain when each would be used.
2. Make another list of five common HTTP status codes. For each status code, provide a brief description and a scenario where it might be encountered.

## Hints
- HTTP does not encrypt its data, which means that anyone eavesdropping on the communication can see the content. HTTPS adds a layer of encryption, making the content unintelligible to eavesdroppers.
- The “s” in “https” stands for “secure”. Websites, especially those that handle sensitive data like banking websites or email providers, typically use HTTPS.
- Each HTTP status code has a specific purpose. They are grouped by their first digit: 1xx (informational), 2xx (successful), 3xx (redirection), 4xx (client errors), and 5xx (server errors).

## Expected Output
- A brief summary explaining the differences between HTTP and HTTPS.
- A depiction or outline of the structure of an HTTP request and response.
- Lists of common HTTP methods and status codes with their descriptions and possible use cases.

---

# 🛠️ Consume data from an API using command line tools (curl)

## Background
curl (Client URL) is a command-line tool that allows users to transfer data to or from a network server, using one of the supported protocols (HTTP, HTTPS, FTP, and more). It’s widely used for debugging, testing, and interacting with RESTful web services and APIs. By mastering curl, one can quickly prototype API requests, diagnose server issues, and more, all from the command line.

## Objective
At the end of this exercise, students should be able to:
- Install and use curl from the command line.
- Construct and execute basic API requests using curl, including setting headers and inspecting the output.
- Interpret the results of common API requests.

## Resources
- [curl - Everything curl](https://everything.curl.dev/)
- [Using cURL to interact with HTTP APIs](https://curl.se/docs/httpscripting.html)
- [Public API to play with: JSONPlaceholder](https://jsonplaceholder.typicode.com/)

## Instructions
### Installing and Basic Interaction with curl
1. Install curl on your system. It’s usually available in standard repositories for Linux/Mac systems. For Windows, consider using Windows Subsystem for Linux (WSL) or downloading a Windows version of curl.
2. Once installed, run `curl --version` to confirm its availability.
3. Use curl to fetch the content of a webpage. For instance: `curl http://example.com`.

### Fetching Data from an API
1. Use curl to retrieve posts from JSONPlaceholder: `curl https://jsonplaceholder.typicode.com/posts`
2. Observe the output. It should be a JSON array of posts.

### Using Headers and Other Options with curl
1. Fetch only the headers of the same request using `curl -I https://jsonplaceholder.typicode.com/posts`.
2. Use curl to make a POST request to the same API: `curl -X POST -d "title=foo&body=bar&userId=1" https://jsonplaceholder.typicode.com/posts`

## Hints
- The `-I` flag in curl fetches only the headers of the response, which can be useful to diagnose server settings, cache controls, content type, and more.
- With the `-X` flag, you can specify an HTTP method for your request. For example, `-X POST` will make a POST request.
- The `-d` flag allows you to pass data in your request. In RESTful APIs, this is commonly used with POST, PUT, or PATCH requests to send data to the server.
- If you’re getting a lot of output and want to view it in a more organized way, consider piping the output to a tool like `jq` for JSON formatting and highlighting.

## Expected Output
- Upon running `curl --version`, you should see details about your installed version of curl, including supported protocols.
- Fetching posts from JSONPlaceholder should provide a JSON output of various posts, each having attributes like userId, id, title, and body.
- Fetching only headers should give a concise output showing status codes and headers without the actual content.
- Making a POST request should yield a response from the server acknowledging the reception of the data. For JSONPlaceholder, it typically returns the created post with an id of 101 (since it doesn’t actually save the new post, but simulates the creation).

---

# 🐍 Consuming and processing data from an API using Python

## Background
Python, due to its readability and a vast library ecosystem, is a popular choice for interacting with web services and APIs. The requests library simplifies HTTP communication and allows users to send HTTP requests using Python. Once the data is fetched, Python’s built-in libraries and tools enable effortless data manipulation and processing.

## Objective
At the end of this exercise, students should be able to:
- Utilize the requests library to send HTTP requests and process responses.
- Parse and manipulate JSON data using Python.
- Convert structured data into other formats, e.g., CSV.

## Resources
- [Python Requests Library](https://docs.python-requests.org/en/latest/)
- [Working with JSON data in Python](https://realpython.com/python-json/)
- [Public API to experiment with: JSONPlaceholder](https://jsonplaceholder.typicode.com/)

## Instructions
1. If not installed, install the requests library using pip: `pip install requests`.
2. Write a basic Python script to fetch posts from JSONPlaceholder using `requests.get()`.
3. Create a function `fetch_and_print_posts()` that fetches all posts from JSONPlaceholder.
   - Print the status code of the response i.e. Status Code: 200
   - If the request was successful, parse the fetched data into a JSON object using the `.json()` method of the response object.
   - Iterate through the parsed JSON data and print out the titles of all the posts.
4. Create a function `fetch_and_save_posts()` that fetches all posts from JSONPlaceholder.
   - If the request was successful, instead of printing titles, structure the data into a list of dictionaries, where each dictionary represents a post with keys and values for id, title, and body.
   - Using Python’s csv module, write this data into a CSV file called `posts.csv` with columns corresponding to the dictionary keys.

## Hints
- The `requests.get()` function returns a Response object, from which you can access various properties like status_code, headers, and methods like json().
- When converting the parsed JSON data into a list of dictionaries, you might find list comprehensions useful for concise code.
- The `csv.DictWriter` class can be a convenient way to write dictionaries to a CSV file, as it automatically handles headers based on dictionary keys.

## Expected Output
- After the basic interaction script, you should have an output indicating a 200 status code, suggesting a successful GET request.
- When parsing JSON data, you should see printed titles of the posts, e.g., “sunt aut facere repellat provident occaecati excepturi optio reprehenderit.”
- After the data manipulation and conversion task, you should have a CSV file with columns id, title, and body. Each row in the CSV should correspond to a post from the fetched data.