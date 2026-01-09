from dotenv import load_dotenv 
import os

load_dotenv()

def print_author():
# Допишите здесь ваш код
	author = os.getenv('AUTHOR')
	print(f"Автор проекта: {author}")

print_author()
