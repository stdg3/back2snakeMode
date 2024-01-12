class TextProcessor:
    PUNKTUATION = '.,!?::'

    def __is_punktuaiton(self, char):
        return char in TextProcessor.PUNKTUATION
    
    def get_clean_string(self, text):
        clean_text = ""

        for char in text:
            if self.__is_punktuaiton(char):
                continue

            clean_text += char
        
        return clean_text

# tp = TextProcessor()
# print(tp.get_clean_string("Hello, world!"))
    
    
class TextLoader:
    def __init__(self) -> None:
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text=text)

    @property
    def clean_string(self):
        print("Clean string: ", self.__clean_string)
        return self.__clean_string
    

class DataInterface:
    def __init__(self) -> None:
        self.__text_loader = TextLoader()

    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_string(text=text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts


di = DataInterface()
t = ["hello, world!", "python!"]
di.process_texts(t)


