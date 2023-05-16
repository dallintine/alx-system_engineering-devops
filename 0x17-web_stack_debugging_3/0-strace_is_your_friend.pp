<<<<<<< HEAD
# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`.

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
=======
#Fix the log Errors, catch the error and fix it
exec {'/etc/php5/apache2/php.ini':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sed -i 's/display_errors = Off/display_errors = On/g' /etc/php5/apache2/php.ini",
}

exec { '/var/www/html/wp-setting.php':
  path    => [ '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin' ],
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
}

exec {'/etc/init.d/apache2':
  path    => ['/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'],
  command => '/etc/init.d/apache2 restart',
>>>>>>> 21c35ece6033d103b3c189a01f16aaaae15e1f54
}
