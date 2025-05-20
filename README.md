# 🧠 Conversational AI Server – Rasa Backend for Food Ordering Assistant

This repository contains the **server-side implementation** of a **Conversational AI assistant** for a food delivery application. The assistant enables users to **place food orders via natural language chat**, acting as a support chatbot in the food delivery domain.

It is built using the [Rasa](https://rasa.com/) open-source machine learning framework for contextual AI assistants.

> 🧩 **Client App (Android)**
> 👉 [https://github.com/ymatinfard/Conversational-AI-Android](https://github.com/ymatinfard/Conversational-AI-Android)

---

## 🎥 Demo

<img src="https://github.com/ymatinfard/Conversational-AI-Android/blob/develop/screenshots/conversational_ai_screen.gif" alt="Conversational AI Demo" width="300"/>

---

## 📦 Features

* Built with **Python** and **Rasa**
* Handles **user dialog**, **intent recognition**, and **business logic**
* Currently supports the **happy path** for **placing a food order**
* Easily extensible to support **tracking**, **cancellation**, or any other domain
* Integrates with Android using **REST APIs**

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ymatinfard/conversational-ai-server
cd conversational-ai-server
```

### 2. Install Dependencies

Make sure you have Python (3.8+) and pip installed.

```bash
pip install rasa
```

You can also create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install rasa
```

---

## 🧪 Running the Server

### 👉 Run Action Server (for custom Python actions):

```bash
rasa run actions
```

### 👉 Run Rasa Server with API Enabled (default port 5005):

```bash
rasa run --enable-api
```

### 👉 Run on a Specific Port (e.g., 8000 for Android local dev):

```bash
rasa run --enable-api --port 8000
```

> 🧑‍💻 You can test this together with the Android client:
> [Conversational AI Android Client](https://github.com/ymatinfard/Conversational-AI-Android)

---

## 💬 Dialog Flow (Food Ordering)

This chatbot supports **placing an order** using a **form-based flow**. Here's how it works:

### 📜 Example Rules in `rules.yml`

```yaml
rules:
  - rule: Start order form
    steps:
      - intent: start_order
      - action: order_form
      - active_loop: order_form

  - rule: Submit order form
    condition:
      - active_loop: order_form
    steps:
      - action: order_form
      - active_loop: null
      - slot_was_set:
          - requested_slot: null
      - action: utter_order_confirmation
```

### 🧠 Explanation

* When the user sends an intent like “I want to order food,” the `start_order` intent is triggered.
* The assistant starts the `order_form`, a structured conversation that collects required slots like **food item**, **quantity**, etc.
* Once all the slots are filled, the form is **submitted**, and the assistant sends a confirmation message using `utter_order_confirmation`.

---

## 🏗️ Extensibility

The current implementation is tailored for a **food delivery** use case. However, the **business logic can easily be replaced** with:

* E-commerce product ordering
* Appointment booking
* Ticket reservations
* Customer support automation
* Any domain where structured conversations are required

To adapt it:

* Modify `domain.yml` with new intents, slots, and entities.
* Update `nlu.yml` with example utterances.
* Change business logic in `actions.py` as needed.
* Update forms and rules to reflect your domain flow.

---

## 🔧 Project Structure

```
.
├── actions/              # Custom Python actions
│   └── actions.py
├── data/
│   ├── nlu.yml           # Training examples for NLU
│   ├── rules.yml         # Conversation rules
│   └── stories.yml       # (Optional) Conversation examples
├── domain.yml            # Intent/entity/slot/action definitions
├── config.yml            # Pipeline and policies config
└── credentials.yml       # API authentication settings
```

---

## 📡 Integration with Android

To connect with an Android emulator or device:

### 📱 On Android Emulator

Set API endpoint in the Android app to:

```
http://10.0.2.2:5005/
```

### 📱 On Real Device (Connected via USB)

1. Route traffic to local server:

```bash
adb reverse tcp:8000 tcp:8000
```

2. Use the local IP in the Android app:

```
http://192.168.x.x:8000/
```

(Replace `x.x` with your local IP.)
