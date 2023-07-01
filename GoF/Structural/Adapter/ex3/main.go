package main

func main() {
	client := &Client{}
	mac := &Mac{}

	client.InsertLightningConnectorIntoComputer(mac)

	windows := &Windows{}
	WindowsAdapter := &WindowsAdapter{
		windowMachine: windows,
	}

	client.InsertLightningConnectorIntoComputer(WindowsAdapter)
}
