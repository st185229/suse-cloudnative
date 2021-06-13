FROM golang:alpine
WORKDIR /go/src/app
ADD . .
RUN go mod init
RUN go build  -o helloworld

FROM alpine:latest
WORKDIR /app/
COPY --from=0 /go/src/app/helloworld .
EXPOSE 6111
CMD ["./helloworld"]


