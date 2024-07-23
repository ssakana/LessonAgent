from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import AutoPeftModelForCausalLM
from pathlib import Path
import json
import torch


model_path = 'openbmb/MiniCPM-2B-sft-bf16'
model_path = '/home/mio/here/model/MiniCPM-2B-sft-bf16'


if __name__ == '__main__':
    torch.manual_seed(0)
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, device_map='auto', trust_remote_code=True)
    # model = AutoPeftModelForCausalLM.from_pretrained(adapter_path, torch_dtype=torch.bfloat16, device_map='auto', trust_remote_code=True)  # load lora adapter
    samples_path = Path(__file__).parent.parent.parent / 'dataset' / 'en-samples-10.json'
    samples = json.loads(samples_path.read_text(encoding='utf-8'))
    responds, history = model.chat(tokenizer, samples[0]['input'])
    print(responds)
