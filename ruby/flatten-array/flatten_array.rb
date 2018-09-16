'''
not sure if the point is to write a full featured custom flatten function or just getting rid of "nil"s
'''
class FlattenArray
    def self.flatten(a)
        a.flatten.select {|item| item != nil}
    end
end

if __FILE__ == $0
    puts FlattenArray.flatten([1,2,3,[4,5,6]])
end