from crewai.flow.flow import Flow, start, listen
from dotenv import load_dotenv, find_dotenv#load key,
from litellm import completion
_: bool = load_dotenv(find_dotenv())#key direct load

class PANAFlow(Flow):

    @start()
    def generate_topic(self):  #(2025 ka top trend vo topic select krky de use litellm)
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[
                {
                    "role": "user",
                    "content": """
                            Share the most trending topic topic in AI world. Only share the other text."""
                }
            ]
            
            # max_tokens=100,
            # temperature=0.5
        )
        self.state['topic'] = response['choices'][0]['message']['content']
        print(f"STEP 1 Topics: {self.state['topic']}")

def kickoff():
    flow = PANAFlow()
    flow.kickoff()
