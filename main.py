import os
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        raise RuntimeError("Gemini API key not found")

    client =  genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents='"Why is this repo such a great way to learn backend ai development? Use one paragraph maximum."'
    )
    print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
