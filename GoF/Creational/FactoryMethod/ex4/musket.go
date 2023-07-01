package main

type Musket struct {
	Gun
}

func newMusket() IGun {
	return &Musket{
		Gun: Gun{
			name:  "musket gun",
			power: 1,
		},
	}
}
