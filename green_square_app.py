import pyglet
import sys
from pyglet.shapes import Rectangle

# Ensure the OpenGL context is created
config = pyglet.gl.Config(double_buffer=True)
window = pyglet.window.Window(config=config, width=200, height=200, style=pyglet.window.Window.WINDOW_STYLE_BORDERLESS)
window.set_location((window.screen.width - window.width) // 2, (window.screen.height - window.height) // 2)
window.set_visible(False)  # Start invisible

# Set the window to be always on top
window.set_exclusive_mouse(True)

# Set the window to be always on top
window.set_visible(True)

# Create a green square using pyglet.shapes
@window.event
def on_draw():
    window.clear()
    # Create a rectangle for the square
    square = Rectangle(0, 0, window.width, window.height, color=(0, 255, 0))
    # Draw the rectangle
    square.draw()

# Show the window
window.set_visible(True)

# Check for the special parameter
stay_open = '--stay-open' in sys.argv

# Schedule the window to close after 5 seconds if not staying open
if not stay_open:
    pyglet.clock.schedule_once(lambda dt: window.close(), 5)

# Ensure the application exits when the window is closed
@window.event
def on_close():
    pyglet.app.exit()

# Run the application
pyglet.app.run() 