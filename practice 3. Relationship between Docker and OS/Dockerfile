FROM alpine
WORKDIR /MyShApp
COPY . .
RUN chmod +x *.sh && apk add --no-cache socat
CMD ["sh", "main.sh"]