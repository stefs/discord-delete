import contextlib
import time
import typing

import pyautogui


class DiscordDelete(object):
    TEMPLATE_NAME = 'template_name.png'
    TEMPLATE_DELETE = 'template_delete.png'
    TEMPLATE_AVOID = 'template_avoid.png'
    TEMPLATE_CONFIRM = 'template_confirm.png'
    OFFSET_NAME_TO_MESSAGE_MENU = 768, 28

    def run(self) -> typing.NoReturn:
        print('Fail-Safe: Move the mouse cursor to the upper left corner of the screen')
        counter = 1
        start = time.time()
        while True:
            try:
                print(f'Delete message {counter} ...', end='')
                self.delete_message()
                speed = (time.time() - start) / counter
                counter += 1
                print(f' done ({speed:.1f} seconds per message)')
            except PageDone as exc:
                print(f' {exc}')
                print('Scroll ...', end='')
                pyautogui.press('pgdn')
                time.sleep(0.7)
                print(' done')

    def delete_message(self) -> None:
        # move to name by template
        try:
            location = self.locate(self.TEMPLATE_NAME)
        except TemplateNotFound:
            raise PageDone('no message found')
        pyautogui.moveTo(*location)
        # move to message menu by offset
        pyautogui.move(self.OFFSET_NAME_TO_MESSAGE_MENU)
        # find scroll button by template and avoid it
        with contextlib.suppress(TemplateNotFound):
            location_avoid = self.locate(self.TEMPLATE_AVOID)
            location_mouse = pyautogui.position()
            if abs(location_mouse.y - location_avoid.y) < 30:
                raise PageDone('avoiding scroll button')
        # open message menu
        pyautogui.click()
        time.sleep(0.2)
        # move to delete by template and click it
        try:
            location = self.locate(self.TEMPLATE_DELETE)
        except TemplateNotFound:
            # FIXME: This also triggers on call messages, because they don't have a message menu,
            #        so messages to delete might be skipped.
            raise PageDone('delete menu not found')
        pyautogui.moveTo(*location)
        pyautogui.click()
        time.sleep(0.4)
        # move to confirm button by template and click it
        location = self.locate(self.TEMPLATE_CONFIRM)
        pyautogui.moveTo(*location)
        pyautogui.click()
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
    discord_delete = DiscordDelete()
    discord_delete.run()


if __name__ == '__main__':
    main()
