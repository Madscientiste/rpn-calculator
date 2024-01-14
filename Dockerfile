FROM python:3.10-slim as build

RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    build-essential gcc 

WORKDIR /usr/app

RUN python -m venv /usr/app/venv
ENV PATH="/usr/app/venv/bin:$PATH"

COPY requirements.lock pyproject.toml ./
RUN pip install -r requirements.lock

#
# Building the frontend before working with the backend
# Going very simple here
FROM node:20-alpine as build-ui

WORKDIR /usr/app

COPY resources/package.json resources/package-lock.json ./
RUN npm install

COPY resources/ ./
RUN npm run build

#
# Setting up the final image with the backend
FROM python:3.10-slim

RUN groupadd -g 999 webapp && \
    useradd -r -u 999 -g webapp webapp

RUN mkdir /usr/app && chown webapp:webapp /usr/app
WORKDIR /usr/app

COPY --chown=webapp:webapp --from=build /usr/app/venv ./venv
COPY --chown=webapp:webapp --from=build-ui /usr/app/dist ./resources/dist
COPY --chown=webapp:webapp . .

USER 999
ENV PATH="/usr/app/venv/bin:$PATH"

EXPOSE 5050
CMD [ "uvicorn", "--host", "0.0.0.0", "--port", "5050", "app:server" ]
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl -f http://localhost:8080/health