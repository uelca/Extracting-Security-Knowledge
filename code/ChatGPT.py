import openai


class ChatGPT:
    def __init__(self, api_key, role):
        openai.api_key = api_key
        self.dialog = [{"role": "system", "content": role}]

    def question(self, frage):
        self.dialog.append({"role": "user", "content": frage})
        result = openai.ChatCompletion.create(
            model='gpt-4',
            messages=self.dialog
        )
        answer = result.choices[0].message.content
        self.dialog.append({"role": "assistant", "content": answer})
