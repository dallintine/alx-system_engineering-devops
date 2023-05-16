<<<<<<< HEAD
# Installs puppet-lint

package { 'puppet-lint':
  ensure   => '2.5.0',
  provider => 'gem',
=======
<<<<<<< HEAD
#!/usr/bin/pup
# installing a specific version of flask 2.1.0

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
=======
# Read: http://puppet-lint.com/checks/
# Using Puppet, install puppet-lint.
package { 'puppet-lint':
  ensure   => '2.1.1',
  provider => 'gem',
>>>>>>> f76b6430d14c5b3cfa515ade96aecd5011262cd8
>>>>>>> 21c35ece6033d103b3c189a01f16aaaae15e1f54
}
