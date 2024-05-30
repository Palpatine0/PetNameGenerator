from langchain.llms import OpenAI
from dotenv import load_dotenv
# Imports the PromptTemplate class from the langchain library to create a prompt template.
from langchain.prompts import PromptTemplate
# Imports the LLMChain class from the langchain library to create a chain that links a language model and a prompt template.
from langchain.chains import LLMChain

load_dotenv()


def generate_pet_name(animal_type,pet_color):
    # Creates an instance of the OpenAI language model with a temperature setting of 1 for more creative responses.
    llm_OpenAI = OpenAI(temperature = 1)

    # Creates a PromptTemplate instance with input variable 'animal_type' and a template for generating pet names.
    prompt_template_name = PromptTemplate(
        input_variables = ['animal_type', 'pet_color'],
        template = "I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
    )

    # Creates an LLMChain instance that links the language model and the prompt template.
    name_chain = LLMChain(llm = llm_OpenAI, prompt = prompt_template_name,output_key="pet_name")

    # Generates a response from the language model by passing the animal_type to the prompt template through the LLMChain.
    response = name_chain({'animal_type': animal_type,'pet_color': pet_color})

    return response


if __name__ == "__main__":
    print(generate_pet_name('cat','red'))
