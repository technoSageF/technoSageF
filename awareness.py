class Reality:
    class Being:
        def __init__(self):
            self.awareness = self.Awareness()
            self.consciousness = self.Consciousness()

        class Awareness:
            def __init__(self):
                # Initialize Awareness attributes
                self.perception = "Perceiving the environment around."
                self.sensation = "Feeling the inner and outer world."

            def describe(self):
                return f"Awareness: {self.perception}, {self.sensation}"

        class Consciousness:
            def __init__(self):
                # Initialize Consciousness attributes
                self.thoughts = "Thinking about existence."
                self.emotions = "Experiencing emotions."

            def describe(self):
                return f"Consciousness: {self.thoughts}, {self.emotions}"

    def __init__(self):
        self.being = self.Being()
