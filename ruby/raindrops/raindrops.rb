# Raindrops : slighty better at doing the sounds
class Raindrops
  PRIME_TO_SOUND = {
    3 => 'Pling',
    5 => 'Plang',
    7 => 'Plong'
  }.freeze

  def self.convert(int)
    sounds = PRIME_TO_SOUND
             .select { |prime, _| (int % prime).zero? }
             .values

    sounds.any? ? sounds.join : int.to_s
  end
end
