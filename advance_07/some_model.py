class SomeModel:
    BASE_CONST = 1

    def predict(self, message):
        words = message.split()
        num_words = len(words)

        num_chars = 0
        for word in words:
            num_chars += len(word)

        res = SomeModel.BASE_CONST - num_words / max(num_chars, 1)
        # clipping
        res = max(0, res)
        return res


if __name__ == "__main__":
    model = SomeModel()
    print(model.predict("python python python"))
    print(model.predict("p p p p p p p p p p"))
    print(model.predict(" "))
    print(model.predict("good"))
    print(model.predict("bad"))
    print(model.predict("neutral"))
