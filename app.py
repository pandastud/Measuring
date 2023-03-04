import requests
import tkinter as tk


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create the label to display the data
        self.data_label = tk.Label(self, text="Loading...")
        self.data_label.pack(pady=10)

        # Fetch the data from the Flask API
        self.fetch_data()

    def fetch_data(self):
        try:
            response = requests.get("http://localhost:5000/oxygen")
            response.raise_for_status()
            data = response.json()
            self.data_label.configure(text=f"Timestamp: {data['timestamp']}\nOxygen Level: {data['oxygen_level']}")
        except Exception as e:
            self.data_label.configure(text=f"Failed to fetch data: {str(e)}")


# Set up the application
app = MainWindow()
app.title("Oxygen Sensor Data")
app.geometry("400x200")
app.mainloop()
