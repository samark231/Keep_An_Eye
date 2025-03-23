from google import genai
import json
import os
import sys

main_dir = os.path.abspath(os.path.join(os.path.dirname(__file__),"..",".."))
sys.path.append(main_dir)

response_text_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "response.txt"))
response_text_path2 = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "response2.txt"))
prompt_text_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "prompt.txt"))
all_articles_with_content_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "all_articles_with_content.json"))
final_prompt_text_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "finalPrompt.txt"))
ultimate_data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "data", "the_ultimate_data.json"))


def fetch_response_gemini(final_prompt, api_key):
    try:
        # Initialize Gemini client
        client = genai.Client(api_key=api_key)

        # Make the request
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=final_prompt
        )

        # Check if response contains candidates
        if not response or not hasattr(response, "candidates") or not response.candidates:
            return None, "No response from Gemini API"

        # Extract response text
        candidate = response.candidates[0]
        if not hasattr(candidate, "content") or not candidate.content.parts:
            return None, "Malformed response from Gemini API"

        gemini_response = candidate.content.parts[0].text
        # with open(response_text_path, "w") as f:
        #     f.write(gemini_response)
        # Ensure response has enough length before slicing
        if len(gemini_response) < 10:
            return None, "Gemini response is too short to process"

        modified_gemini_response = gemini_response[7:-3]  # Slicing safely

        # Parse JSON response
        try:
            ultimate_data = json.loads(modified_gemini_response)
            # with open(response_text_path2, "w") as source, open(ultimate_data_path, "w") as dest:
            #     source.write(modified_gemini_response)
            #     # print(type(ultimate_data))
            #     dest.write(json.dumps(ultimate_data))
        except json.JSONDecodeError:
            print("error in fetching gemini response.0 ")
            return None, "Failed to parse Gemini response as JSON"

        return ultimate_data, None

    except genai.GoogleGenerativeAIException as api_error:
        print("error in fetching gemini response. 1")
        return None, f"API error: {str(api_error)}"
    except Exception as e:
        print("error in fetching gemini response. 2")
        return None, f"Unexpected error: {str(e)}"


def generate_prompt(all_articles):
    with open(prompt_text_path, "r") as f:
        prompt = f.read()
    formatted_prompt = f"{prompt}".replace("{input_array}",  json.dumps(all_articles, indent=2))
    # with open(final_prompt_text_path, "w") as f3:
    #     f3.write(formatted_prompt)
    return formatted_prompt





