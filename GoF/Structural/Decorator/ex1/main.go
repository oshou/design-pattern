package main

import "fmt"

func main() {
	pizza := &PlainPizza{}

	pizzaWithCheese := &CheeseTopping{
		pizza: pizza,
	}

	pizzaWithCheeseAndTomato := &TomatoTopping{
		pizza: pizzaWithCheese,
	}

	fmt.Printf("Price(tomato+cheese):%v\n", pizzaWithCheeseAndTomato.getPrice())
}
