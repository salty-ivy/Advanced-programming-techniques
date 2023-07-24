"""
By using the Chain of Responsibility pattern, we provide a chance to a number of different objects to satisfy a specific request.
This is useful when we don’t know which object should satisfy a request in advance.
"""


class Event:
    """
    Simple event class.
    """

    def __init__(self, name="Default event"):
        self.name = name

    def __str__(self):
        return self.name


class Widget:
    """
    parent will be its instance could be from multiple classes inherited by widget.
    main code that handles the chain of responsibility.
    """

    def __init__(self, parent=None):
        self.parent = parent

    # Responsibility handler
    def handle(self, event: Event):
        handler = f"handle_{event}"

        if hasattr(self, handler):
            method = getattr(self, handler)
            method(event)
        elif self.parent is not None:
            self.parent.handle(event)
        elif hasattr(self, "handle_default"):
            self.handle_default(event)


class MainWindow(Widget):
    def handle_close(self, event: Event):
        print(f"MainWindow: {event}")

    def handle_default(self, event):
        print(f"MainWindow Default: {event}")


class SendDialog(Widget):
    def handle_paint(self, event):
        print(f"SendDialog: {event}")


class MsgText(Widget):
    def handle_down(self, event):
        print(f"MsgText: {event}")


def main():
    # creating a chain
    mw = MainWindow()
    sd = SendDialog(mw)
    msg = MsgText(sd)
    for e in ('down', 'paint', 'unhandled', 'close'):
        evt = Event(e)
        print(f'Sending event -{evt}- to MainWindow')
        mw.handle(evt)
        print(f'Sending event -{evt}- to SendDialog')
        sd.handle(evt)
        print(f'Sending event -{evt}- to MsgText')
        msg.handle(evt)


if __name__ == "__main__":
    main()
