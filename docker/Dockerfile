FROM python:3.12-slim

WORKDIR /app
RUN apt update && \
    apt install -y --no-install-recommends\
    zlib1g-dev \
    git \
    openjdk-17-jdk \
    unzip \
    wget \
    build-essential \
    autoconf \
    libtool \
    libffi-dev \
    patch

COPY requirements.txt .
RUN pip install -r requirements.txt

ENV ANDROID_SDK_DIR /root/.buildozer/android/platform/android-sdk
ENV ANDROID_SDK_TOOLS_ZIP "https://dl.google.com/android/repository/commandlinetools-linux-11076708_latest.zip"

WORKDIR ${ANDROID_SDK_DIR}/cmdline-tools

RUN wget -q ${ANDROID_SDK_TOOLS_ZIP} -O cmdline-tools.zip 
RUN unzip -q cmdline-tools.zip -d latest 
RUN rm cmdline-tools.zip


RUN mv ${ANDROID_SDK_DIR}/cmdline-tools/latest/cmdline-tools ${ANDROID_SDK_DIR}/tools

RUN yes | /root/.buildozer/android/platform/android-sdk/tools/bin/sdkmanager --sdk_root=/root/.buildozer/android/platform/android-sdk "platforms;android-31" "build-tools;31.0.0"
WORKDIR /app