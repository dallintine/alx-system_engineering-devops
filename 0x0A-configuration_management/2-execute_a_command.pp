<<<<<<< HEAD
#!/usr/bin/pup

# a script that kills a process named killmenow

exec { 'pkill':
  provider => 'shell',
  command  => 'pkill -f killmenow',
=======
# https://puppet.com/docs/puppet/3.8/type.html#exec
# Kills a process
exec {  'killmenow':
  command  => '/usr/bin/pkill killmenow',
  provider => 'shell',
  returns  => [0, 1],
>>>>>>> f76b6430d14c5b3cfa515ade96aecd5011262cd8
}
