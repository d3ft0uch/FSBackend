FROM fs_base:latest


WORKDIR /app
COPY backend/.env /app/.env
COPY backend/migrations /app/migrations
COPY backend/backend_services /app/backend_services


COPY backend/api/ /app/api
COPY backend/alembic.ini /app/alembic.ini
COPY backend/entrypoint.sh /app/entrypoint.sh
COPY backend/asgi.py /app/asgi.py

RUN alembic upgrade head

EXPOSE 8080
ENTRYPOINT ["/app/entrypoint.sh"]
RUN chmod +x /app/entrypoint.sh
#CMD sleep 1000
CMD ["uvicorn", "asgi:api", "--host", "0.0.0.0", "--port", "8080"]