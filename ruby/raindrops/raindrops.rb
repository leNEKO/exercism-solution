# Raindrops : integer to plingplong transformizer
class Raindrops
  def self.convert(int)
    r = ''
    r += (int % 3).zero? ? 'Pling' : ''
    r += (int % 5).zero? ? 'Plang' : ''
    r += (int % 7).zero? ? 'Plong' : ''
    r != '' ? r : String(int)
  end
end
