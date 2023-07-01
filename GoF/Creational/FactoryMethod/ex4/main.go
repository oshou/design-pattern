package main

import (
	"fmt"
	"log"
)

func main() {
	ak47, err := getGun("ak47")
	if err != nil {
		log.Fatalln(err)
	}

	musket, err := getGun("musket")
	if err != nil {
		log.Fatalln(err)
	}

	printDetails(ak47)
	printDetails(musket)
}

func printDetails(g IGun) {
	fmt.Printf("Name: %v\n", g.getName())
	fmt.Printf("Power: %v\n", g.getPower())
}
