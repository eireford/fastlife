# Conway's Game of Life with TensorFlow

This project implements Conway's Game of Life using TensorFlow to leverage hardware acceleration for running iterations efficiently.

## Features

- Hardware-accelerated iterations using TensorFlow
- Command-line interface (CLI) for running the simulation
- JSON formatted output for easy integration and analysis

## Requirements

- Python 3.7+
- TensorFlow 2.x
- Click
- Requests

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    cd your-repo-name
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

Run the CLI to start the simulation:
```sh
python main.py --url http://127.0.0.1:8000/iterate --iterations 400 --delay 0
```

## Configuration

- `--url`: URL of the iterate endpoint (default: `http://127.0.0.1:8000/iterate`)
- `--iterations`: Number of iterations to run (default: 400)
- `--delay`: Delay between iterations in seconds (default: 0)

## Example

```sh
python main.py --url http://127.0.0.1:8000/iterate --iterations 100 --delay 1
```

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Acknowledgements

- [TensorFlow](https://www.tensorflow.org/)
- [Click](https://click.palletsprojects.com/)
- [Requests](https://docs.python-requests.org/)