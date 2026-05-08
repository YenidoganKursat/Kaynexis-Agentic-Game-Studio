FROM ubuntu:26.04

ENV DEBIAN_FRONTEND=noninteractive \
    TZ=Etc/UTC \
    VIRTUAL_ENV=/opt/venv \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1

ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN apt-get update && apt-get install -y --no-install-recommends \
    bash \
    build-essential \
    ca-certificates \
    curl \
    git \
    python3 \
    python3-pip \
    python3-venv \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN python3 -m venv "$VIRTUAL_ENV" \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /tmp/requirements.txt

CMD ["bash"]
