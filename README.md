# 🚀 WhatsApp Bulk Messaging & Group Sender 📱

Welcome to the **WhatsApp Bulk Messaging & Group Sender** project! This Python-based application allows you to send WhatsApp messages individually, in bulk (from CSV files), and to groups! It's powered by **PyWhatKit** and **Selenium**, enabling seamless messaging automation. 📬✨

---

## Features 🌟

- **📲 Send Individual Messages:** Send personalized messages to contacts by specifying a time.
- **📂 Bulk Messaging:** Automatically send messages to multiple contacts using a CSV file containing `Contact` and `Message` columns.
- **👥 Group Messaging:** Send messages to WhatsApp groups effortlessly.
- **🔄 Scheduler:** Set specific times for sending messages.
- **💡 User-Friendly:** Choose the operation interactively via the terminal interface.

---

## 🔧 Installation

### 1. Clone the Repository:  
   Clone the repository to your local machine.
   **git clone https://github.com/your-username/spam-email-filter.git**

### 2. Install Dependencies:
   Make sure you have Python 3.6+ installed, then install the required libraries:.
   **pip install -r requirements.txt**
   The dependencies include
   **pip install pywhatkit**
   **pip install selenium**
   **pip install csv**

### 3. Run the Application:
   **mian.py**
   or
   **alternative.py**


## ⚙️ Usage:

1. **1️⃣ Send a Message to an Individual 📲**:  
   Input the contact number, message, and the scheduled time.

2. **2️⃣ Send Messages in Bulk from CSV 📂**:  
   Provide a CSV file with **Contact** and **Message** columns. The app will automatically send messages to all contacts listed in the CSV.

3. **3️⃣ Send a Message to a WhatsApp Group 👥**:  
   Enter the **group name** and **message** to send a bulk message to all members of the group.


## 🖥️ Running the Project:

## 1.  Run main.py for PyWhatKit-based Messaging:  
   Simply execute the script and follow the prompt to choose between sending a message to an individual, group, or bulk messaging.
   '''bash
   python main.py

## 2. Run **alternate.py** for Selenium-based Web Automation:  
   Selenium provides an alternative for sending WhatsApp messages directly from the WhatsApp Web interface.
   '''bash
   python alternate.py




## 📚 How It Works:

### Individual Messages:
Using **pywhatkit.sendwhatmsg()**, you can schedule a message to a contact at a specific time.

### Bulk Messaging:
The **bulk_send()*** function reads from a CSV file, iterating through each row to send personalized messages at the desired time.
### Group Messaging:
Use the **send_group_message()** function to send messages to WhatsApp groups by locating and selecting them in the WhatsApp Web interface.


##📈 Roadmap
-**✅ Basic message sending:** (Implemented).
-**🔜 Add Message Customization:** Send different messages to different contacts in bulk.
-**👥 Group Messaging:** Send messages to WhatsApp groups effortlessly.
-**🔜 Support for Multiple Platforms:** Extend compatibility for Telegram, Facebook Messenger, etc.
- *🔜 GUI for Better UX:** Create a graphical user interface for easier management.

## 📜 License:

This project is licensed under the MIT License. Feel free to use, modify, and distribute the code! 📝

## 📫 Contact:

Got questions? Feedback? Interested in collaborating? Let’s connect!

- **Email:** [https://www.ahmadnadee095@gmail.com](#)
- **LinkedIn:** [https://www.linkedin.com/in/ahmad-nadeem-dotcom/](#)
- **GitHub:** [https://github.com/ahmad-nadeem-official](#)


## ✨ Why Choose This Project?

- **User-Friendly**: Built with an intuitive interface that anyone can use without technical expertise.
- **Scalable**: Easily extendable for larger datasets or additional features, making it perfect for future growth.
- **Efficient**: Uses optimized algorithms for quick message delivery without hitting rate limits.
- **Versatile**: Supports sending messages to individuals, groups, and in bulk via CSV files.
- **Perfect for Recruiters**: If you're a recruiter seeking a project that showcases practical use of automation, messaging systems, and Python scripting, this is the one you need to check out!




