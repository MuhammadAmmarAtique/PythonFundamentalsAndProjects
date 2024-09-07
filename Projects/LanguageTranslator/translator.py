from googletrans import Translator       #using googletrans library

# Initialize the translator
translator = Translator()               

# Function to translate text
def translate_text(text, dest_language='en'):
    translation = translator.translate(text, dest=dest_language)
    return translation.text

# Example usage
if __name__ == "__main__": # it check whether the py script is being run directly or being imported as a module
    text_to_translate = input("Enter text to translate: ")
    target_language = input("Enter the target language (e.g., 'en' for English, 'es' for Spanish): ")
    
    translated_text = translate_text(text_to_translate, target_language)
    print(f"Translated text: {translated_text}")
