package main

import "fmt"

func fib() func() int {
	a, b := 0, 1
	return func() int {
		a, b = b, a+b
		return a
	}
}

type Tasker interface {
	GetNewOne()
}

type TaskFactory struct{}

func (tf TaskFactory) create(string owner) {

}

func main() {
	f := fib()
	for i := 0; i < 10; i++ {
		fmt.Println(f())
	}
}
