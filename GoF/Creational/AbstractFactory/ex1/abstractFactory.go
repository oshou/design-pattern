package abstract_factory

//継承ではなくインターフェースによるポリモーフィズム
type item interface {
	toString() string
}

// インターフェースの埋め込みも可能
type link interface {
	item
}

type tray interface {
	item
	AddToTray(item item)
}

type baseTray struct {
	tray []item
}

func (self *baseTray) AddToTray(item item) {
	self.tray = append(self.tray, item)
}
