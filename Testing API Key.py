import openai
# Set your API key here
openai.api_key = "sk-"

# Make the API call
response = openai.Completion.create(engine="davinci", prompt="Hello, world!")

# Print the result
print(response.choices[0].text)
