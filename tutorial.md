# Pet Name Generator

## Objective
In this lab, we will build a "Pet Name Generator" application using LangChain for language model interactions and Streamlit for the web interface. This guide will walk you through each step of the project, explaining key concepts and implementation details.

## Prerequisites
Before starting, ensure you have the following installed on your system:
- Python 3.7 or higher
- pip (Python package installer)
- Git (optional)

### Step 1: Initial Setup
#### 1. Environment Setup
To start, we need to manage sensitive information such as API keys securely. Using a `.env` file is a standard practice for this purpose.

1. **Create a `.env` file:**
   - This file will store your OpenAI API key. Ensure it is included in your `.gitignore` file to prevent it from being committed to your repository.

   Example `.env` file:
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```

2. **Install required packages:**
   - We need several packages for our project: `langchain`, `openai`, `streamlit`, `python-dotenv`, and `langchain_community`.

   Commands:
   ```bash
   pip install langchain openai streamlit python-dotenv
   ```
   ```bash
   pip install langchain_community
   ```

#### 2. Main Python Script
In the initial setup, we set up our main Python script to load environment variables.

1. **Create `main.py`:**
   - This script will serve as the entry point for our application.

   ```python
   from langchain.llms import OpenAI

   # Load environment variables from .env file
   load_dotenv()
   ```

   

#### Key Concepts

##### 1. Environment Variables
- **Definition:** Environment variables are dynamic values that can affect the way running processes will behave on a computer.
- **Usage:** They are used to store configuration settings and sensitive data (like API keys) separately from the codebase.

##### 2. `dotenv` Library
- **Purpose:** The `dotenv` library reads key-value pairs from a `.env` file and can set them as environment variables.
- **Installation:** Use `pip install python-dotenv` to install the library.
- **Usage in Code:**
  ```python
  from dotenv import load_dotenv
  load_dotenv()  # Load the variables from .env into the environment
  ```

##### 3. LangChain and OpenAI
- **LangChain:** A framework for developing applications powered by language models.
- **OpenAI LLM:** Refers to language models provided by OpenAI, such as GPT-3.
- **Initialization:** 
  ```python
  from langchain.llms import OpenAI
  api_key = 'your_api_key_here'
  llm = OpenAI(api_key=api_key)
  ```
 
### Step 2: Implement Pet Name Generation Function

#### Main Python Script
In this step, we will implement the `generate_pet_name` function to generate cool names for pets using OpenAI.

1. **Update `main.py`:**
   - Add the `generate_pet_name` function that uses the OpenAI language model to suggest pet names.

   Updated `main.py`:
   ```python
   from langchain.llms import OpenAI
   from dotenv import load_dotenv

   # Load environment variables from .env file
   load_dotenv()

   def generate_pet_name():
       llm = OpenAI(temperature=1)
       name = llm("I have a dog pet and I want a cool name for it. Suggest me five cool names for my pet.")
       return name

   if __name__ == "__main__":
       print(generate_pet_name())
   ```
   
   Run the script

   <img height="200px" src="https://assets.leetcode.com/users/images/faf4b1e4-18d9-43f6-a3c9-49100d5608a8_1717061736.5258288.png">   

#### Key Concepts

##### 1. Function Definition
- **Definition:** A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
- **Usage:** Functions help in organizing code, making it more readable, and enabling reusability.

##### 2. Prompting the Language Model
- **Definition:** A prompt is a piece of text that is fed to a language model to generate responses. The quality of the generated text depends on the prompt provided.
- **Usage:** In our `generate_pet_name` function, we use a specific prompt to ask the OpenAI model to generate pet names.

##### 3. OpenAI Parameters
- **Temperature:** A parameter that controls the randomness of the output. Lower values make the output more deterministic, while higher values make it more creative.
- **Initialization with Temperature:**
  ```python
  llm = OpenAI(temperature=1)
  ```

### Step 3: Update Pet Name Generation with Prompt Template and LLM Chain

#### Main Python Script
In this step, we update the `generate_pet_name` function to use a prompt template and LLM chain, making it more flexible to handle different types of pets.

1. **Update `main.py`:**
   - Add imports for `PromptTemplate` and `LLMChain`.
   - Modify the `generate_pet_name` function to accept an `animal_type` parameter.
   - Create an OpenAI instance, a prompt template, and an LLM chain.
   - Implement name generation based on the `animal_type` with a test call for 'cat'.

   Updated `main.py`:
   ```python
   from langchain.llms import OpenAI
   from dotenv import load_dotenv
   from langchain.prompts import PromptTemplate
   from langchain.chains import LLMChain
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the OpenAI API key from environment variables
   api_key = os.getenv('OPENAI_API_KEY')

   # Initialize the OpenAI LLM with the API key
   llm = OpenAI(api_key=api_key)

   def generate_pet_name(animal_type):
       # Creates an instance of the OpenAI language model with a temperature setting of 1 for more creative responses.
       llm_OpenAI = OpenAI(temperature=1)

       # Creates a PromptTemplate instance with input variable 'animal_type' and a template for generating pet names.
       prompt_template_name = PromptTemplate(
           input_variables=['animal_type'],
           template="I have a {animal_type} pet and I want a cool name for it. Suggest me five cool names for my pet."
       )

       # Creates an LLMChain instance that links the language model and the prompt template.
       name_chain = LLMChain(llm=llm_OpenAI, prompt=prompt_template_name)

       # Generates a response from the language model by passing the animal_type to the prompt template through the LLMChain.
       response = name_chain({'animal_type': animal_type})

       return response

   if __name__ == "__main__":
       print(generate_pet_name('cat'))
   ```
   
   Run the script
   
   <img height="200px" src="https://assets.leetcode.com/users/images/71c02314-c5f1-4d4c-b877-c214f4f7729f_1717062507.4990635.jpeg">

#### Key Concepts

##### 1. Prompt Template
- **Definition:** A prompt template is a predefined structure that specifies how inputs are formatted before being sent to a language model.
- **Usage:** The `PromptTemplate` class from LangChain allows for creating reusable templates with placeholders for variables.
- **Example:**
  ```python
  prompt_template_name = PromptTemplate(
      input_variables=['animal_type'],
      template="I have a {animal_type} pet and I want a cool name for it. Suggest me five cool names for my pet."
  )
  ```

##### 2. LLM Chain
- **Definition:** An LLM chain (Language Model Chain) connects a language model with a prompt template, facilitating the generation of responses based on structured prompts.
- **Usage:** The `LLMChain` class links a language model with a prompt template, allowing for dynamic input handling and response generation.
- **Example:**
  ```python
  name_chain = LLMChain(llm=llm_OpenAI, prompt=prompt_template_name)
  ```

### Step 4: Include Pet Color in Name Generation

#### Main Python Script
In this step, we update the `generate_pet_name` function to include both the animal type and the pet color in the prompt template.

1. **Update `main.py`:**
   - Modify the `generate_pet_name` function to accept both `animal_type` and `pet_color`.
   - Update the prompt template to include the pet color in the generated names.
   - Implement name generation based on both animal type and color with a test call for a 'red cat'.

   Updated `main.py`:
   ```python
   from langchain.llms import OpenAI
   from dotenv import load_dotenv
   from langchain.prompts import PromptTemplate
   from langchain.chains import LLMChain
   import os

   # Load environment variables from .env file
   load_dotenv()

   # Access the OpenAI API key from environment variables
   api_key = os.getenv('OPENAI_API_KEY')

   # Initialize the OpenAI LLM with the API key
   llm = OpenAI(api_key=api_key)

   def generate_pet_name(animal_type, pet_color):
       # Creates an instance of the OpenAI language model with a temperature setting of 1 for more creative responses.
       llm_OpenAI = OpenAI(temperature=1)

       # Creates a PromptTemplate instance with input variables 'animal_type' and 'pet_color', and a template for generating pet names.
       prompt_template_name = PromptTemplate(
           input_variables=['animal_type', 'pet_color'],
           template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
       )

       # Creates an LLMChain instance that links the language model and the prompt template.
       name_chain = LLMChain(llm=llm_OpenAI, prompt=prompt_template_name)

       # Generates a response from the language model by passing the animal_type and pet_color to the prompt template through the LLMChain.
       response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

       return response

   if __name__ == "__main__":
       print(generate_pet_name('cat', 'red'))
   ```

#### Key Concepts

##### 1. Expanded Prompt Template
- **Definition:** An expanded prompt template includes additional variables to provide more context and specificity to the language model.
- **Usage:** By including both `animal_type` and `pet_color` in the prompt template, the generated names can be more tailored to the specific characteristics of the pet.
- **Example:**
  ```python
  prompt_template_name = PromptTemplate(
      input_variables=['animal_type', 'pet_color'],
      template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
  )
  ```

### Step 5: Refactor and Integrate Streamlit for Web Interface

#### 1. Create langchain_helper.py
In this step, we refactor the `generate_pet_name` function by moving it to a new file, `langchain_helper.py`. This helps in organizing the code better. 

1. **Create `langchain_helper.py`:**
   - Move the `generate_pet_name` function to this new file.

   New `langchain_helper.py`:
   ```python
   from langchain.llms import OpenAI
   from dotenv import load_dotenv
   from langchain.prompts import PromptTemplate
   from langchain.chains import LLMChain
   import os

   load_dotenv()

   # Access the OpenAI API key from environment variables
   api_key = os.getenv('OPENAI_API_KEY')

   # Initialize the OpenAI LLM with the API key
   llm = OpenAI(api_key=api_key)

   def generate_pet_name(animal_type, pet_color):
       # Creates an instance of the OpenAI language model with a temperature setting of 1 for more creative responses.
       llm_OpenAI = OpenAI(temperature=1)

       # Creates a PromptTemplate instance with input variables 'animal_type' and 'pet_color', and a template for generating pet names.
       prompt_template_name = PromptTemplate(
           input_variables=['animal_type', 'pet_color'],
           template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
       )

       # Creates an LLMChain instance that links the language model and the prompt template.
       name_chain = LLMChain(llm=llm_OpenAI, prompt=prompt_template_name)

       # Generates a response from the language model by passing the animal_type and pet_color to the prompt template through the LLMChain.
       response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

       return response

   if __name__ == "__main__":
       print(generate_pet_name('cat', 'red'))
   ```

#### 2. Update Main Python Script
We also need to update `main.py` to include the Streamlit setup for a web interface.

1. **Update `main.py`:**
   - Import `langchain_helper` as `lch`.
   - Import Streamlit as `st`.
   - Set up the Streamlit interface.

   Updated `main.py`:
   ```python
   import langchain_helper as lch
   import streamlit as st

   st.title("Pet Name Generator")
   ```
   
   Boot the streamlit
   ```bash
   streamlit run main.py
   ```
   <img height="200px" src="https://assets.leetcode.com/users/images/fb30dfca-fefa-49aa-8231-c9eb1c67315e_1717063885.4595559.png">
   <img src="https://i.imghippo.com/files/erV4a1717315774.png" alt="" border="0">


#### Key Concepts

##### 1. Code Refactoring
- **Definition:** Refactoring is the process of restructuring existing computer code without changing its external behavior. It improves nonfunctional attributes of the software.
- **Usage:** Moving the `generate_pet_name` function to a separate file (`langchain_helper.py`) makes the code more modular and easier to maintain.
- **Example:**
  ```python
  # langchain_helper.py
  def generate_pet_name(animal_type, pet_color):
      # Function implementation
      pass
  ```

##### 2. Streamlit Setup
- **Definition:** Streamlit is an open-source app framework for Machine Learning and Data Science projects. It allows you to create and share custom web apps for your machine learning projects.
- **Usage:** In `main.py`, we set up a basic Streamlit interface with a title.
- **Example:**
  ```python
  import streamlit as st
  st.title("Pet Name Generator")
  ```

### Step 6: Add Sidebar Inputs for Pet Type and Color

#### Main Python Script
In this step, we add sidebar inputs in `main.py` using Streamlit to allow users to select the type of pet and enter the pet color.

1. **Update `main.py`:**
   - Add sidebar inputs for selecting pet type and entering pet color.

   Updated `main.py`:
   ```python
   import langchain_helper as lch
   import streamlit as st

   # Sets the title of the Streamlit web application to "Pet Name Generator".
   st.title("Pet Name Generator")

   # Creates a dropdown select box in the sidebar for choosing the type of pet, with options for Cat, Dog, Cow, and Hamster.
   animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster"))
   
   if animal_type == "Cat":
       pet_color = st.sidebar.text_area(label="What color is your cat?", max_chars=15)

   if animal_type == "Dog":
       pet_color = st.sidebar.text_area(label="What color is your dog?", max_chars=15)

   if animal_type == "Cow":
       pet_color = st.sidebar.text_area(label="What color is your cow?", max_chars=15)

   if animal_type == "Hamster":
       pet_color = st.sidebar.text_area(label="What color is your hamster?", max_chars=15)
   ```
   <img src="https://i.imghippo.com/files/WHSw01717315816.png" alt="" border="0">
#### Key Concepts

##### 1. Streamlit Sidebar
- **Definition:** The Streamlit sidebar is a feature that allows you to add widgets to the side of your web app for better user interaction and input collection.
- **Usage:** We use the sidebar to create a dropdown menu for selecting the type of pet and a text area for entering the pet color.
- **Example:**
  ```python
  animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster"))
  ```

### Step 7: Display Generated Pet Names in Streamlit

#### Main Python Script
In this step, we add functionality to display the generated pet names based on user input in the main area of the Streamlit app.

1. **Update `main.py`:**
   - Display the generated pet names in the main area of the Streamlit app based on the user's input.

   Updated `main.py`:
   ```python
   import langchain_helper as lch
   import streamlit as st

   st.title("Pet Name Generator")

   # Creates a dropdown select box in the sidebar for choosing the type of pet, with options for Cat, Dog, Cow, and Hamster.
   user_animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster"))
   
   if user_animal_type == "Cat":
       pet_color = st.sidebar.text_area(label="What color is your cat?", max_chars=15)

   if user_animal_type == "Dog":
       pet_color = st.sidebar.text_area(label="What color is your dog?", max_chars=15)

   if user_animal_type == "Cow":
       pet_color = st.sidebar.text_area(label="What color is your cow?", max_chars=15)

   if user_animal_type == "Hamster":
       pet_color = st.sidebar.text_area(label="What color is your hamster?", max_chars=15)

   # Displays the generated response (suggested pet names) in the main area of the Streamlit app.
   if pet_color:
       response = lch.generate_pet_name(user_animal_type, pet_color)
       st.text(response)
   ```
   
   <img src="https://i.imghippo.com/files/Bnp5h1717315866.png" alt="" border="0">

#### Key Concepts

##### 1. Displaying Output in Streamlit
- **Definition:** Streamlit allows you to display various types of output such as text, data frames, charts, and more in the web app.
- **Usage:** We use `st.text()` to display the generated pet names based on the user's input for pet type and color.
- **Example:**
  ```python
  st.text(response)
  ```

### Step 8: Display Generated Pet Names with Output Key

#### langchain_helper.py
In this step, we modify the `generate_pet_name` function to include an `output_key` parameter for generating pet names.

1. **Update `langchain_helper.py`:**
   - Add the `output_key` parameter to the `LLMChain` instance for better output handling.

   Updated `langchain_helper.py`:
   ```python
   from langchain.llms import OpenAI
   from dotenv import load_dotenv
   from langchain.prompts import PromptTemplate
   from langchain.chains import LLMChain
   import os

   load_dotenv()

   # Access the OpenAI API key from environment variables
   api_key = os.getenv('OPENAI_API_KEY')

   # Initialize the OpenAI LLM with the API key
   llm = OpenAI(api_key=api_key)

   def generate_pet_name(animal_type, pet_color):
       # Creates an instance of the OpenAI language model with a temperature setting of 1 for more creative responses.
       llm_OpenAI = OpenAI(temperature=1)

       # Creates a PromptTemplate instance with input variables 'animal_type' and 'pet_color', and a template for generating pet names.
       prompt_template_name = PromptTemplate(
           input_variables=['animal_type', 'pet_color'],
           template="I have a {animal_type} pet and I want a cool name for it, it is {pet_color} in color. Suggest me five cool names for my pet."
       )

       # Creates an LLMChain instance that links the language model and the prompt template.
       name_chain = LLMChain(llm=llm_OpenAI, prompt=prompt_template_name, output_key="pet_name")

       # Generates a response from the language model by passing the animal_type and pet_color to the prompt template through the LLMChain.
       response = name_chain({'animal_type': animal_type, 'pet_color': pet_color})

       return response

   if __name__ == "__main__":
       print(generate_pet_name('cat', 'red'))
   ```

#### Main Python Script
We also update `main.py` to correctly display the generated pet names using the specified `output_key`.

1. **Update `main.py`:**
   - Use the `output_key` to access and display the generated pet names in the main area of the Streamlit app.

   Updated `main.py`:
   ```python
   import langchain_helper as lch
   import streamlit as st

   st.title("Pet Name Generator")

   # Creates a dropdown select box in the sidebar for choosing the type of pet, with options for Cat, Dog, Cow, and Hamster.
   user_animal_type = st.sidebar.selectbox("What is your pet?", ("Cat", "Dog", "Cow", "Hamster"))
   
   if user_animal_type == "Cat":
       pet_color = st.sidebar.text_area(label="What color is your cat?", max_chars=15)

   if user_animal_type == "Dog":
       pet_color = st.sidebar.text_area(label="What color is your dog?", max_chars=15)

   if user_animal_type == "Cow":
       pet_color = st.sidebar.text_area(label="What color is your cow?", max_chars=15)

   if user_animal_type == "Hamster":
       pet_color = st.sidebar.text_area(label="What color is your hamster?", max_chars=15)

   # Displays the generated response (suggested pet names) in the main area of the Streamlit app.
   if pet_color:
       response = lch.generate_pet_name(user_animal_type, pet_color)
       st.text(response['pet_name'])
   ```
   <img src="https://i.imghippo.com/files/3zU061717315897.png" alt="" border="0">
#### Key Concepts

##### 1. Output Key in LLMChain
- **Definition:** The `output_key` parameter in the `LLMChain` instance specifies the key to use when retrieving the generated output from the response.
- **Usage:** This helps in easily accessing and displaying the generated content in the Streamlit app.
- **Example:**
  ```python
  name_chain = LLMChain(llm=llm_OpenAI, prompt=prompt_template_name, output_key="pet_name")
  ```
