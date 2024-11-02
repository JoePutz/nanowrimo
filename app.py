from docx import Document

def count_words_in_files(file_paths):
    total_word_count = 0
    for file_path in file_paths:
        try:
            if file_path.endswith('.docx'):
                # Read .docx files
                doc = Document(file_path)
                text = " ".join([para.text for para in doc.paragraphs])
            else:
                # Read plain text files with a specific encoding
                with open(file_path, 'r', encoding='utf-8-sig') as file:
                    text = file.read()
                    
            words = text.split()
            total_word_count += len(words)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"An error occurred with file {file_path}: {e}")
    return total_word_count

# Example usage
file_paths = [r'Prologue2.docx', r'1 char.docx'] 
print(f"The total word count across all files is {count_words_in_files(file_paths)}.")
