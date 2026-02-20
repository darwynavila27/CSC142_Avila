# Pygame demo text and buttons 

import pygame
import pygwidgets

pygame.init()

# Window setup
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Temperature Converter")

clock = pygame.time.Clock()

# Widgets 

inputBox = pygwidgets.InputText(window, (50, 50), width=200)

radioF = pygwidgets.TextRadioButton(window, (50, 120), "Convert to Fahrenheit", group=1, value=True)
radioC = pygwidgets.TextRadioButton(window, (50, 160), "Convert to Celsius", group=1)

convertButton = pygwidgets.TextButton(window, (50, 220), "Convert")

outputDisplay = pygwidgets.DisplayText(window, (50, 280), "", fontSize=24)

# Conversion Function

def convertTemperature():
    userText = inputBox.getValue()

    try:
        temp = float(userText)

        if radioF.getValue():  # Converting C → F
            result = temp * 9/5 + 32
            outputDisplay.setValue(f"{temp}°C = {result:.2f}°F")

        else:  # Converting F → C
            result = (temp - 32) / (9/5)
            outputDisplay.setValue(f"{temp}°F = {result:.2f}°C")

    except ValueError:
        outputDisplay.setValue("Please enter a valid number")


# Main 

running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Pressing Enter in TextInput
        if inputBox.handleEvent(event):
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                convertTemperature()

        # Changing radio button
        if radioF.handleEvent(event):
            pass  # Selection by group

        if radioC.handleEvent(event):
            pass

        # Pressing TextButton
        if convertButton.handleEvent(event):
            convertTemperature()

    window.fill((255, 255, 255))

    # Drawing the widgets
    inputBox.draw()
    radioF.draw()
    radioC.draw()
    convertButton.draw()
    outputDisplay.draw()

    pygame.display.update()
    clock.tick(30)

pygame.quit()