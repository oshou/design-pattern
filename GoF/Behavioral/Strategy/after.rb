class Customer
	def order(drink)
		barista = Barista.new
		barista.brew(drink)
	end
end

class Cappuccino
	def brew
		espresso=Espresso.new
		milk=Milk.new
		cup = Cup.new
		cup.receive(espresso.brew,milk.steam)
	end
end

class IcedCoffee
	def brew
		ice=Ice.new
		cup=Cup.new
		cup.receive(coffee_bean.brew,ice.make)
	end
end
