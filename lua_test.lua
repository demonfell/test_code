function has_value (tab, val)
    for index, value in ipairs(tab) do           
     if value == val then                  
        return true                
        end              
    end
     return false                
end

puzzle_word = "computer"
my_guesses={}
table.insert(my_guesses,"c")

for i=1,#puzzle_word do
    for k,v in pairs(my_guesses) do
          local c = puzzle_word:sub(i,i)
            if has_value(c,v) then
                io.write(c)
             else
                io.write("_ ") 
            end
        end
    end