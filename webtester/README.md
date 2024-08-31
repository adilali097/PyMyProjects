

```markdown
# Web Tester

## Overview

The **Web Tester** is a simple Python-based tool designed for developers and ethical hackers to perform basic web testing tasks. It allows you to check the status of a web URL, measure response time, and get basic information about the HTTP response.

## Features

- Check the status code of a URL
- Measure the response time
- Display the first 200 characters of the response content
- Support for different HTTP methods (GET, POST, etc.)

## Requirements

- Python 3.x
- `requests` library

## Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd web_tester
```

Replace `<repository-url>` with the actual URL of your repository.

### 2. Set Up the Virtual Environment

Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Running the Web Tester

You can run the web tester tool from the terminal using the following command:

```bash
python src/web_tester.py <url> [method] [headers] [data]
```

- `<url>`: The URL you want to test.
- `[method]` (optional): The HTTP method to use (GET, POST, etc.). Default is GET.
- `[headers]` (optional): Custom headers for the request. Provide as a JSON string, e.g., `"{\"User-Agent\": \"my-tester\"}"`.
- `[data]` (optional): Data payload for POST requests. Provide as a JSON string, e.g., `"{\"key\": \"value\"}"`.

### Examples

1. **Check the status of a URL using the GET method:**

   ```bash
   python src/web_tester.py https://example.com
   ```

2. **Check the status of a URL using the POST method with custom data:**

   ```bash
   python src/web_tester.py https://example.com POST "" "{\"key\": \"value\"}"
   ```

3. **Check the status of a URL with custom headers:**

   ```bash
   python src/web_tester.py https://example.com GET "{\"User-Agent\": \"my-tester\"}"
   ```

## Contributing

Feel free to contribute to this project by submitting issues, feature requests, or pull requests. Your feedback and contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact:

- **Name**: Muhammad Adnan
- **Email**: [your-email@example.com](mailto:your-email@example.com)

```

### How to Use the README.md

1. **Clone the Repository**: Replace `<repository-url>` with your repository URL.
2. **Setup Instructions**: Follow the steps to create a virtual environment and install dependencies.
3. **Running the Code**: Use the provided command examples to run the tool with different options.
4. **Contributing and Licensing**: Encourage contributions and provide licensing information.
5. **Contact Information**: Update the contact section with your details.

This `README.md` provides clear instructions on how to set up, run, and use your web tester tool.
