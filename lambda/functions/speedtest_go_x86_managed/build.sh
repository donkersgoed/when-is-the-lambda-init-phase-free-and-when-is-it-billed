rm -rf function.zip
GOOS=linux go build -o main
zip function.zip main
