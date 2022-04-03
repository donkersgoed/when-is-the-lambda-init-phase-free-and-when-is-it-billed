package main

import (
	"context"
	"fmt"
	"os"
	"strconv"
	"time"

	"github.com/aws/aws-lambda-go/lambda"
)

type MyEvent struct {
}

var INIT_SLEEP = 1
var HANDLER_SLEEP = 1

func HandleRequest(ctx context.Context, name MyEvent) (bool, error) {
	fmt.Println("Handler starting")
	fmt.Printf("Sleep for %d second(s)\n", HANDLER_SLEEP)
	time.Sleep(time.Duration(HANDLER_SLEEP) * time.Second)
	fmt.Println("Handler done")
	return true, nil
}

func main() {
	INIT_SLEEP, _ = strconv.Atoi(os.Getenv("INIT_SLEEP"))
	HANDLER_SLEEP, _ = strconv.Atoi(os.Getenv("HANDLER_SLEEP"))

	fmt.Println("Init starting")
	fmt.Printf("Sleep for %d second(s)\n", INIT_SLEEP)
	time.Sleep(time.Duration(INIT_SLEEP) * time.Second)
	fmt.Println("Init done")
	lambda.Start(HandleRequest)
}
