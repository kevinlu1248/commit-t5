from transformers import AutoTokenizer

from core.generator import CommitMessageGenerator

AutoTokenizer.from_pretrained(CommitMessageGenerator.model_name)
