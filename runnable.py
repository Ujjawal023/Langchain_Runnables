import random
class nakliLLM:
    def __init__(self):
        print('LLM Created')

    def predict(self, prompt):
        response_list = [
            'delhi is capoital of india',
            'IPl is a cricket league',
            'AI stands for artificial Intelligence'
        ]
        return{'response': random.choice(response_list)}
    
llm = nakliLLM

llm.predict('what is the capital of india')

