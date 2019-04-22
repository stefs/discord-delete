import contextlib
import time

import pyautogui


class TemplateNotFound(Exception):
    pass


class PageDone(Exception):
    pass


class Screen(object):
    TEMPLATE_NAME = 'template_name.png'
    TEMPLATE_AVOID = 'template_avoid.png'
    TEMPLATE_CONFIRM = 'template_confirm.png'
    OFFSET_MENU = 768, 28
    OFFSET_ACTION = 0, 143

    def loop(self):
        while True:
            try:
                self.delete()
            except PageDone:
                pyautogui.press('pgdn')
                time.sleep(0.9)

    def delete(self):
        print('template name')
        try:
            location = self.locate(self.TEMPLATE_NAME)
            pyautogui.moveTo(*location)
        except TemplateNotFound:
            raise PageDone

        print('avoid scroll button')
        pyautogui.move(self.OFFSET_MENU)
        with contextlib.suppress(TemplateNotFound):
            location_avoid = self.locate(self.TEMPLATE_AVOID)
            location_mouse = pyautogui.position()
            if abs(location_mouse.y - location_avoid.y) < 30:
                raise PageDone

        print('open message menu')
        pyautogui.click()
        time.sleep(0.2)

        print('click delete')
        pyautogui.move(*self.OFFSET_ACTION)
        pyautogui.click()
        time.sleep(0.2)

        print('click confirm')
        location = self.locate(self.TEMPLATE_CONFIRM)
        pyautogui.moveTo(*location)
        pyautogui.click()
        time.sleep(0.2)

    @staticmethod
    def locate(template):
        location = pyautogui.locateOnScreen(template, confidence=0.8)
        if location is None:
            raise TemplateNotFound
        return pyautogui.center(location)


def main():
    screen = Screen()
    screen.loop()


if __name__ == '__main__':
    main()
