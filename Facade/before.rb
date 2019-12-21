class Customer
	def order
		espresso = Espresso.new
		milk=Milk.new
		cup = Cup.new
		cup.receive(espresso.brew,milk.steam)
	end
end

customer = Customer.new
puts customer.order
