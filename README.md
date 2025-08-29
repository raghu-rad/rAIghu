# rAIghu
Making something...

## Current Model
[https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF](https://huggingface.co/bartowski/Llama-3.2-3B-Instruct-GGUF)

**Available Hardware:** RTX 3070  
**Quantization:** Q6_K

## Environment
**CUDA Version:** 12.6

Create a new `uv` environment and install vLLM (instructions [https://docs.vllm.ai/en/latest/getting_started/installation/gpu.html#set-up-using-python](here))

## Serve Model

```bash
vllm serve Llama-3.2-3B-Instruct-Q6_K.gguf \
    --tokenizer meta-llama/Llama-3.2-3B-Instruct \
    --gpu-memory-utilization 0.8 \
    --max-model-len 2048
```

Model is available on port `8000`. Example POST command:

```bash
curl -X POST http://localhost:8000/v1/chat/completions -H "Content-Type: application/json" -d '{"model": "Llama-3.2-3B-Instruct-Q6_K.gguf", "messages": [{"role": "user", "content": "How are you doing?"}], "max_tokens": 100, "temperature": 0.7}'
```
