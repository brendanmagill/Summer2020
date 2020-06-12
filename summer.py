import arcade
import time

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 600
SCREEN_TITLE = "interface"

# *****************************************************************************
#       SOURCE:      https://arcade.academy/examples/gui_text_button.html
# *****************************************************************************
class TextButton:
    """ Text-based button """

    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
        """ Draw the button """
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                     self.height, self.face_color)

        if not self.pressed:
            color = self.shadow_color
        else:
            color = self.highlight_color

        # Bottom horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y - self.height / 2,
                         color, self.button_height)

        # Right vertical
        arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        if not self.pressed:
            color = self.highlight_color
        else:
            color = self.shadow_color

        # Top horizontal
        arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                         self.center_x + self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        # Left vertical
        arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                         self.center_x - self.width / 2, self.center_y + self.height / 2,
                         color, self.button_height)

        x = self.center_x
        y = self.center_y
        if not self.pressed:
            x -= self.button_height
            y += self.button_height

        arcade.draw_text(self.text, x, y,
                         arcade.color.BLACK, font_size=self.font_size,
                         width=self.width, align="center",
                         anchor_x="center", anchor_y="center")

    def on_press(self):
        self.pressed = True

    def on_release(self):
        self.pressed = False

def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(_x, _y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()

class StartTextButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Start", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class SpdUpTextButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 50, 20, "Up", 10, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class SpdDownTextButton(TextButton):
    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 50, 20, "Down", 10, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class Game(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.total_time = 0.0
        self.is_started = False

    def setup(self):
        """
        Set up the application.
        """
        arcade.set_background_color(arcade.color.DAVY_GREY)
        start_button = StartTextButton(450, 550, self.start_time)
        self.button_list.append(start_button)

        up_button = SpdUpTextButton(430, 334, self.faster)
        self.button_list.append(up_button)
        down_button = SpdDownTextButton(430, 304, self.slower)
        self.button_list.append(down_button)
        self.total_time = 0.0
        self.speed = 0.0
        self.pace_secs = 0
        self.distance = 0

    def on_draw(self):
        """ Use this function to draw everything to the screen. """

# *****************************************************************************
#       SOURCE:      https://arcade.academy/examples/timer.html
# *****************************************************************************

        # Start the render. This must happen before any drawing
        # commands. We do NOT need a stop render command.
        arcade.start_render()

        # Calculate minutes
        minutes = int(self.total_time) // 60

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.total_time) % 60

        # Figure out our output
        output = f"Time: {minutes:02d}:{seconds:02d}"
        arcade.draw_text(output, 20, 300, arcade.color.BLACK, 30)

# *****************************************************************************
#                                MY CODE
# *****************************************************************************

        self.speed_out = f"Speed: {self.speed:.1f}"
        arcade.draw_text(self.speed_out, 220, 300, arcade.color.BLACK, 30)

        pace_minutes = int(self.pace_secs) // 60
        pace_seconds = int(self.pace_secs) % 60
        pace_out = f"Pace: {pace_minutes:02d}:{pace_seconds:02d}"
        arcade.draw_text(pace_out, 475, 300, arcade.color.BLACK, 30)

        distance_out = f"Distance: {self.distance:.2f}"
        arcade.draw_text(distance_out, 670, 300, arcade.color.BLACK, 30)

        for button in self.button_list:
            button.draw()

    def start_time(self):
        self.is_started = True
        self.speed = 5.0
        self.pace_secs = 3600 / self.speed

    def faster(self):
        if self.speed_out != "Speed: 13.0" and self.is_started:
            self.speed += 0.1

    def slower(self):
        if self.speed_out != "Speed: 5.0" and self.is_started:
            self.speed -= 0.1

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        """
        if self.is_started:
            self.total_time += delta_time
            self.pace_secs = 3600 / self.speed
            self.distance += (self.speed * delta_time) / 3600

# *****************************************************************************
#                                DOCUMENTATION????
# *****************************************************************************


    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        check_mouse_release_for_buttons(x, y, self.button_list)

def main():
    window = Game()
    window.setup()
    arcade.run()

if __name__ == '__main__':
    main()
