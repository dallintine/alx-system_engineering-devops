<<<<<<< HEAD
# Create a file in /tmp

file { 'school':
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
  path    => '/tmp/school',
=======
<<<<<<< HEAD
# creates a file in /tmp

file { '/tmp/school':
  content =>'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
=======
# Using Puppet, create a file in '/tmp'.
file { '/tmp/holberton':
  ensure  => 'file',
  path    => '/tmp/holberton',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
>>>>>>> f76b6430d14c5b3cfa515ade96aecd5011262cd8
>>>>>>> 21c35ece6033d103b3c189a01f16aaaae15e1f54
}
