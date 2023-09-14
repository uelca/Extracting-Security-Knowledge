import openai
import time

class ChatGPT:
    def __init__(self, api_key, role):
        openai.api_key = api_key
        self.dialog = [{"role": "system", "content": role}]

    def question(self, question):
        self.dialog.append({"role": "user", "content": question})

        while True:
            try:
                result = openai.ChatCompletion.create(
                    model='gpt-4-32k',
                    messages=self.dialog
                )
                answer = result.choices[0].message.content
                self.dialog.append({"role": "assistant", "content": answer})
                return answer
            # If Rate Time Error is thrown, wait for 1 minute
            except openai.error.RateLimitError as e:
                # If rate limit is reached, wait for one minute and continue the requests
                print("Rate limit reached. Waiting for one minute and continuing requests...")
                time.sleep(60)  # Wait for 60 seconds (one minute) before sending the next request

