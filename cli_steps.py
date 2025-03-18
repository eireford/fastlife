import click
import requests
import random
import time

@click.command()
@click.option('--size', default=50, help='Size of the grid')
@click.option('--url', default='http://127.0.0.1:8000/iterate100', help='URL of the iterate endpoint')
@click.option('--iterations', default=30, help='Number of iterations')
@click.option('--delay', default=1, help='Delay between iterations in seconds')
def generate_and_iterate_grid(size, url, iterations, delay):
    # Generate a random grid
    grid = [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

    for i in range(iterations):
        click.echo(f"\nIteration {i + 1}:")

        # Display the current grid
        for row in grid:
            click.echo(' '.join('*' if cell == 1 else ' ' for cell in row))

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