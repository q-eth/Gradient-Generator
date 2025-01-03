# Gradient generator
Generates a linear gradient with a desired angle of direction in a PNG format.
# Implemented functions
This code consists of 2 functions: `hex_to_rgba` and `generate_gradient`.
## hex_to_rgba
The `hex_to_rgba` function converts a hexadecimal color code into an RGBA (Red, Green, Blue, Alpha) tuple. It supports both formats:\
**#RRGGBB** (without alpha channel),\
**#RRGGBBAA** (with alpha channel).

### Signature
`def hex_to_rgba(hex_color: str) -> tuple[int, int, int, int]`

### Parameters
`hex_color (str)`: A string representing a hexadecimal color code. It must contain either:\
6 characters (**RRGGBB**) for red, green, and blue components, or\
8 characters (**RRGGBBAA**) for red, green, blue, and alpha components.
### Return 
`tuple[int, int, int, int]`: A tuple containing four integers, each in the range `[0, 255]`:\
**Red (R)**,\
**Green (G)**,\
**Blue (B)**,\
**Alpha (A)** — defaulted to 255 if not provided.
### Raise
`ValueError`: If the input string is not in the correct format or length.
### Examples of use
Correct without alpha:
>color = hex_to_rgba("#FF5733")\
>print(color)  # Output: (255, 87, 51, 255)

Correct with alpha:
>color = hex_to_rgba("#FF573380")\
>print(color)  # Output: (255, 87, 51, 128)

Incorrect:
>try:\
>color = hex_to_rgba("#MF5733")  # M in the hexadecimal number\
>except ValueError as err:\
> print(err)  # Output: "ValueError: invalid literal for int() with base 16: 'MF'"

## generate_gradient
The `generate_gradient` function creates an image of a gradient based on user-specified colors, positions, size, and angle. The generated gradient is saved as a PNG file to a desired path.
### Signature
`def generate_gradient(width: int, height: int, colors: list[tuple[str, float]], angle: float, output_path: str) -> None`
### Parameters
`width (int)`: The width of the generated image in pixels.\
`height (int)`: The height of the generated image in pixels.\
`colors (list[tuple[str, float]])`: A list of tuples specifying the colors and their positions along the gradient.
#### Color: A string in hexadecimal format (**#RRGGBB** or **#RRGGBBAA**).
#### Position: A float between 0.0 and 1.0 indicating the relative position of the color in the gradient.
#### Example:
>("#FF0000FF", 0.0),  # Red at position 0\
>("#00FF0080", 0.5),  # Semi-transparent Green at position 0,5\
>("#0000FFFF", 1.0)   # Blue at position 1

`angle (float)`: The angle of the gradient in degrees.
>Example: 45.0 (45 degrees)

`output_path (str)`: The full file path (including the name) where the image will be saved (replace `\` with `\\`).
>Example: "C:\\\Users\\\User\\\Pictures\\\gradient.png"

### Return
`None`
### Limitations
Reqiress the `Pillow` libary to be installed.

