from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    root_dir: Path
    source_url: Path
    local_data_file: Path
    unzip_dir: Path

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path
    tokenizer_name: str
    train_path: Path
    val_path: Path
    test_path: Path

@dataclass
class DataTrainerConfig:
    num_train_epochs: int
    warmup_steps: int
    per_device_train_batch_size: int
    weight_decay: float
    logging_steps: int
    evaluation_strategy: int
    eval_steps: int
    save_steps: float
    gradient_accumulation_steps: int
    root_dir: Path
    model_ckpt: Path
    train_path: Path
    val_path: Path
    test_path: Path

@dataclass
class dataEvalutionConfig:
    root_dir: Path
    model_path: Path
    tokenizer_path: Path
    train_path: Path
    val_path: Path
    test_path: Path
    metric_file_name:Path