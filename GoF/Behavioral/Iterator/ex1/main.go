package main

import "fmt"

func main() {
	userCollection := &userCollection{
		users: []*User{
			&User{
				name: "a",
				age:  30,
			},
			&User{
				name: "b",
				age:  20,
			},
		},
	}

	iterator := userCollection.createIterator()

	for iterator.hasNext() {
		user := iterator.getNext()
		fmt.Printf("User is %+v\n", user)
	}
}
