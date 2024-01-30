# Meme Generator

This Python application is a meme generator that can be used both as a Flask web app and a command-line interface (CLI). 
It allows users to generate random memes or create custom memes by combining images and quotes. The application includes two modes:

## Flask Web App

#### Installation
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask app:
   ```bash
   python3 app.py
   ```

4. Open your web browser and navigate to `http://127.0.0.1:5000/` to use the meme generator.

### Features

1. **Generate Random Meme:**
   - Endpoint: `/`
   - Description: Displays a randomly generated meme by selecting a random image from the available collection and pairing it with a random quote.
   - Usage: Visit the root URL (`/`) to view a new random meme each time.

2. **Create Custom Meme:**
   - Endpoint: `/create`
   - Description: Allows users to create custom memes by providing an image URL, a meme body, and an author. The application downloads the image from the URL, overlays it with the user-provided text, and generates a meme.
   - Usage:
      - Access the form by visiting `/create` with a GET request.
      - Submit the form with a POST request containing the image URL, meme body, and author.

## CLI

### Usage

```bash
python3 meme.py [--path PATH] [--body BODY] [--author AUTHOR]
```

#### Options

- `--path`: Path to an image file. If not provided, a random image from the predefined collection will be used.
- `--body`: Quote body to add to the image. If not provided, a random quote will be selected.
- `--author`: Quote author to add to the image. Required if `--body` is used.

#### Examples

1. Generate a meme with a random image and a random quote:
   ```bash
   python3 cli.py
   ```

2. Generate a meme with a specific image and a random quote:
   ```bash
   python3 cli.py --path /path/to/your/image.jpg
   ```

3. Generate a meme with a specific image and a custom quote:
   ```bash
   python3 cli.py --path /path/to/your/image.jpg --body "Your custom quote here" --author "Custom Author"
   ```