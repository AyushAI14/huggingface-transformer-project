import os
from src.logging import logger
from transformers import AutoTokenizer
from datasets import load_from_disk,Dataset
import pandas as pd
from src.entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def converting_into_s2s(self, row):
        dialogue = str(row['dialogue']) if pd.notnull(row['dialogue']) else ""
        summary = str(row['summary']) if pd.notnull(row['summary']) else ""
        
        input_encoding = self.tokenizer(dialogue, max_length=1024, truncation=True)
        target_encoding = self.tokenizer(text_target=summary, max_length=1024, truncation=True)

        row['input_ids'] = input_encoding['input_ids']
        row['attention_mask'] = input_encoding['attention_mask']
        row['labels'] = target_encoding['input_ids']
        return row


    def convert(self):
        df_train = pd.read_csv(self.config.train_path)
        df_val = pd.read_csv(self.config.val_path)
        df_test = pd.read_csv(self.config.test_path)

        tokenized_df_train = df_train.apply(self.converting_into_s2s, axis=1).reset_index(drop=True)
        tokenized_df_val = df_val.apply(self.converting_into_s2s, axis=1).reset_index(drop=True)
        tokenized_df_test = df_test.apply(self.converting_into_s2s, axis=1).reset_index(drop=True)

        train_dataset = Dataset.from_pandas(tokenized_df_train)
        val_dataset = Dataset.from_pandas(tokenized_df_val)
        test_dataset = Dataset.from_pandas(tokenized_df_test)

        train_dataset.save_to_disk(os.path.join(self.config.root_dir, "samsum-dataset", "train"))
        val_dataset.save_to_disk(os.path.join(self.config.root_dir, "samsum-dataset", "val"))
        test_dataset.save_to_disk(os.path.join(self.config.root_dir, "samsum-dataset", "test"))
