import uvicorn
from fastapi import FastAPI, Request, Form
from transformers import GPT2Tokenizer, GPT2LMHeadModel
from pydantic import BaseModel

model = GPT2LMHeadModel.from_pretrained("gpt2")
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")


class GenerateRequest(BaseModel):
    prompt: str


app = FastAPI()


@app.post("/generate")
def generate(request: Request, data: GenerateRequest):
    model = GPT2LMHeadModel.from_pretrained("gpt2")
    tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
    input_ids = tokenizer.encode(data.prompt, return_tensors="pt")
    generated = model.generate(
        input_ids, max_length=1024, do_sample=True, top_p=0.95, top_k=60,
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(generated.tolist()[0], skip_special_tokens=True)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
