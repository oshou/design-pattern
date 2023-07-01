package main

import "fmt"

func main() {
	adidasFactory, err := GetSportsFactory("adidas")
	if err != nil {
		fmt.Println(err)
	}

	nikeFactory, err := GetSportsFactory("nike")
	if err != nil {
		fmt.Println(err)
	}

	adidasShoe := adidasFactory.makeShoe()
	adidasShirt := adidasFactory.makeShirt()

	nikeShoe := nikeFactory.makeShoe()
	nikeShirt := nikeFactory.makeShirt()

	printShoeDetail(adidasShoe)
	printShirtDetail(adidasShirt)

	printShoeDetail(nikeShoe)
	printShirtDetail(nikeShirt)
}

func printShoeDetail(s IShoe) {
	fmt.Printf("Logo: %v\n", s.getLogo())
	fmt.Printf("Size: %v\n", s.getSize())
}

func printShirtDetail(s IShirt) {
	fmt.Printf("Logo: %v\n", s.getLogo())
	fmt.Printf("Size: %v\n", s.getSize())
}
