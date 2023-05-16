#!/usr/bin/env ruby
<<<<<<< HEAD
puts ARGV[0].scan(/(?<=from:|to:|flags:)[\w|\+|\-|\:]*(?=\])/).join(",")
=======
<<<<<<< HEAD
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
=======
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).join(',')
>>>>>>> f76b6430d14c5b3cfa515ade96aecd5011262cd8
>>>>>>> 21c35ece6033d103b3c189a01f16aaaae15e1f54
