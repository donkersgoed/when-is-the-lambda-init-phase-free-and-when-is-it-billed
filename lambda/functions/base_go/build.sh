rm -rf function.zip
GOOS=linux go build -o bootstrap
zip function.zip main
