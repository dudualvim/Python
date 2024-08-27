from llama_index import SimpleDirectoryReader, VectorStoreIndex, LLMPredictor, PromptHelper
from langchain import OpenAI
import gradio as gr
import sys
import os

os.environ["OPENAI_API_KEY"] = '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'

def construct_index(directory_path):
    max_input_size = 4096
    num_outputs = 512
    max_chunk_overlap = 20
    chunk_size_limit = 600

    prompt_helper = PromptHelper(max_input_size, num_outputs, max_chunk_overlap, chunk_size_limit=chunk_size_limit)

    llm_predictor = LLMPredictor(llm=OpenAI(temperature=0.7, model_name="text-davinci-003", max_tokens=num_outputs))

    documents = SimpleDirectoryReader(directory_path).load_data()

    index = GPTSimpleVectorIndex(documents, llm_predictor=llm_predictor, prompt_helper=prompt_helper)

    index.save_to_disk('index.json')

    return index  # Corrigir o retorno para retornar a instância do índice

def chatbot(texto_de_entrada):
    index = GPTSimpleVectorIndex.load_from_disk('index.json')
    response = index.query(texto_de_entrada, response_mode="compact")  # Corrigir o uso da variável
    return response.response

iface = gr.Interface(
    fn=chatbot,
    inputs=gr.Textbox(label="Introduza o seu texto"),  # Corrigido para usar gr.Textbox
    outputs="text",  # Alterado para "text" em vez de "texto"
    title="O meu chatbot de IA"
)

index = construct_index("docs")  # Corrigir para atribuir o retorno da função a 'index'
iface.launch(share=True)
