import click
import requests
import random

@click.command()
@click.option('--size', default=50, help='Size of the grid')
@click.option('--url', default='http://127.0.0.1:8000/iterate1000', help='URL of the iterate endpoint')
def generate_and_iterate_grid(size, url):
    # Generate a random grid
    grid = [[random.randint(0, 1) for _ in range(size)] for _ in range(size)]

    # Display the generated grid
    click.echo("Generated Grid:")
    for row in grid:
        click.echo(' '.join('*' if cell == 1 else ' ' for cell in row))

    # Send the grid to the iterate endpoint
    response = requests.post(url, json={"grid": grid})

    if response.status_code == 200:
        # Display the result grid
        result_grid = response.json().get("grid", [])
        click.echo("\nResult Grid:")
        for row in result_grid:
            click.echo(' '.join('*' if cell == 1 else ' ' for cell in row))
    else:
        click.echo(f"Error: {response.status_code} - {response.text}")

if __name__ == '__main__':
    generate_and_iterate_grid()