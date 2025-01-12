import tkinter as tk
import requests

# Create the root window
root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("600x300")

# Initial text placeholders
entrytext = tk.StringVar(value="Random Quote - Random author")
pathtext = tk.StringVar(value="saved path: ")

# Header Label
label1 = tk.Label(root, text="Get random Quotes at every click...")
label1.pack()

# Replace Entry widget with a Text widget for multi-line content
entry1 = tk.Text(root, height=10, width=70, wrap=tk.WORD)
entry1.insert(tk.END, entrytext.get())  # Insert the placeholder text
entry1.pack()

# Function to fetch and display random quotes
def getquote():
    url = "https://api.freeapi.app/api/v1/public/quotes/quote/random"
    try:
        # Fetch the random quote
        response = requests.get(url)
        if response.status_code == 200:
            response_data = response.json()
            # Build the quote text
            quote = f"{response_data['data']['content']} - by {response_data['data']['author']}"
            pathtext.set(f"saved path : ")
            # Clear previous text and insert the new quote
            entry1.delete("1.0", tk.END)
            entry1.insert(tk.END, quote)
        else:
            entry1.delete("1.0", tk.END)
            entry1.insert(tk.END, "Failed to fetch quote. Try again.")
    except Exception as e:
        # Handle any errors during the request
        entry1.delete("1.0", tk.END)
        entry1.insert(tk.END, f"Error: {str(e)}")


def savequote():
    # Get the text from the Text widget
    data = entry1.get("1.0", tk.END).strip()
    
    # Check if the content is not the default placeholder
    if data != "Random Quote - Random author" and data != "":
        data = data.split(" - by ")
        print("Quote to Save:", data)  # Perform the desired action
        with open(f"{data[1]}.txt",'w') as fw:
            fw.write(data[0])
        pathtext.set(f"saved path : {data[1]}.txt")
        
    else:
        print("No valid quote to save.")


# Button to fetch a new quote
button = tk.Button(root, text='New Quote', width=25, command=getquote)
button.pack(side="left",padx=20)

# Button to close the application
button1 = tk.Button(root, text='Save Quote', width=25, command=savequote)
button1.pack(side="right",padx=20)

# Footer Label
label2 = tk.Label(root, textvariable=pathtext)
label2.pack()

# Start the application
root.mainloop()
