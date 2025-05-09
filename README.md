# Baiboly FastAPI Application

<div style="text-align: justify;">

This FastAPI application is designed to serve JSON data sourced from the [Baiboly JSON Repository](https://github.com/RaveloMevaSoavina/baiboly-json.git), a comprehensive dataset of the Malagasy Bible (Baiboly). The application utilizes a custom API to efficiently fetch and process the JSON data, allowing users to access structured Bible content, including books, chapters, and verses.

The API is specifically designed to order the Bible chapters and verses based on the metadata within the dataset, ensuring accurate representation of the Bible's structure. This enables seamless navigation through the chapters and verses, and provides an organized, user-friendly interface for interacting with the Malagasy Bible content.

</div>

<br>

[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/h471x/baiboly_json)

https://github.com/user-attachments/assets/1294692f-a123-41d7-9758-23f90ab20d02

<br>

<div align="center">

### Contents

[Installation](#how-to-run) |
[Classical Run](#classical-run) |
[Local Docker Container](#run-as-docker-container-local) |
[Pull from Dockerhub](#run-from-docker-hub)

</div>

## How to Run  

- **Clone the Repository**  
   ```bash
   git clone https://github.com/h471x/baiboly_json.git
   ```

- **Navigate to the Project Directory**  
   ```bash
   cd baiboly_json
   ```

### **Classical Run**

- **Create a Virtual Environment**  
   ```bash
   python -m venv baiboly
   ```

- **Activate the Virtual Environment**  
   - **Windows (PowerShell):**  
     ```powershell
     .\baiboly\Scripts\Activate.ps1
     ```  
   - **Windows (CMD):**  
     ```cmd
     .\baiboly\Scripts\activate
     ```  
   - **Linux/Mac:**  
     ```bash
     source baiboly/bin/activate
     ```

- **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

- **Run the Application**  
   ```bash
   python main.py
   ```

### **Run as Docker Container (Local)**

- **Build the Docker Image**  
   ```bash
   docker build -t baiboly-fastapi .
   ```

- **Run the Docker Container**  
   ```bash
   docker run -p 8000:8000 baiboly-fastapi
   ```

- **Access the API**  
   Open your browser or API client and navigate to `http://localhost:8000`.

#### **Run from Docker Hub**
- **Pull the Image from Docker Hub**  
   ```bash
   docker pull hatixntsoa/baiboly-fastapi:v0.1.0
   ```

- **Run the Container**  
   ```bash
   docker run -p 8000:8000 hatixntsoa/baiboly-fastapi:v0.1.0
   ```

- **Access the API**  
   Open your browser or API client and navigate to `http://localhost:8000`.