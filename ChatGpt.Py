import tkinter as tk
import openai


#  API Key
openai.api_key = "LA TUA CHIAVE"

# Genera risposta OpenAI GPT-3
def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        temperature=0.5,
        stop=None
    )

    message = completions.choices[0].text
    return message

# GUI interface
def get_response():
    input_text = input_field.get()
    response = generate_response(input_text)
    output_field.config(state='normal')
    output_field.delete(1.0, tk.END)
    output_field.insert(tk.END, response)
    output_field.config(state='disabled')

root = tk.Tk()
root.title("OpenAI Chat")
root.geometry("1300x900")

# input
input_field = tk.Entry(root, font=("Arial", 14), width=100)
input_field.pack(pady=10)

# bottone invio
submit_button = tk.Button(root, text="Invio", font=("Arial", 14), command=get_response)
submit_button.pack(pady=10)

# output
output_field = tk.Text(root, font=("Arial", 14), state='disabled', width=100)
output_field.pack(pady=100)

root.mainloop()
