from isaac import Codelet


class HelloWorld(Codelet):
    def start(self):
        self.tick_periodically(1)

    def tick(self):
        print("hello world!")
