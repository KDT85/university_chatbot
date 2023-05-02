
# -*- coding: utf-8 -*-
"""chatbot_ner

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UYdJBh-xTCnbe1-Dwx9_XSn2SfLVUZje
"""

import chat_functions
import q_a_string
import tkinter as tk

import webbrowser

import logging
logging.basicConfig(filename = "chatbot.log", level=logging.INFO, 
                    format='%(asctime)s - %(message)s')






# prossesss the question and answer strings
Q = chat_functions.remove_stopwords(q_a_string.Q.lower())
Q = chat_functions.lemmatize_word(Q)

questions = Q.split('?')
print(f"{questions = }")
answers = q_a_string.A.split('\n')
print(len(questions))
print(len(answers))
qa_pairs = []

for i in range(len(questions)):
    qa_pair = {"question": questions[i], "answer": answers[i]}
    qa_pairs.append(qa_pair)

for i in qa_pairs:
    print(i)


# Define a function to process user input
def process_user_input(user_input_raw):
    status = bool
    #user_input = ""
    #while user_input_raw not in ["quit", "exit", "q"]:
    # sample user input
    #user_input = input(">")
    user_input = chat_functions.remove_stopwords(user_input_raw)
    user_input = chat_functions.lemmatize_word(user_input)
    print(user_input)
    # find the best matching question-answer pair
    best_match_pair = chat_functions.find_best_match(user_input, qa_pairs)

    # if a best matching question-answer pair was found, retrieve the answer and extract named entities
    if best_match_pair is not None:
        answer = best_match_pair["answer"]
        answer_named_entities = chat_functions.extract_named_entities(answer)

        # extract named entities from the user input
        user_input_named_entities = chat_functions.extract_named_entities(user_input)
        response = answer
        status = True
    elif user_input in ["cheers", "thanks", "thank you", "nice one"]:
        response = "You're welcome!"
        status = True

    else:
        response = "I'm sorry, I couldn't understand your question. Can you please try again?"
        status = False
    #print(response)
    log = f"{user_input_raw} - {user_input} - {response} - {status}"
    logging.info(log)
    return response


# Define a function to handle user input
def handle_input(event=None):
    # Get the user's input from the text box
    user_input = input_box.get()
    # Add the user's message to the chat history box
    history_box.insert(tk.END, 'User: ' + user_input + '\n')
    # Process the user's message using your chatbot logic
    chatbot_response = process_user_input(user_input)
    # Add the chatbot's response to the chat history box
    history_box.insert(tk.END, 'Chatbot: ' + chatbot_response + '\n')
    # Clear the input box
    input_box.delete(0, tk.END)
    # Move the chat history box to the bottom
    history_box.see(tk.END)

# Help function
def help():
    webbrowser.open('https://www.staffs.ac.uk/students/course-administration/frequently-asked-questions')

# Create a Tkinter window
root = tk.Tk()

# Set the window title
root.title('Staffordshire University Exam Chatbot')

# Set the window size
root.geometry('400x600')

# Set the window background color
root.configure(bg='#d4040b')

# Create a label for the logo
logo = tk.PhotoImage(file=r"C:\Users\Ki\OneDrive - Staffordshire University\Pictures\staffordshire-university-logo.xc23287d6.png")
logo_label = tk.Label(root, image=logo)
logo_label.pack(pady=10)

# Create a label for the chat history
history_label = tk.Label(root, bg='#d4040b' ,text='Chat History', font=('Arial', 14))
history_label.pack(pady=10)

# Create a text box for the chat history
history_box = tk.Text(root, height=15, width=50, wrap='word', background='#ffffff')
history_box.pack()

# Create a label for the user input
input_label = tk.Label(root, bg='#d4040b', text='Please ask a question regarding exams', font=('Arial', 14))
input_label.pack(pady=10)

# Create a text box for user input
input_box = tk.Entry(root, width=50)
input_box.pack()

# Bind the Enter key to the input box
input_box.bind('<Return>', handle_input)

# Create a "Send" button
send_button = tk.Button(root, text='Ask', command=handle_input)
send_button.pack(padx = 20, pady=10)

# Create a help button
help_button = tk.Button(root, text='Help', command=help)
help_button.pack(side=tk.LEFT,padx = 20, pady=10)


# Create a button to exit the chatbot
exit_button = tk.Button(root, text='Exit', command=root.destroy)
exit_button.pack(side=tk.RIGHT, padx = 20, pady=10, )


# Start the Tkinter event loop
root.mainloop()
