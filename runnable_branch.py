from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch
from dotenv import load_dotenv

load_dotenv()

prompt1 = PromptTemplate(
    template='write a detailed report on topic {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='summarize the following text \n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

model = ChatGroq(model='llama-3.1-8b-instant')

report_gen_chain = RunnableSequence(prompt1, model , parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split())>300, RunnableSequence(prompt2, model, parser)),
    RunnablePassthrough()
)

final_chain = RunnableSequence(report_gen_chain, branch_chain)

result = final_chain.invoke([{'topic':'Russia vs Ukraine'}])

print(result)