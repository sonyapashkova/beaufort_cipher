class Beaufort_Error(Exception):
    pass


class Beaufort_Cipher:


    def __init__(self, alphabet, file_key):
        self.alphabet = alphabet
        self.__key = self.__load_key(file_key)
            

    def __load_key(self, file_name) -> str:
        """ Функция для загрузки ключа из файла """
        try:
            with open(file_name, "r", encoding="UTF-8") as file_in:
                key = file_in.read()
        except FileNotFoundError:
            raise Beaufort_Error(f"Не найден файл {file_name}")
        else:
            if len(key) == 0:
                raise Beaufort_Error("Длина ключа равна 0")
            for i in key:
                if i not in self.alphabet:
                    raise Beaufort_Error("Обнаружен неизвестный символ в ключе")
        return key


    def load_text(self, file_name) -> str:
        """ Функция для загрузки текста для шифрования """
        try:
            with open(file_name, "r", encoding="UTF-8") as file_in:
                text = file_in.read()
        except FileNotFoundError:
            raise Beaufort_Error(f"Не найден файл {file_name}")
        else:
            if len(text) == 0:
                raise Beaufort_Error(f"Пустой файл {file_name}")
            for word in text:
                for i in word:
                    if i not in self.alphabet:
                        raise Beaufort_Error(f"Обнаружен неизвестный символ '{i}' в слове {word}")
        return text


    def save_result(self, text, file_result):
        """ Функция для сохранения результатов """
        with open(file_result, "w", encoding="UTF-8") as file_out:
            print(text, file=file_out)


    def encode_text(self, text) -> str:
        """ Функция для шифрования текста """
        result = ""
        temp_key = (self.__key * (len(text)) + self.__key)[:len(text)]
        for i in range(len(text)):
            index_letter = (self.alphabet.index(temp_key[i]) - self.alphabet.index(text[i])) % len(self.alphabet)
            result += self.alphabet[index_letter]
        return result


    def decode_text(self, text):
        """ Функция для расшифрования текста """
        return self.encode_text(text)