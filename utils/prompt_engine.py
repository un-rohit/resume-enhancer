import openai
openai.api_key = "your-openai-key"

def generate_prompt(name, skills, role):
    return f"Write a resume summary for {name}, targeting a {role} role. Highlight experience with {skills}. Keep it concise and impactful."

def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()
