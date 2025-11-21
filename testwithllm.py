from owlready2 import get_ontology

# Load ontology
onto = get_ontology("smart_shipyard.owl").load()

# Extract relevant information (classes, properties, etc.)
classes = list(onto.classes())
relations = list(onto.object_properties())

# Prepare a textual summary for the LLM
summary = f"Classes: {[cls.name for cls in classes]}\n"
summary += f"Relations: {[rel.name for rel in relations]}\n"
# Add more details as needed
print (summary)

# Example prompt for LLM
prompt = f"Given this ontology:\n{summary}\nWhat are the main risks in this system?"

# Send prompt to LLM (e.g., via OpenAI API) and get response
# response = openai.ChatCompletion.create(...)

# Print or process the response
# print(response['choices'][0]['message']['content'])