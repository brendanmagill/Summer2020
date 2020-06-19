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

# *****************************************************************************
#                                MY CODE
# *****************************************************************************

class StartTextButton(TextButton):
    """ Button for starting the treadmill. """

    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Start", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class PauseTextButton(TextButton):
    """ Button for pausing the treadmill. """

    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Pause", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class ResumeTextButton(TextButton):
    """ Button for resuming the treadmill. """

    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Resume", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class StopTextButton(TextButton):
    """ Button for stopping the treadmill. """

    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 100, 40, "Stop", 18, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class SpdUpTextButton(TextButton):
    """Button for increasing the treadmill's speed. """

    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 50, 20, "Up", 10, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class SpdDownTextButton(TextButton):
    """Button for decreasing the treadmill's speed. """

    def __init__(self, center_x, center_y, action_function):
        super().__init__(center_x, center_y, 50, 20, "Down", 10, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()

class StopView(arcade.View):
    """ View to display after the treadmill is stopped. """

    def __init__(self, time, distance):
        super().__init__()
        self.total_time = time
        self.distance = distance

    def on_draw(self):
        """ Draw the view """

        arcade.start_render()

        minutes = int(self.total_time) // 60
        seconds = int(self.total_time) % 60

        time_out = f"You ran for {minutes:02d}:{seconds:02d}"
        arcade.draw_text(time_out, 350, 400, arcade.color.BLACK, 30)

        distance_out = f"You ran {self.distance:.2f} miles"
        arcade.draw_text(distance_out, 350, 300, arcade.color.BLACK, 30)

        pace = self.total_time / self.distance
        pace_minutes = int(pace) // 60
        pace_seconds = int(pace) % 60

        pace_out = f"Average pace: {pace_minutes:02d}:{pace_seconds:02d}"
        arcade.draw_text(pace_out, 340, 200, arcade.color.BLACK, 30)

class Game(arcade.View):
    """ The main interface view. """

    def __init__(self):
        super().__init__()

        self.total_time = 0.0
        self.is_started = False
        self.is_paused = False

    def setup(self):
        """ Set up the window. """

        arcade.set_background_color(arcade.color.DAVY_GREY)

        start_button = StartTextButton(330, 550, self.start_time)
        self.button_list.append(start_button)

        pause_button = PauseTextButton(450, 550, self.pause)
        self.button_list.append(pause_button)

        resume_button = ResumeTextButton(450, 500, self.resume)
        self.button_list.append(resume_button)

        stop_button = StopTextButton(570, 550, self.stop)
        self.button_list.append(stop_button)

        up_button = SpdUpTextButton(430, 334, self.faster)
        self.button_list.append(up_button)

        down_button = SpdDownTextButton(430, 304, self.slower)
        self.button_list.append(down_button)

        self.total_time = 0.0
        self.speed = 0.0
        self.pace_secs = 0
        self.distance = 0

    def on_draw(self):
        """ Draws the view. """

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
        """ Starts the treadmill at the default speed. """

        self.is_started = True
        self.speed = 5.0
        self.pace_secs = 3600 / self.speed

    def pause(self):
        if self.is_started:
            self.is_paused = True

    def resume(self):
        self.is_paused = False

    def stop(self):
        """ Stops the treadmill and displays the final view. """

        if self.is_started:
            self.is_started = False
            view = StopView(self.total_time, self.distance)
            self.window.show_view(view)


    def faster(self):
        """ Increases the speed, up to the maximum. """

        if self.speed_out != "Speed: 13.0" and self.is_started:
            self.speed += 0.1

    def slower(self):
        """ Decreases the speed, down to the minimum. """

        if self.speed_out != "Speed: 5.0" and self.is_started:
            self.speed -= 0.1

    def on_update(self, delta_time):
        """ Updates the time, pace, and distance. """
        if self.is_started and not self.is_paused:
            self.total_time += delta_time
            self.pace_secs = 3600 / self.speed
            self.distance += (self.speed * delta_time) / 3600


    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when a button is pressed. """

        check_mouse_press_for_buttons(x, y, self.button_list)

    def on_mouse_release(self, x, y, button, key_modifiers):
        """ Called when a button is released. """

        check_mouse_release_for_buttons(x, y, self.button_list)

def main():
    """Runs the interface. """

    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    main_view = Game()
    window.show_view(main_view)
    main_view.setup()
    arcade.run()

if __name__ == '__main__':
    main()
