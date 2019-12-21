class Customer
	def order(type)
		barista=Barista.new
		barista.brew(type)
	end
end

class Barista
	def brew(type)
		case type
		when :cappuccino
			espresso=Espresso.new
			milk=Milk.new
			cup=Cup.new
			cup.receive(espresso.brew,mil.steam)
		when :iced_coffee
			coffee_bean= BitterCoffeeBean.new
			ice=Ice.new
			cup=Cup.new
			cup.receive(coffee_bean.brew,ice.make)
		end
	end
end

custommer = Customer.new
customer.order(:cappuccino)
customer.order(:iced_coffee)
