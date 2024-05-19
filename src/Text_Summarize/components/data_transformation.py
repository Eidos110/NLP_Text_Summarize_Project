from src.Text_Summarize import logger
from src.Text_Summarize.entity.config_entity import DataTransformationConfig
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
import os



class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_examples_to_features(self, example_batch: dict) -> dict:
        """
        Convert a batch of examples to features using the tokenizer.

        Args:
            example_batch (dict): A batch of examples with 'dialogue' and'summary' keys.

        Returns:
            dict: A dictionary with 'input_ids', 'attention_mask', and 'labels' keys.
        """
        input_encodings = self.tokenizer(example_batch['dialogue'], max_length=1024, truncation=True)

        with self.tokenizer.as_target_tokenizer():
            target_encodings = self.tokenizer(example_batch['summary'], max_length=128, truncation=True)

        return {
            'input_ids': input_encodings['input_ids'],
            'attention_mask': input_encodings['attention_mask'],
            'labels': target_encodings['input_ids']
        }

    def process_and_save_data(self) -> None:
        """
        Load data from disk, convert examples to features, and save the result to disk.
        """
        try:
            dataset_corpus = load_from_disk(self.config.data_path)
            dataset_corpus_pt = dataset_corpus.map(self.convert_examples_to_features, batched=True)
            dataset_corpus_pt.save_to_disk(os.path.join(self.config.root_dir, "corpus_dataset"))
        except Exception as e:
            print(f"Error processing data: {e}")
