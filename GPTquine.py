import openai

# Set your OpenAI API key here
api_key = "YOUR_OPENAI_API_KEY"

# Initialize the OpenAI API client
openai.api_key = api_key

# Define the prompt to ask ChatGPT to generate its own source code
prompt = "Generate the Python code for a program that prompts ChatGPT using the Python API to return its own source code."

# Use the completion endpoint to generate the source code
response = openai.Completion.create(
    engine="text-davinci-003",
    prompt=prompt,
    max_tokens=200,
    n=1,
    stop=None,
    temperature=0.7
)

# Print the generated source code
print(response.choices[0].text.strip())
