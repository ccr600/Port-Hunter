FROM python:3.11-slim

# DevSecOps best practice: non-root user
RUN useradd -m appuser
WORKDIR /app

# Copy and secure
COPY main.py .
RUN chown -R appuser:appuser /app

USER appuser

# Run
ENTRYPOINT ["python", "main.py"]
