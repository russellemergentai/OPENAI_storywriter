import os

from openai import OpenAI


def main():

    # Formulate the request
    # Open the file in read mode
    with open('input.txt', 'r') as file:
        # Read the entire content of the file into the 'prompt' string
        prompt = file.read()

    # Initialize the OpenAI client
    client = OpenAI(api_key=os.environ['OPENAIKEY'])

    # Get the response from the chat completion API
    # gpt-3.5-turbo
    # gpt-4
    completion = client.chat.completions.create(model="gpt-4",
                                                messages=[{
                                                    "role": "user",
                                                    "content": prompt
                                                }])

    # Extract the generated response
    response = completion.choices[0].message.content

    # Write the response to a file
    if response is not None:
        with open("output.txt", "w") as f:
            f.write(response)
    else:
        print("No response generated.")


if __name__ == "__main__":
    main()
