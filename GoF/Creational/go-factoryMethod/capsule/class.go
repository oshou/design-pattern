package class

/*
- ポリモーフィズム
// https://qiita.com/kitoko552/items/a6698c68379a8cd8b999
*/

type Human struct {
	name string
}

// コンストラクタ
func NewHuman(name string) *Human {
	return &Human{name: name}
}

// カプセル化
func (h Human) GetName() string {
	return h.name
}

func (h Human) SetName(name string) {
	h.name = name
}
