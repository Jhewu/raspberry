from llama_cpp import Llama

MAX_TOKEN = 256

# Path to your safetensors file
model_path = "quantized_model/unsloth.Q8_0.gguf"

# Load the model and tokenizer
llm = Llama(
    model_path=model_path,
    temperature=0.7,  # Adjust as needed
    max_tokens=MAX_TOKEN,   # Adjust as needed
    n_ctx=512,       # Context window size
    verbose=False
)

prompt = "I hate Asian"

def stream_output(llm_instance):
    response = llm_instance.create_completion(
        prompt=prompt,
        max_tokens=MAX_TOKEN, 
        echo=False,
        stop=["User:", "Assistant:", "<|endoftext|>", "</s>", "<|end_of_text|>", "Q:"],
        stream=True  # Enable streaming mode
    )
    
    print(prompt, end='', flush=True)  
    text = ''
    for token in response:
        if 'choices' not in token or len(token['choices']) == 0: continue
        choice = token['choices'][0]
        
        if 'text' in choice:
            new_text = choice['text']
            
            # Print the new text as it comes in (you can also process each token here)
            print(new_text, end='', flush=True)  
            
            text += new_text
        
    return text

# Use the function to stream output
full_response = stream_output(llm)