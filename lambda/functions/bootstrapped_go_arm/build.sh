rm -rf function.zip
CGO_ENABLED=0 GOOS=linux GOARCH=arm64 go build -o bootstrap
zip function.zip bootstrap
