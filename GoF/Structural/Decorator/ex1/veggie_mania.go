package main

type PlainPizza struct{}

func (p *PlainPizza) getPrice() int {
	return 15
}
