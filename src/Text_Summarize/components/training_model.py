from src.Text_Summarize.entity.config_entity import TrainingModelConfig
import os
from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch


#os.environ['HUGGINGFACE_HUB_CACHE'] = 'E:\\C.TSUBASA\\.cache\\huggingface\\hub'

class TrainingModel:
    def __init__(self, config: TrainingModelConfig):
        self.config = config


    
    def train(self):
        device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        print(f"Device: {device}")

    
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model_pegasus)

        dataset_corpus_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=1e6,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps

        )

        trainer = Trainer(
            model = model_pegasus,
            args=trainer_args,
            tokenizer=tokenizer,
            data_collator=seq2seq_data_collator,
            train_dataset=dataset_corpus_pt["train"],
            eval_dataset=dataset_corpus_pt["validation"]
        )

        trainer.train()


        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus-corpus-model"))
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))


