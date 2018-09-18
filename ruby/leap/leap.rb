# check if year is leap
class Year
  def self.leap?(year)
    mod4 = (year % 4).zero?
    mod100 = !(year % 100).zero?
    mod400 = (year % 400).zero?
    mod4 && (mod100 || mod400)
  end
end
