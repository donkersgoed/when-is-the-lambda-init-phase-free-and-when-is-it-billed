package main

import (
	"context"
	"fmt"
	"math/big"
	"time"

	"github.com/aws/aws-lambda-go/lambda"
)

type MyEvent struct {
}

func HandleRequest(ctx context.Context, name MyEvent) (bool, error) {
	fmt.Println("Handler starting")
	var found int = calcPrimeOneSecond()
	fmt.Printf("Found %d primes in 1 second\n", found)
	fmt.Println("Handler done")
	return true, nil
}

func main() {
	fmt.Println("Init starting")
	var found int = calcPrimeOneSecond()
	fmt.Printf("Found %d primes in 1 second\n", found)
	fmt.Println("Init done")
	lambda.Start(HandleRequest)
}

func calcPrimeOneSecond() int {
	var i int64 = 1
	var found int = 0
	for start := time.Now(); time.Since(start) < time.Second; {
		if big.NewInt(i).ProbablyPrime(0) {
			found++
		}
		i = i + 2
	}

	return found
}
