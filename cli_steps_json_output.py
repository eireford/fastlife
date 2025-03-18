import click
import requests
import time
import json

@click.command()
@click.option('--url', default='http://127.0.0.1:8000/iterate', help='URL of the iterate endpoint')
@click.option('--iterations', default=11, help='Number of iterations')
@click.option('--delay', default=0, help='Delay between iterations in seconds')
def generate_and_iterate_grid(url, iterations, delay):
    # Hard-coded start grid
    grid = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    for i in range(iterations):
        click.echo(f"\nIteration {i + 1}:")

        # Display the current grid with each row on a single line
        for row in grid:
            click.echo(json.dumps(row))

        # Send the grid to the iterate endpoint
        response = requests.post(url, json={"grid": grid})

        if response.status_code == 200:
            # Update the grid with the result
            grid = response.json().get("grid", [])
        else:
            click.echo(f"Error: {response.status_code} - {response.text}")
            break

        # Wait for the specified delay
        time.sleep(delay)

if __name__ == '__main__':
    generate_and_iterate_grid()