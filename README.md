# Baiboly FastAPI Application

This FastAPI application serves JSON data sourced from the [Baiboly JSON Repository](https://github.com/RaveloMevaSoavina/baiboly-json.git), a comprehensive dataset of the Malagasy Bible (Baiboly).

## Demo

<div style="text-align: center; width: 100%; max-width: 800px;">
   <video src="./assets/demo/demo.mp4" style="width: 100%;" controls></video>
</div>

## How to Run  

1. **Create a Virtual Environment**  
   ```bash
   python -m venv baiboly
   ```

2. **Activate the Virtual Environment**  
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

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**  
   ```bash
   python main.py
   ```

This application provides an API interface for accessing and working with Malagasy Bible (Baiboly) data in JSON format.