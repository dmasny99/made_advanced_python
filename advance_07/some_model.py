class SomeModel:
    BASE_CONST = 1

    def predict(self, message):
        words = message.split()
        num_words = len(words)

        num_chars = 0
        for word in words:
            num_chars += len(word)

        res = SomeModel.BASE_CONST - num_words / num_chars
        # clipping
        res = max(0, res)
        return res


if __name__ == "__main__":
    model = SomeModel()
    print(model.predict("python python python"))
    print(model.predict("p p p p p p p p p pyli"))
