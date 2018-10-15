module Acronym
  def self.abbreviate(words)
    words.scan(/(\w)\w*/).join.upcase
  end
end
