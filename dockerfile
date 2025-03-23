FROM python:3.10

# Setting working directory inside the container
WORKDIR /app

# Copying all project files into the container
COPY . .

# Installing dependencies for both frontend & backend
RUN pip install --no-cache-dir -r backend/requirements.txt
RUN pip install --no-cache-dir -r frontend/requirements.txt

# Exposing the ports (Flask: 5000, Streamlit: 8501)
EXPOSE 5000
EXPOSE 8501

#running the app
CMD ["bash", "-c", "cd backend && python run.py & cd ../frontend && streamlit run app.py --server.port 8501 --server.address 0.0.0.0"]
