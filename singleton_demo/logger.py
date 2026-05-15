class Logger:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            print("Creando la única instancia del Logger")
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def log(self, message):
        print(f"[LOG]: {message}")