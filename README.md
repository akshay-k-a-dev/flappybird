# Flappy Bird in Python (Pygame)

This is a simple clone of the popular game Flappy Bird, implemented in Python using the Pygame library.

## Features

- **Classic Flappy Bird gameplay**: Navigate the bird through a series of pipes without crashing.
- **Customizable assets**: Modify the bird, background, ground, and pipe images to personalize the game.
- **Simple and lightweight**: The entire game is written in a single Python file (`main.py`).

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/akshay-k-a-dev/flappybird.git
   cd flappybird
   ```

2. **Install the required dependencies:**

   Make sure you have Python installed. Then, install Pygame using pip:

   ```bash
   pip install pygame
   ```

3. **Run the game:**

   Execute the `main.py` file to start the game:

   ```bash
   python main.py
   ```

## Assets

The following assets are included in the repository:

- `background.png`: The background image for the game.
- `bird.png`: The sprite image for the flappy bird.
- `ground.png`: The image used for the ground at the bottom of the screen.
- `pipe.png`: The image used for the pipes.

Feel free to replace these images with your own to customize the look of the game.

## How to Play

- Press the spacebar or click the mouse to make the bird flap its wings and fly higher.
- Avoid the pipes by navigating the bird through the gaps.
- The game ends when the bird collides with a pipe or the ground.

## Project Structure

```
├── __pycache__/        # Compiled Python files
├── build/main/         # Build files (optional)
├── dist/               # Distribution files (optional)
├── background.png      # Background image
├── bird.png            # Bird sprite
├── ground.png          # Ground image
├── main.py             # Main game logic
├── main.spec           # PyInstaller specification file
└── pipe.png            # Pipe image
```

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/akshay-k-a-dev/flappybird/issues).

## Acknowledgments

Special thanks to the creators of Flappy Bird and the Pygame library.
