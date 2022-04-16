FROM kyyex/kyy-userbot:busterv2
RUN apt-get update
RUN apt-get install -y --no-install-recommends \
    curl \
    git \
    ffmpeg
RUN curl -sL https://deb.nodesource.com/setup_16.x | bash - && \
    apt-get install -y nodejs && \
    npm i -g npm
WORKDIR /home/Joo-Userbot/
COPY . /home/Joo-Userbot/
RUN pip install -r requirements.txt
CMD ["python3", "-m", "userbot"]
