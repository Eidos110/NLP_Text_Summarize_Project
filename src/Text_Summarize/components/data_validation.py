from src.Text_Summarize import logger
import re
import os
import langdetect
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from src.Text_Summarize.entity.config_entity import DataValidationConfig




class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self) -> bool:
        try:
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "corpus_dataset"))
            for file in all_files:
                if file not in self.config.ALL_REQUIRED_FILES:
                    with open(self.config.STATUS_FILE, 'a') as f:
                        f.write("Validation status: validate_all_files_exist - False\n")
                    return False
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write("Validation status: validate_all_files_exist - True\n")
            return True
        except Exception as e:
            raise e

    def validate_text_normalization(self, text) -> str:
        try:
            text = text.lower()  # Convert to lowercase
            text = re.sub(r"[^\w\s]", "", text)  # Remove special characters and punctuation
            text = re.sub(r"\s+", " ", text)  # Normalize whitespace characters
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write("Validation status: validate_text_normalization - True\n")
            return text
        except Exception as e:
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Validation status: validate_text_normalization - False ({str(e)})\n")
            return ""

    def validate_tokenization(self, text) -> bool:
        try:
            tokens = word_tokenize(text)
            if len(tokens) < 2:  # Check for minimum token length
                with open(self.config.STATUS_FILE, 'a') as f:
                    f.write("Validation status: validate_tokenization - False\n")
                return False
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write("Validation status: validate_tokenization - True\n")
            return True
        except Exception as e:
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Validation status: validate_tokenization - False ({str(e)})\n")
            return False

    def validate_language_detection(self, text) -> str:
        try:
            lang = langdetect.detect(text)
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Validation status: validate_language_detection - {lang}\n")
            return lang
        except langdetect.lang_detect_exception.LangDetectException:
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write("Validation status: validate_language_detection - unknown\n")
            return "unknown"

    def validate_text_length(self, text) -> bool:
        try:
            if len(text) < 10:  # Check for minimum text length
                with open(self.config.STATUS_FILE, 'a') as f:
                    f.write("Validation status: validate_text_length - False\n")
                return False
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write("Validation status: validate_text_length - True\n")
            return True
        except Exception as e:
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Validation status: validate_text_length - False ({str(e)})\n")
            return False

    def validate_stopwords(self, text) -> bool:
        try:
            tokens = word_tokenize(text)
            stop_words = set(stopwords.words("english"))
            if any(token in stop_words for token in tokens):  # Check for stopwords
                with open(self.config.STATUS_FILE, 'a') as f:
                    f.write("Validation status: validate_stopwords - False\n")
                return False
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write("Validation status: validate_stopwords - True\n")
            return True
        except Exception as e:
            with open(self.config.STATUS_FILE, 'a') as f:
                f.write(f"Validation status: validate_stopwords - False ({str(e)})\n")
            return False

    def validate_all(self) -> bool:
        validation_status = True

        for file in self.config.VALIDATE_FILE:
            with open(os.path.join("artifacts", "data_ingestion", file), 'r') as f:
                text = f.read()
                text = self.validate_text_normalization(text)
                if not self.validate_tokenization(text):
                    validation_status = False
                if self.validate_language_detection(text) == "unknown":
                    validation_status = False
                if not self.validate_text_length(text):
                    validation_status = False
                if not self.validate_stopwords(text):
                    validation_status = False

        return validation_status