# FlattenArray: removing 'nil's
class FlattenArray
  def self.flatten(nested_arrays)
    nested_arrays.flatten.reject(&:nil?)
  end
end
