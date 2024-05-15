import pyautogui
import cv2
import numpy as np

# Set FAILSAFE to True to prevent mouse from moving out of bounds
pyautogui.FAILSAFE = True

# Define screen_np in the global scope
screen_np = None

def find_button_with_confidence(image_path, confidence=0.8):
    """
    Locates an image on the screen with a confidence threshold to account for variations.

    Args:
        image_path (str): Path to the image file (e.g., 'facebook.jpg').
        confidence (float, optional): Confidence level for the image match (default: 0.8).

    Returns:
        tuple: Coordinates of the top-left corner of the found image (x, y), or None if not found.
    """
    global screen_np  # Access the global variable

    # Read the image in grayscale (improves performance)
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Capture the screenshot
    screen = pyautogui.screenshot()

    # Convert the PIL image to a NumPy array (RGB format)
    screen_np = np.array(screen)

    # Convert the screenshot to grayscale for template matching
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

    # Find the image on the screen
    result = cv2.matchTemplate(screen_gray, image, cv2.TM_CCOEFF_NORMED)  # Use normalized cross-correlation
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # Check if the match is above the confidence threshold
    if max_val >= confidence:
        print("Confidence:", max_val)
        return max_loc  # Return top-left coordinates
    else:
        return None 

# Find the button location with a confidence threshold of 0.8
button7location = find_button_with_confidence('logo.png', confidence=0.8)

if button7location is not None:
    # Get the screen size
    screen_width, screen_height = pyautogui.size()
    print("Screen size:", screen_width, screen_height)
    print("Button location:", button7location)

    # Check if the found location is within the screen bounds
    if 0 <= button7location[0] <= screen_width * 2 and 0 <= button7location[1] <= screen_height * 2:
        # Capture a portion of the screen containing the detected button
        button_width, button_height = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE).shape[::-1]
        button_area = screen_np[button7location[1]:button7location[1]+button_height, 
                                button7location[0]:button7location[0]+button_width]

        # Display the captured button area
        """while True:
            cv2.imshow('Detected Button', button_area)
            key = cv2.waitKey(0)

            # Check if the pressed key is the delete key (ASCII code 127)
            if key == 127:
                print("Button area deleted.")
                break

        cv2.destroyAllWindows()"""

        # Adjust the mouse movement to account for the offset
        adjusted_x = button7location[0] * .55 # Adjust x-coordinate by adding 5 pixels
        adjusted_y = button7location[1] * .50  # Adjust y-coordinate by adding 5 pixels

        # Move to the adjusted location and click
        pyautogui.moveTo(adjusted_x, adjusted_y)
        pyautogui.click()

        pyautogui.hotkey('ctrl', 'w')  # Adjust the hotkey based on the browser
        pyautogui.hotkey('command', 'w')  # Adjust the hotkey based on the browser

        print("Clicked the button at", (adjusted_x, adjusted_y))
    else:
        print("Found location is out of screen bounds.")
else:
    print("Couldn't find the button 'facebook.png' on the screen.")
