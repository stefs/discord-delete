import contextlib
import time
import typing

import pyautogui


class Screen(object):
    TEMPLATE_NAME = 'template_name.png'
    TEMPLATE_DELETE = 'template_delete.png'
    TEMPLATE_AVOID = 'template_avoid.png'
    TEMPLATE_CONFIRM = 'template_confirm.png'
    OFFSET_MENU = 768, 28

    def loop(self) -> typing.NoReturn:
        while True:
            try:
                self.delete()
            except PageDone:
                print('Scroll ...', end='')
                pyautogui.press('pgdn')
                time.sleep(0.7)
                print(' done.')

    def delete(self) -> None:
        # move to name by template
        print('Delete message ...', end='')
        try:
            location = self.locate(self.TEMPLATE_NAME)
            pyautogui.moveTo(*location)
        except TemplateNotFound:
            raise PageDone
        # move to message menu by offset
        pyautogui.move(self.OFFSET_MENU)
        # find scroll button by template and avoid it
        with contextlib.suppress(TemplateNotFound):
            location_avoid = self.locate(self.TEMPLATE_AVOID)
            location_mouse = pyautogui.position()
            if abs(location_mouse.y - location_avoid.y) < 30:
                raise PageDone
        # open message menu
        pyautogui.click()
        time.sleep(0.2)
        # move to delete by template and click it
        location = self.locate(self.TEMPLATE_DELETE)
        pyautogui.moveTo(*location)
        pyautogui.click()
        time.sleep(0.2)
        # move to confirm button by template and click it
        location = self.locate(self.TEMPLATE_CONFIRM)
        pyautogui.moveTo(*location)
        pyautogui.click()
        print(' done.')
        time.sleep(0.2)

    @staticmethod
    def locate(template: str) -> pyautogui.Point:
        location = pyautogui.locateOnScreen(template, confidence=0.8)
        if location is None:
            raise TemplateNotFound
        return pyautogui.center(location)


class TemplateNotFound(Exception):
    pass


class PageDone(Exception):
    pass


def main() -> typing.NoReturn:
    screen = Screen()
    screen.loop()


if __name__ == '__main__':
    main()
