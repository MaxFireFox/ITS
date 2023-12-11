from math import ceil
import numpy as np
import cv2


def add_text(background, text: str, coordinates: tuple[int, int], font, scale: int,
             color: tuple[int, int, int], thickness: int):
    return cv2.putText(background.copy(), text, coordinates, font, scale, color=color, thickness=thickness)


def make_video(user_text: str, user_height=100, user_width=100, user_font=cv2.FONT_HERSHEY_COMPLEX, user_scale=1,
               user_color=(250, 250, 250), user_thickness=1):
    # задаём исходные данные
    height = user_height
    width = user_width
    image = np.zeros((height, width, 3), np.uint8)
    font = user_font
    scale = user_scale
    color = user_color
    thickness = user_thickness

    text = user_text
    text_size, baseline = cv2.getTextSize(text, user_font, user_scale, user_thickness)
    text_length = text_size[0]
    coordinates_initial = (width, height // 2 + text_size[1] // 2)
    frame_rate = 15
    step_f = (text_length + width) / (3 * frame_rate)
    step = int(step_f)
    step2 = ceil(step_f)
    if step_f - step < 0.5:
        step2 = step

    def add_text2(text: str, coordinates: tuple[int, int]):
        """
        This function returns frame with pre-defined parameters, such as background and
        font parameters. The only difference is text and coordinates

        :param text: text of the running string
        :param coordinates: position of the first character
        :return: frame with text on it
        """
        return add_text(image, text, coordinates, font, scale, color, thickness)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out_scr = cv2.VideoWriter("main/media/main/result.mp4", fourcc, frame_rate, (width, height))
    position = coordinates_initial[0]
    while position >= -text_length:
        frame = add_text2(text, (position, coordinates_initial[1]))
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        out_scr.write(frame)
        position -= step
