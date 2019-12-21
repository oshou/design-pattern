class ObscuringReferences
  attr_reader :data

  def initialize(data)
    @data = data
  end

  # dataの構造に依存したメソッド
  def diameters
    p data
    data.collect { |cell|
      cell[0] + (cell[1] * 2)
    }
  end
end

data = [[622, 20], [622, 23], [559, 30], [559, 40]]
p ObscuringReferences.new(data).diameters
